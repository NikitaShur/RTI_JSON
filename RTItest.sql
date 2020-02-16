
CREATE database if not exists db_RTItest character set utf8 collate utf8_unicode_ci;

use db_RTItest;

create table tbl_class (
	idclass smallint NOT null,
    name varchar(15),
    CONSTRAINT pk_class PRIMARY KEY (idclass)
);

create table tbl_teacher (
	idteacher smallint NOT NULL,
	fullname varchar(20),
	qualification varchar(20),
	CONSTRAINT pk_teacher PRIMARY KEY (idteacher)
);

create table tbl_subject (
	idsubject smallint NOT NULL,
	name varchar(20),
	CONSTRAINT pk_subject PRIMARY KEY (idsubject)
);

create table tbl_learningactivities (
	idclass smallint NOT NULL,
	idteacher smallint NOT NULL,
	idsubject smallint NOT NULL,
    CONSTRAINT fk_class_learningactivities FOREIGN KEY (idclass) REFERENCES tbl_class (idclass) MATCH FULL ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_teacher_learningactivities FOREIGN KEY (idteacher) REFERENCES tbl_teacher (idteacher) MATCH FULL ON DELETE NO ACTION ON UPDATE NO ACTION,
    CONSTRAINT fk_subject_learningactivities FOREIGN KEY (idsubject) REFERENCES tbl_subject (idsubject) MATCH FULL ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT pk_learmingactivities PRIMARY KEY (idclass,idteacher,idsubject)
);

show tables;
select * from db_rtitest.tbl_teacher;
select * from db_rtitest.tbl_subject;
select * from db_rtitest.tbl_class;
select * from db_rtitest.tbl_learningactivities;

INSERT INTO tbl_teacher (idteacher, fullname, qualification)
	values
    (1,'Назарова М. И.','Русский язык'),
    (2,'Стрелкова Е. Н.','Математика'),
    (3,'Robertson B.','English lang.'),
    (4,'Мухин А. С.','Истроия');
    
INSERT INTO tbl_subject (idsubject, name)
	values
    (1,'Алгебра'),
    (2,'Русский язык'),
    (3,'Литература'),
    (4,'English lang.'),
    (5,'Истроия'),
    (6,'Геометрия');
    
INSERT INTO tbl_class (idclass, name)
	values
    (1,'10А'),
    (2,'9Б'),
    (3,'11-А'),
    (4,'10В');
    
INSERT INTO tbl_learningactivities (idclass, idteacher, idsubject)
	values
    (1,4,5),
    (2,3,4),
    (1,2,1),
    (3,2,1),
    (3,2,6),
    (2,1,3),
    (1,1,2),
    (4,3,4),
    (3,1,2),
    (4,1,3),
    (1,2,6),
    (2,4,5);
    
    