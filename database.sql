/*
Created: 19/04/2018
Modified: 11/04/2020
Project: SmartTraining
Model: PostgreSQL 9.4
Company: Jamal & Felipe produções
Author: Jamal e mais ou menos o Felipe
Version: 1.0
Database: PostgreSQL 9.4
*/

-- Create tables section -------------------------------------------------

-- Table user

CREATE TABLE "user"
(
  "id" Serial NOT NULL,
  "name" Character varying(50) NOT NULL,
  "password" Character varying NOT NULL,
  "email" Character varying(30) NOT NULL,
  "birth_date" Date NOT NULL,
  UNIQUE("email")
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "user" ADD CONSTRAINT "PK_user" PRIMARY KEY ("id")
;

-- Table exercise

CREATE TABLE "exercise"
(
  "id" Serial NOT NULL,
  "name" Character varying(20) NOT NULL,
  "description" Character varying(50) NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "exercise" ADD CONSTRAINT "PK_exercise" PRIMARY KEY ("id")
;
-- Table workout_plan

CREATE TABLE "workout_plan"
(
  "id" Serial NOT NULL,
  "user_id" Integer NOT NULL,
  "date" Date NOT NULL,
  "change_date" Date NOT NULL,
  "description" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "workout_plan" ADD CONSTRAINT "PK_workout_plan" PRIMARY KEY ("id","user_id")
;
-- Table assessment

CREATE TABLE "assessment"
(
  "id" Serial NOT NULL,
  "user_id" Integer NOT NULL,
  "date" Date NOT NULL,
  "weight" Numeric(5,2) NOT NULL,
  "fat_percentage" Numeric(5,2) NOT NULL,
  "neck" Numeric(6,2) NOT NULL,
  "shoulder" Numeric(6,2) NOT NULL,
  "torax" Numeric(6,2) NOT NULL,
  "abdomen" Numeric(6,2) NOT NULL,
  "waist" Numeric(6,2) NOT NULL,
  "hip" Numeric(6,2) NOT NULL,
  "left_arm" Numeric(6,2) NOT NULL,
  "right_arm" Numeric(6,2) NOT NULL,
  "left_forearm" Numeric(6,2) NOT NULL,
  "right_forearm" Numeric(6,2) NOT NULL,
  "left_thigh" Numeric(6,2) NOT NULL,
  "right_thigh" Numeric(6,2) NOT NULL,
  "left_calf" Numeric(6,2) NOT NULL,
  "right_calf" Numeric(6,2) NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "assessment" ADD CONSTRAINT "PK_assessment" PRIMARY KEY ("id","user_id")
;
-- Table workout

CREATE TABLE "workout"
(
  "id" Serial NOT NULL,
  "workout_plan_id" Integer NOT NULL,
  "user_id" Integer NOT NULL,
  "workout_number" Smallint NOT NULL,
  "description" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "workout" ADD CONSTRAINT "PK_workout" PRIMARY KEY ("workout_plan_id","id","user_id")
;
-- Table muscle

CREATE TABLE "muscle"
(
  "id" Serial NOT NULL,
  "name" Character varying NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "muscle" ADD CONSTRAINT "PK_muscle" PRIMARY KEY ("id")
;
-- Table exercice_muscle

CREATE TABLE "exercice_muscle"
(
  "exercise_id" Integer NOT NULL,
  "muscle_id" Integer NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "exercice_muscle" ADD CONSTRAINT "PK_exercise_muscle" PRIMARY KEY ("exercise_id","muscle_id")
;
-- Table equipment

CREATE TABLE "equipment"
(
  "id" Serial NOT NULL,
  "name" Character varying NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "equipment" ADD CONSTRAINT "PK_equipment" PRIMARY KEY ("id")
;
-- Table exercise_equipment

CREATE TABLE "exercise_equipment"
(
  "exercise_id" Integer NOT NULL,
  "equipment_id" Integer NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "exercise_equipment" ADD CONSTRAINT "PK_exercise_equipment" PRIMARY KEY ("exercise_id","equipment_id")
;
-- Table activity

CREATE TABLE "activity"
(
  "id" Serial NOT NULL,
  "workout_plan_id" Integer NOT NULL,
  "workout_id" Integer NOT NULL,
  "user_id" Integer NOT NULL,
  "exercise_id" Integer NOT NULL,
  "equipment_id" Integer NOT NULL,
  "sets" Smallint NOT NULL,
  "execution_order" Smallint NOT NULL,
  "weight" Smallint,
  "repetitions" Character varying(20),
  "observations" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "activity" ADD CONSTRAINT "PK_activity" PRIMARY KEY ("exercise_id","equipment_id","workout_plan_id","workout_id","user_id","id")
;
-- Table goal

CREATE TABLE "goal"
(
  "id" Serial NOT NULL,
  "name" Character varying NOT NULL,
  "description" Character varying NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "goal" ADD CONSTRAINT "PK_goal" PRIMARY KEY ("id")
;
-- Table workout_plan_goal

CREATE TABLE "workout_plan_goal"
(
  "id_goal" Integer NOT NULL,
  "workout_plan_id" Integer NOT NULL,
  "user_id" Integer NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "workout_plan_goal" ADD CONSTRAINT "PK_workout_plan_goal" PRIMARY KEY ("id_goal","workout_plan_id","user_id")
;
-- Table activity_day

CREATE TABLE "activity_day"
(
  "id" Serial NOT NULL,
  "activity_id" Integer NOT NULL,
  "exercise_id" Integer NOT NULL,
  "equipment_number" Integer NOT NULL,
  "workout_plan_id" Integer NOT NULL,
  "workout_id" Integer NOT NULL,
  "user_id" Integer NOT NULL,
  "start_date" Date NOT NULL,
  "end_date" Date
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "activity_day" ADD CONSTRAINT "PK_activity_day" PRIMARY KEY ("exercise_id","equipment_number","id","workout_plan_id","workout_id","user_id","activity_id")
;
-- Table exercise_category

CREATE TABLE "exercise_category"
(
  "id" Serial NOT NULL,
  "name" Character varying(50) NOT NULL,
  "description" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "exercise_category" ADD CONSTRAINT "PK_exercise_category" PRIMARY KEY ("id")
;
-- Table activities_modifiers

CREATE TABLE "activities_modifiers"
(
  "exercise_id" Integer NOT NULL,
  "equipment_id" Integer NOT NULL,
  "modifier_id" Integer NOT NULL,
  "workout_plan_id" Integer NOT NULL,
  "workout_id" Integer NOT NULL,
  "user_id" Integer NOT NULL,
  "activity_id" Integer NOT NULL,
  "observations" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "activities_modifiers" ADD CONSTRAINT "PK_activities_modifiers" PRIMARY KEY ("exercise_id","equipment_id","modifier_id","workout_plan_id","workout_id","user_id","activity_id")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "workout" ADD CONSTRAINT "FK_workout" FOREIGN KEY ("workout_plan_id", "user_id") REFERENCES "workout_plan" ("id", "user_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "exercice_muscle" ADD FOREIGN KEY ("exercise_id") REFERENCES "exercise" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "exercice_muscle" ADD FOREIGN KEY ("muscle_id") REFERENCES "muscle" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "exercise_equipment" ADD FOREIGN KEY ("exercise_id") REFERENCES "exercise" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "exercise_equipment" ADD CONSTRAINT "FK_exercise_equipment" FOREIGN KEY ("equipment_id") REFERENCES "equipment" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "activity" ADD FOREIGN KEY ("exercise_id", "equipment_id") REFERENCES "exercise_equipment" ("exercise_id", "equipment_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "activity" ADD FOREIGN KEY ("workout_plan_id", "workout_id", "user_id") REFERENCES "workout" ("workout_plan_id", "id", "user_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "workout_plan_goal" ADD FOREIGN KEY ("id_goal") REFERENCES "goal" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "activity_day" ADD CONSTRAINT "FK_activity_day" FOREIGN KEY ("exercise_id", "equipment_number", "workout_plan_id", "workout_id", "user_id", "activity_id") REFERENCES "activity" ("exercise_id", "equipment_id", "workout_plan_id", "workout_id", "user_id", "id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "activities_modifiers" ADD FOREIGN KEY ("exercise_id", "equipment_id", "workout_plan_id", "workout_id", "user_id", "activity_id") REFERENCES "activity" ("exercise_id", "equipment_id", "workout_plan_id", "workout_id", "user_id", "id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "activities_modifiers" ADD FOREIGN KEY ("modifier_id") REFERENCES "exercise_category" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "workout_plan" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "workout_plan_goal" ADD FOREIGN KEY ("workout_plan_id", "user_id") REFERENCES "workout_plan" ("id", "user_id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "assessment" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;




