
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


-- select la.idteacher, t.fullname, la.idclass, c.name, la.idsubject, s.name
-- 	from tbl_learningactivities as la
-- 		inner join tbl_teacher as t on t.idteacher = la.idteacher
--         inner join tbl_class as c on c.idclass = la.idclass
--         inner join tbl_subject as s on s.idsubject = la.idsubject
-- 			where t.idteacher = 1 or 2 or 3 or 4
-- 				order by la.idteacher, la.idclass, la.idsubject;
--                 
-- SELECT tbl_learningactivities.idclass , tbl_learningactivities.idteacher , tbl_learningactivities.idsubject
-- 	FROM tbl_learningactivities 
-- 		INNER JOIN tbl_teacher ON tbl_teacher.idteacher = tbl_learningactivities.idteacher 
-- 		INNER JOIN tbl_class ON tbl_class.idclass = tbl_learningactivities.idclass 
-- 		INNER JOIN tbl_subject ON tbl_subject.idsubject = tbl_learningactivities.idsubject
-- 			WHERE tbl_learningactivities.idteacher = 1 or 2 or 3 or 4
-- 				ORDER BY tbl_learningactivities.idteacher, tbl_learningactivities.idclass, tbl_learningactivities.idsubject;
--                 
-- SELECT tbl_learningactivities.idclass AS tbl_learningactivities_idclass, tbl_learningactivities.idteacher AS tbl_learningactivities_idteacher, tbl_learningactivities.idsubject AS tbl_learningactivities_idsubject, tbl_teacher.idteacher AS tbl_teacher_idteacher, tbl_teacher.fullname AS tbl_teacher_fullname, tbl_teacher.qualification AS tbl_teacher_qualification, tbl_subject.idsubject AS tbl_subject_idsubject, tbl_subject.name AS tbl_subject_name
-- 	FROM tbl_learningactivities 
--     INNER JOIN tbl_teacher ON tbl_teacher.idteacher = tbl_learningactivities.idteacher 
--     INNER JOIN tbl_class ON tbl_class.idclass = tbl_learningactivities.idclass 
--     INNER JOIN tbl_subject ON tbl_subject.idsubject = tbl_learningactivities.idsubject
-- 		WHERE tbl_learningactivities.idteacher = 1 or 2 or 3 or 4
-- 			ORDER BY tbl_learningactivities.idteacher, tbl_learningactivities.idclass, tbl_learningactivities.idsubject;