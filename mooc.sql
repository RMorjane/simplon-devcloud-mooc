CREATE DATABASE mooc;
USE mooc;
CREATE TABLE Need (
	quantity DOUBLE PRECISION NOT NULL,
	materialID INTEGER NOT NULL,
	coursID INTEGER NOT NULL,
	CONSTRAINT PK_Need11 PRIMARY KEY (materialID, coursID)
	);
CREATE INDEX TC_Need11 ON Need (coursID );
CREATE INDEX TC_Need10 ON Need (materialID );
CREATE TABLE Step (
	stepID INTEGER NOT NULL AUTO_INCREMENT,
	label VARCHAR ( 255 ) NOT NULL,
	paragraph VARCHAR ( 255 ) NOT NULL,
	coursID INTEGER NOT NULL,
	CONSTRAINT PK_Step5 PRIMARY KEY (stepID)
	);
CREATE INDEX TC_Step7 ON Step (coursID );
CREATE TABLE Role (
	roleID INTEGER NOT NULL AUTO_INCREMENT,
	rolename VARCHAR ( 255 ) NOT NULL,
	CONSTRAINT PK_Role0 PRIMARY KEY (roleID)
	);
CREATE TABLE Review (
	datereview DATE NOT NULL,
	comment VARCHAR ( 255 ) NOT NULL,
	note DOUBLE PRECISION NOT NULL,
	coursID INTEGER NOT NULL,
	roleID INTEGER NOT NULL,
	userID INTEGER NOT NULL,
	CONSTRAINT PK_Review6 PRIMARY KEY (coursID , userID)
	);
CREATE INDEX TC_Review5 ON Review (roleID , userID );
CREATE INDEX TC_Review4 ON Review (coursID );
CREATE TABLE User (
	userID INTEGER NOT NULL AUTO_INCREMENT,
	username VARCHAR ( 255 ) NOT NULL,
	password VARCHAR ( 255 ) NOT NULL,
	email VARCHAR ( 255 ) NOT NULL,
	roleID INTEGER NOT NULL,
	CONSTRAINT PK_User3 PRIMARY KEY (userID)
	);
CREATE INDEX TC_User3 ON User (roleID );
CREATE TABLE Permission (
	state SMALLINT NOT NULL,
	privilegeID INTEGER NOT NULL,
	roleID INTEGER NOT NULL,
	CONSTRAINT PK_Permission2 PRIMARY KEY (privilegeID, roleID)
	);
CREATE INDEX TC_Permission1 ON Permission (roleID );
CREATE INDEX TC_Permission0 ON Permission (privilegeID );
CREATE TABLE Material (
	materialID INTEGER NOT NULL AUTO_INCREMENT,
	label VARCHAR ( 255 ) NOT NULL,
	CONSTRAINT PK_Material10 PRIMARY KEY (materialID)
	);
CREATE TABLE Privilege (
	privilegeID INTEGER NOT NULL AUTO_INCREMENT,
	privilegename VARCHAR ( 255 ) NOT NULL,
	CONSTRAINT PK_Privilege1 PRIMARY KEY (privilegeID)
	);
CREATE TABLE Cours (
	coursID INTEGER NOT NULL AUTO_INCREMENT,
	title VARCHAR ( 255 ) NOT NULL,
	datecreated DATE NOT NULL,
	description VARCHAR ( 255 ) NOT NULL,
	estimatedtime VARCHAR ( 255 ) NOT NULL,
	CONSTRAINT PK_Cours4 PRIMARY KEY (coursID)
	);
ALTER TABLE Permission ADD CONSTRAINT FK_Permission1 FOREIGN KEY (roleID) REFERENCES Role (roleID)  ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Permission ADD CONSTRAINT FK_Permission0 FOREIGN KEY (privilegeID) REFERENCES Privilege (privilegeID)  ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE User ADD CONSTRAINT FK_User2 FOREIGN KEY (roleID) REFERENCES Role (roleID)  ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE Review ADD CONSTRAINT FK_Review4 FOREIGN KEY (roleID, userID) REFERENCES User (roleID, userID)  ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE Review ADD CONSTRAINT FK_Review3 FOREIGN KEY (coursID) REFERENCES Cours (coursID)  ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Step ADD CONSTRAINT FK_Step5 FOREIGN KEY (coursID) REFERENCES Cours (coursID)  ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE Need ADD CONSTRAINT FK_Need7 FOREIGN KEY (materialID) REFERENCES Material (materialID)  ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE Need ADD CONSTRAINT FK_Need8 FOREIGN KEY (coursID) REFERENCES Cours (coursID)  ON DELETE CASCADE ON UPDATE CASCADE;

INSERT INTO Role(rolename) VALUES('Lambda'),('SuperUser');
INSERT INTO Privilege(privilegename)
VALUES('read cours'),('add cours'),('update cours'),('delete cours'),
('read comment'),('add comment'),('delete comment'),('add note');
INSERT INTO Permission(roleID,privilegeID,state)
VALUES(1,1,1),(1,2,0),(1,3,0),(1,4,0),(1,5,1),(1,6,1),(1,7,0),(1,8,1),
(2,1,1),(2,2,1),(2,3,1),(2,4,1),(2,5,1),(2,6,1),(2,7,1),(2,8,1);