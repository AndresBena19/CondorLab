CREATE DATABASE CondorLab;


USE condorlab;
CREATE TABLE User_Profile
(
id_user INTEGER AUTO_INCREMENT,
nm_first varchar(55),
nm_middle varchar(55),
nm_last varchar(55),

PRIMARY KEY (id_user)

);

CREATE TABLE User_role
(
id_user INTEGER ,
cd_role_type  varchar(55) ,
id_entity INTEGER ,
in_status INTEGER NOT NULL,

PRIMARY KEY (id_user, cd_role_type,id_entity)
);

CREATE TABLE User_address
(
id_address INTEGER ,
id_user INTEGER ,

PRIMARY KEY (id_address)
);

ALTER TABLE User_role ADD CONSTRAINT FK_id_user FOREIGN KEY (id_user) REFERENCES User_Profile (id_user);
ALTER TABLE User_address ADD CONSTRAINT FKN_id_user FOREIGN KEY (id_user) REFERENCES User_Profile (id_user); 





INSERT INTO user_profile (nm_first,nm_middle,nm_last)VALUES("Jose","Rafael","Martinez");
INSERT INTO user_profile (nm_first,nm_last)VALUES("William","Sanchez");
INSERT INTO user_profile (nm_first,nm_middle,nm_last) VALUES("Alvaro","Andres","Parra");
INSERT INTO user_profile (nm_first,nm_last) VALUES("Luis","Esquivia");
INSERT INTO user_profile (nm_first,nm_middle,nm_last)VALUES("Juan","Carlos","Aguilar");
INSERT INTO user_profile (nm_first,nm_middle,nm_last)VALUES("Pedro","Alverto","Sanchez");
INSERT INTO user_profile (nm_first,nm_middle,nm_last)VALUES("Lucas","Rafael","Escobar");
INSERT INTO user_profile (nm_first,nm_middle,nm_last)VALUES("Alfonso","Casseres","Sanchez");
INSERT INTO user_profile (nm_first,nm_last)VALUES("Pedro","villamisar");
INSERT INTO user_profile (nm_first,nm_last)VALUES("Esteban","Leal");
INSERT INTO user_profile (nm_first,nm_last)VALUES("Kevin","Rueda");
INSERT INTO user_profile (nm_first,nm_last)VALUES("Manolo","Gonzales");



INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(1,"Licensee",4221,1);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(2,"Limited",4321,0);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(3,"Provider",5432,1);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(4,"Provider",7854,1);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(5,"Provider",4321,0);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(6,"Licensee",5432,0);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(7,"Limited",8767,1);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(8,"Licensee",4321,1);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(9,"Licensee",4321,0);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(10,"Limited",4321,1);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(11,"Limited",4311,0);
INSERT INTO user_role (id_user,cd_role_type,id_entity,in_status)VALUES(12,"Provider",4321,1);


INSERT INTO user_address(id_user,id_address)VALUES(1, 213);
INSERT INTO user_address(id_user,id_address)VALUES(2,3432);
INSERT INTO user_address(id_user,id_address)VALUES(3, 435);
INSERT INTO user_address(id_user,id_address)VALUES(4,675);
INSERT INTO user_address(id_user,id_address)VALUES(5,54435);
INSERT INTO user_address(id_user,id_address)VALUES(6, 53242);
INSERT INTO user_address(id_user,id_address)VALUES(7,324);
INSERT INTO user_address(id_user,id_address)VALUES(8,5654);
INSERT INTO user_address(id_user,id_address)VALUES(9,34324);
INSERT INTO user_address(id_user,id_address)VALUES(10,45345);
INSERT INTO user_address(id_user,id_address)VALUES(11, 32131);
INSERT INTO user_address(id_user,id_address)VALUES(12, 5677);





