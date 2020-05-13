# -*- encoding: utf-8 -*-
# begin

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)



class User (db.Model):
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key = True)
    # Unknown SQL type: 'character varying(50)' 
    name = db.Column('name', db.String)
    # Unknown SQL type: 'character varying' 
    password = db.Column('password', db.String)
    # Unknown SQL type: 'character varying(30)' 
    email = db.Column('email', db.String)
    birth_date = db.Column('birth_date', db.Date)

class Exercise (db.Model):
    __tablename__ = "exercise"
    id = db.Column('id', db.Integer, primary_key = True)
    # Unknown SQL type: 'character varying(20)' 
    name = db.Column('name', db.String)
    # Unknown SQL type: 'character varying(50)' 
    description = db.Column('description', db.String)

class WorkoutPlan (db.Model):
    __tablename__ = "workout_plan"
    id = db.Column('id', db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key = True)
    date = db.Column('date', db.Date)
    change_date = db.Column('change_date', db.Date)
    # Unknown SQL type: 'character varying(255)' 
    description = db.Column('description', db.String)

    user = db.relationship('User', foreign_keys=user_id)

class Assessment (db.Model):
    __tablename__ = "assessment"
    id = db.Column('id', db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key = True)
    date = db.Column('date', db.Date)
    weight = db.Column('weight', db.BigInteger)
    fat_percentage = db.Column('fat_percentage', db.BigInteger)
    neck = db.Column('neck', db.BigInteger)
    shoulder = db.Column('shoulder', db.BigInteger)
    torax = db.Column('torax', db.BigInteger)
    abdomen = db.Column('abdomen', db.BigInteger)
    waist = db.Column('waist', db.BigInteger)
    hip = db.Column('hip', db.BigInteger)
    left_arm = db.Column('left_arm', db.BigInteger)
    right_arm = db.Column('right_arm', db.BigInteger)
    left_forearm = db.Column('left_forearm', db.BigInteger)
    right_forearm = db.Column('right_forearm', db.BigInteger)
    left_thigh = db.Column('left_thigh', db.BigInteger)
    right_thigh = db.Column('right_thigh', db.BigInteger)
    left_calf = db.Column('left_calf', db.BigInteger)
    right_calf = db.Column('right_calf', db.BigInteger)

    user = db.relationship('User', foreign_keys=user_id)

class Workout (db.Model):
    __tablename__ = "workout"
    id = db.Column('id', db.Integer, primary_key = True)
    workout_plan_id = db.Column('workout_plan_id', db.Integer, db.ForeignKey('workout_plan.id'), primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('workout_plan.user_id'), primary_key = True)
    # Unknown SQL type: 'smallint' 
    workout_number = db.Column('workout_number', db.String)
    # Unknown SQL type: 'character varying(255)' 
    description = db.Column('description', db.String)

class Muscle (db.Model):
    __tablename__ = "muscle"
    id = db.Column('id', db.Integer, primary_key = True)
    # Unknown SQL type: 'character varying' 
    name = db.Column('name', db.String)

class ExerciceMuscle (db.Model):
    __tablename__ = "exercice_muscle"
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key = True)
    muscle_id = db.Column('muscle_id', db.Integer, db.ForeignKey('muscle.id'), primary_key = True)

    exercise = db.relationship('Exercise', foreign_keys=exercise_id)
    muscle = db.relationship('Muscle', foreign_keys=muscle_id)

class Equipment (db.Model):
    __tablename__ = "equipment"
    id = db.Column('id', db.Integer, primary_key = True)
    # Unknown SQL type: 'character varying' 
    name = db.Column('name', db.String)

class ExerciseEquipment (db.Model):
    __tablename__ = "exercise_equipment"
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key = True)
    equipment_id = db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.id'), primary_key = True)

    exercise = db.relationship('Exercise', foreign_keys=exercise_id)
    equipment = db.relationship('Equipment', foreign_keys=equipment_id)

class Activity (db.Model):
    __tablename__ = "activity"
    id = db.Column('id', db.Integer, primary_key = True)
    workout_plan_id = db.Column('workout_plan_id', db.Integer, db.ForeignKey('workout.workout_plan_id'), primary_key = True)
    workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('workout.user_id'), primary_key = True)
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('exercise_equipment.exercise_id'), primary_key = True)
    equipment_id = db.Column('equipment_id', db.Integer, db.ForeignKey('exercise_equipment.equipment_id'), primary_key = True)
    # Unknown SQL type: 'smallint' 
    sets = db.Column('sets', db.String)
    # Unknown SQL type: 'smallint' 
    execution_order = db.Column('execution_order', db.String)
    # Unknown SQL type: 'smallint' 
    weight = db.Column('weight', db.String)
    # Unknown SQL type: 'character varying(20)' 
    repetitions = db.Column('repetitions', db.String)
    # Unknown SQL type: 'character varying(255)' 
    observations = db.Column('observations', db.String)

class Goal (db.Model):
    __tablename__ = "goal"
    id = db.Column('id', db.Integer, primary_key = True)
    # Unknown SQL type: 'character varying' 
    name = db.Column('name', db.String)
    # Unknown SQL type: 'character varying' 
    description = db.Column('description', db.String)

class WorkoutPlanGoal (db.Model):
    __tablename__ = "workout_plan_goal"
    id_goal = db.Column('id_goal', db.Integer, db.ForeignKey('goal.id'), primary_key = True)
    workout_plan_id = db.Column('workout_plan_id', db.Integer, db.ForeignKey('workout_plan.id'), primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('workout_plan.user_id'), primary_key = True)

    goal = db.relationship('Goal', foreign_keys=id_goal)

class ActivityDay (db.Model):
    __tablename__ = "activity_day"
    id = db.Column('id', db.Integer, primary_key = True)
    activity_id = db.Column('activity_id', db.Integer, db.ForeignKey('activity.id'), primary_key = True)
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('activity.exercise_id'), primary_key = True)
    equipment_number = db.Column('equipment_number', db.Integer, db.ForeignKey('activity.equipment_id'), primary_key = True)
    workout_plan_id = db.Column('workout_plan_id', db.Integer, db.ForeignKey('activity.workout_plan_id'), primary_key = True)
    workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('activity.workout_id'), primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('activity.user_id'), primary_key = True)
    start_date = db.Column('start_date', db.Date)
    end_date = db.Column('end_date', db.Date)

class ExerciseCategory (db.Model):
    __tablename__ = "exercise_category"
    id = db.Column('id', db.Integer, primary_key = True)
    # Unknown SQL type: 'character varying(50)' 
    name = db.Column('name', db.String)
    # Unknown SQL type: 'character varying(255)' 
    description = db.Column('description', db.String)

class ActivitiesModifiers (db.Model):
    __tablename__ = "activities_modifiers"
    exercise_id = db.Column('exercise_id', db.Integer, db.ForeignKey('activity.exercise_id'), primary_key = True)
    equipment_id = db.Column('equipment_id', db.Integer, db.ForeignKey('activity.equipment_id'), primary_key = True)
    modifier_id = db.Column('modifier_id', db.Integer, db.ForeignKey('exercise_category.id'), primary_key = True)
    workout_plan_id = db.Column('workout_plan_id', db.Integer, db.ForeignKey('activity.workout_plan_id'), primary_key = True)
    workout_id = db.Column('workout_id', db.Integer, db.ForeignKey('activity.workout_id'), primary_key = True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('activity.user_id'), primary_key = True)
    activity_id = db.Column('activity_id', db.Integer, db.ForeignKey('activity.id'), primary_key = True)
    # Unknown SQL type: 'character varying(255)' 
    observations = db.Column('observations', db.String)

    exercise_category = db.relationship('ExerciseCategory', foreign_keys=modifier_id)

# end
