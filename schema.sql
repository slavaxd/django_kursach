BEGIN;
--
-- Create model Bike
--
CREATE TABLE "allinone_bike" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "kind_of_bike" varchar(255) NOT NULL, "made_by" varchar(255) NOT NULL, "material" varchar(255) NOT NULL, "weight" varchar(255) NOT NULL, "color" varchar(255) NOT NULL, "country" varchar(255) NOT NULL, "price" integer NOT NULL);
--
-- Create model Coach
--
CREATE TABLE "allinone_coach" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "age" integer NOT NULL, "birthday" datetime NOT NULL, "birthplace" varchar(255) NOT NULL);
--
-- Create model Competition
--
CREATE TABLE "allinone_competition" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "country" varchar(255) NOT NULL, "city" varchar(255) NOT NULL);
--
-- Create model Organizator
--
CREATE TABLE "allinone_organizator" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "birthday" datetime NOT NULL);
--
-- Create model Participant
--
CREATE TABLE "allinone_participant" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "age" integer NOT NULL, "birthday" datetime NOT NULL, "birthplace" varchar(255) NOT NULL, "bike_id" integer NOT NULL UNIQUE REFERENCES "allinone_bike" ("id"));
--
-- Create model Team
--
CREATE TABLE "allinone_team" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL);
--
-- Add field team to participant
--
ALTER TABLE "allinone_participant" RENAME TO "allinone_participant__old";
CREATE TABLE "allinone_participant" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "age" integer NOT NULL, "birthday" datetime NOT NULL, "birthplace" varchar(255) NOT NULL, "bike_id" integer NOT NULL UNIQUE REFERENCES "allinone_bike" ("id"), "team_id" integer NOT NULL UNIQUE REFERENCES "allinone_team" ("id"));
INSERT INTO "allinone_participant" ("birthplace", "name", "age", "team_id", "birthday", "bike_id", "id") SELECT "birthplace", "name", "age", NULL, "birthday", "bike_id", "id" FROM "allinone_participant__old";
DROP TABLE "allinone_participant__old";
--
-- Add field organizator to competition
--
ALTER TABLE "allinone_competition" RENAME TO "allinone_competition__old";
CREATE TABLE "allinone_competition" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "country" varchar(255) NOT NULL, "city" varchar(255) NOT NULL, "organizator_id" integer NOT NULL REFERENCES "allinone_organizator" ("id"));
INSERT INTO "allinone_competition" ("organizator_id", "country", "city", "id", "name") SELECT NULL, "country", "city", "id", "name" FROM "allinone_competition__old";
DROP TABLE "allinone_competition__old";
CREATE INDEX "allinone_competition_60d48b1f" ON "allinone_competition" ("organizator_id");
--
-- Add field participants to competition
--
CREATE TABLE "allinone_competition_participants" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "competition_id" integer NOT NULL REFERENCES "allinone_competition" ("id"), "participant_id" integer NOT NULL REFERENCES "allinone_participant" ("id"));
--
-- Add field team to coach
--
ALTER TABLE "allinone_coach" RENAME TO "allinone_coach__old";
CREATE TABLE "allinone_coach" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "age" integer NOT NULL, "birthday" datetime NOT NULL, "birthplace" varchar(255) NOT NULL, "team_id" integer NOT NULL UNIQUE REFERENCES "allinone_team" ("id"));
INSERT INTO "allinone_coach" ("birthplace", "name", "age", "team_id", "birthday", "id") SELECT "birthplace", "name", "age", NULL, "birthday", "id" FROM "allinone_coach__old";
DROP TABLE "allinone_coach__old";
CREATE UNIQUE INDEX "allinone_competition_participants_competition_id_34e1105f_uniq" ON "allinone_competition_participants" ("competition_id", "participant_id");
CREATE INDEX "allinone_competition_participants_88606bbe" ON "allinone_competition_participants" ("competition_id");
CREATE INDEX "allinone_competition_participants_4a3c2f9c" ON "allinone_competition_participants" ("participant_id");
COMMIT;
