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

-- Table usuario

CREATE TABLE "usuario"
(
  "id" Serial NOT NULL,
  "nome" Character varying(50) NOT NULL,
  "senha" Character varying NOT NULL,
  "email" Character varying(30) NOT NULL,
  "nascimento" Date NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "usuario" ADD CONSTRAINT "Key5" PRIMARY KEY ("id")
;
-- Table exercicio

CREATE TABLE "exercicio"
(
  "id" Serial NOT NULL,
  "nome" Character varying(20) NOT NULL,
  "descricao" Character varying(50) NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "exercicio" ADD CONSTRAINT "Key6" PRIMARY KEY ("id")
;
-- Table ficha

CREATE TABLE "ficha"
(
  "id" Serial NOT NULL,
  "id_usuario" Integer NOT NULL,
  "data" Date NOT NULL,
  "data_troca" Date NOT NULL,
  "descricao" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "ficha" ADD CONSTRAINT "Key7" PRIMARY KEY ("id","id_usuario")
;
-- Table avaliacao

CREATE TABLE "avaliacao"
(
  "id" Serial NOT NULL,
  "id_usuario" Integer NOT NULL,
  "data" Date NOT NULL,
  "peso" Numeric(5,2) NOT NULL,
  "percentual_gordura" Numeric(5,2) NOT NULL,
  "pescoco" Numeric(6,2) NOT NULL,
  "ombro" Numeric(6,2) NOT NULL,
  "torax" Numeric(6,2) NOT NULL,
  "abdomen" Numeric(6,2) NOT NULL,
  "cintura" Numeric(6,2) NOT NULL,
  "quadril" Numeric(6,2) NOT NULL,
  "braco_esquerdo" Numeric(6,2) NOT NULL,
  "braco_direito" Numeric(6,2) NOT NULL,
  "antebraco_esquerdo" Numeric(6,2) NOT NULL,
  "antebraco_direito" Numeric(6,2) NOT NULL,
  "coxa_esquerda" Numeric(6,2) NOT NULL,
  "coxa_direita" Numeric(6,2) NOT NULL,
  "panturrilha_esquerda" Numeric(6,2) NOT NULL,
  "panturrilha_direita" Numeric(6,2) NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "avaliacao" ADD CONSTRAINT "Key8" PRIMARY KEY ("id","id_usuario")
;
-- Table treino

CREATE TABLE "treino"
(
  "id" Serial NOT NULL,
  "id_ficha" Integer NOT NULL,
  "id_usuario" Integer NOT NULL,
  "numero_treino" Smallint NOT NULL,
  "descricao" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "treino" ADD CONSTRAINT "Key14" PRIMARY KEY ("id_ficha","id","id_usuario")
;
-- Table musculo

CREATE TABLE "musculo"
(
  "id" Serial NOT NULL,
  "nome" Character varying NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "musculo" ADD CONSTRAINT "Key16" PRIMARY KEY ("id")
;
-- Table musculo_exercicio

CREATE TABLE "musculo_exercicio"
(
  "id_exercicio" Integer NOT NULL,
  "id_musculo" Integer NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "musculo_exercicio" ADD CONSTRAINT "Key18" PRIMARY KEY ("id_exercicio","id_musculo")
;
-- Table aparelho

CREATE TABLE "aparelho"
(
  "id" Serial NOT NULL,
  "nome" Character varying NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "aparelho" ADD CONSTRAINT "Key19" PRIMARY KEY ("id")
;
-- Table aparelho_exercicio

CREATE TABLE "aparelho_exercicio"
(
  "id_exercicio" Integer NOT NULL,
  "id_aparelho" Integer NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "aparelho_exercicio" ADD CONSTRAINT "Key20" PRIMARY KEY ("id_exercicio","id_aparelho")
;
-- Table atividade

CREATE TABLE "atividade"
(
  "id" Serial NOT NULL,
  "id_ficha" Integer NOT NULL,
  "id_treino" Integer NOT NULL,
  "id_usuario" Integer NOT NULL,
  "id_exercicio" Integer NOT NULL,
  "id_aparelho" Integer NOT NULL,
  "series" Smallint NOT NULL,
  "ordem_execucao" Smallint NOT NULL,
  "peso" Smallint,
  "repeticoes" Character varying(20),
  "observacoes" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "atividade" ADD CONSTRAINT "Key21" PRIMARY KEY ("id_exercicio","id_aparelho","id_ficha","id_treino","id_usuario","id")
;
-- Table objetivo

CREATE TABLE "objetivo"
(
  "id" Serial NOT NULL,
  "nome" Character varying NOT NULL,
  "descricao" Character varying NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "objetivo" ADD CONSTRAINT "Key22" PRIMARY KEY ("id")
;
-- Table objetivo_ficha

CREATE TABLE "objetivo_ficha"
(
  "id_objetivo" Integer NOT NULL,
  "id_ficha" Integer NOT NULL,
  "id_usuario" Integer NOT NULL
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "objetivo_ficha" ADD CONSTRAINT "Key23" PRIMARY KEY ("id_objetivo","id_ficha","id_usuario")
;
-- Table dia_atividade

CREATE TABLE "dia_atividade"
(
  "id" Serial NOT NULL,
  "id_atividade" Integer NOT NULL,
  "id_exercicio" Integer NOT NULL,
  "nro_aparelho" Integer NOT NULL,
  "id_ficha" Integer NOT NULL,
  "id_treino" Integer NOT NULL,
  "id_usuario" Integer NOT NULL,
  "data_inicio" Date NOT NULL,
  "data_fim" Date
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "dia_atividade" ADD CONSTRAINT "Key24" PRIMARY KEY ("id_exercicio","nro_aparelho","id","id_ficha","id_treino","id_usuario","id_atividade")
;
-- Table categoria_exercicio

CREATE TABLE "categoria_exercicio"
(
  "id" Serial NOT NULL,
  "nome" Character varying(50) NOT NULL,
  "descricao" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "categoria_exercicio" ADD CONSTRAINT "PK_categoria_exercicio" PRIMARY KEY ("id")
;
-- Table modificadores_atividades

CREATE TABLE "modificadores_atividades"
(
  "cod_exercicio" Integer NOT NULL,
  "id_aparelho" Integer NOT NULL,
  "id_modificador" Integer NOT NULL,
  "id_ficha" Integer NOT NULL,
  "id_treino" Integer NOT NULL,
  "id_usuario" Integer NOT NULL,
  "id_atividade" Integer NOT NULL,
  "observacoes" Character varying(255)
)
WITH (
  autovacuum_enabled=true)
;

ALTER TABLE "modificadores_atividades" ADD CONSTRAINT "PK_modificadores_atividades" PRIMARY KEY ("cod_exercicio","id_aparelho","id_modificador","id_ficha","id_treino","id_usuario","id_atividade")
;
-- Create foreign keys (relationships) section ------------------------------------------------- 

ALTER TABLE "treino" ADD CONSTRAINT "Relationship17" FOREIGN KEY ("id_ficha", "id_usuario") REFERENCES "ficha" ("id", "id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "musculo_exercicio" ADD FOREIGN KEY ("id_exercicio") REFERENCES "exercicio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "musculo_exercicio" ADD FOREIGN KEY ("id_musculo") REFERENCES "musculo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "aparelho_exercicio" ADD FOREIGN KEY ("id_exercicio") REFERENCES "exercicio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "aparelho_exercicio" ADD CONSTRAINT "Relationship24" FOREIGN KEY ("id_aparelho") REFERENCES "aparelho" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "atividade" ADD FOREIGN KEY ("id_exercicio", "id_aparelho") REFERENCES "aparelho_exercicio" ("id_exercicio", "id_aparelho") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "atividade" ADD FOREIGN KEY ("id_ficha", "id_treino", "id_usuario") REFERENCES "treino" ("id_ficha", "id", "id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "objetivo_ficha" ADD FOREIGN KEY ("id_objetivo") REFERENCES "objetivo" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "dia_atividade" ADD CONSTRAINT "Relationship29" FOREIGN KEY ("id_exercicio", "nro_aparelho", "id_ficha", "id_treino", "id_usuario", "id_atividade") REFERENCES "atividade" ("id_exercicio", "id_aparelho", "id_ficha", "id_treino", "id_usuario", "id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "modificadores_atividades" ADD FOREIGN KEY ("cod_exercicio", "id_aparelho", "id_ficha", "id_treino", "id_usuario", "id_atividade") REFERENCES "atividade" ("id_exercicio", "id_aparelho", "id_ficha", "id_treino", "id_usuario", "id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "modificadores_atividades" ADD FOREIGN KEY ("id_modificador") REFERENCES "categoria_exercicio" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "ficha" ADD FOREIGN KEY ("id_usuario") REFERENCES "usuario" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "objetivo_ficha" ADD FOREIGN KEY ("id_ficha", "id_usuario") REFERENCES "ficha" ("id", "id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION
;

ALTER TABLE "avaliacao" ADD FOREIGN KEY ("id_usuario") REFERENCES "usuario" ("id") ON DELETE NO ACTION ON UPDATE NO ACTION
;




