# coding: utf-8
import sqlalchemy
from dbsql import TblClass, TblLearningactivity, TblSubject, TblTeacher
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base



def mysql_connect(user, password, host, port, database):

    mysql_url = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user, password, host, port, database)
    mysql_engine = sqlalchemy.create_engine(mysql_url)

    return mysql_engine


def row_query(engine, teacher_id = None):

    if(teacher_id is None):
        print('Set teacher_id with terminal argument "-t_id"')
        return

    existing_tables = engine.execute('show tables;')
    tables_list = [tbl[0] for tbl in existing_tables]
    tables_list.sort()

    print('\n------FIRST Query------\n')

    query_class = engine.execute('select * from {}'.format(tables_list[0]))
    [print('idclass: {} nameclass: {}'.format(row[0], row[1])) for row in query_class]

    print('\n------SECOND Query------\n')

    query_teacher = engine.execute('select * from {}'.format(tables_list[3]))
    [print('idteacher: {} nameteacher: {} qualification {}'.format(row[0], row[1], row[2])) for row in query_teacher]

    print('\n------THIRD Query------\n')

    query_tcs = engine.execute('select la.idteacher, t.fullname, la.idclass, c.name, la.idsubject, s.name from {} as la inner join {} as t on t.idteacher = la.idteacher inner join {} as c on c.idclass = la.idclass inner join {} as s on s.idsubject = la.idsubject where t.idteacher = {} order by la.idteacher, la.idclass, la.idsubject;'.format(tables_list[1], tables_list[3], tables_list[0], tables_list[2], teacher_id))
    [print('idteacher: {} nameteacher: {} idclass: {} nameclass: {} idsubject: {} namesubject: {}'.format(row[0], row[1], row[2], row[3], row[4], row[5])) for row in query_tcs] 



def models(engine, teacher_id = None):

    if(teacher_id is None):
        print('Set teacher_id with terminal argument "-t_id"')
        return
    
    Session = sessionmaker(bind=engine)
    session = Session()

    print('\n------FIRST Query------\n')

    first_query = session.query(TblClass).all()
    [print('idclass: {} nameclass: {}'.format(row.idclass, row.name)) for row in first_query]

    print('\n------SECOND Query------\n')

    second_query = session.query(TblTeacher).all()
    [print('idteacher: {} nameteacher: {} qualification {}'.format(row.idteacher, row.fullname, row.qualification)) for row in second_query]

    print('\n------THIRD Query------\n')

    third_query = session.query(TblLearningactivity.idteacher.label('idteacher'), TblLearningactivity.idteacher.label('idclass'), TblLearningactivity.idteacher.label('idsubject'), TblClass.name.label('classname'), TblTeacher.fullname.label('fullname'), TblSubject.name.label('subjectname')).join(TblTeacher).join(TblClass).join(TblSubject).filter(TblLearningactivity.idteacher.__eq__(teacher_id)).order_by(TblLearningactivity.idteacher, TblLearningactivity.idclass, TblLearningactivity.idsubject)
    [print('idteacher: {} nameteacher: {} idclass: {} nameclass: {} idsubject: {} namesubject: {}'.format(row.idteacher, row.fullname, row.idclass, row.classname, row.idsubject, row.subjectname)) for row in third_query]





# third_query = session.query(TblLearningactivity, TblClass, TblTeacher, TblSubject).join(TblTeacher).join(TblClass).join(TblSubject).filter(TblLearningactivity.idteacher.__eq__(teacher_id)).order_by(TblLearningactivity.idteacher, TblLearningactivity.idclass, TblLearningactivity.idsubject).all()
# [print('idteacher: {} nameteacher: {} idclass: {} nameclass: {} idsubject: {} namesubject: {}'.format(row.tbl_learningactivities_idteacher, row.tbl_teacher_fullname, row.tbl_learningactivities_idclass, row.tbl_class_name, row.tbl_learningactivities_idsubject, row.tbl_subject_name)) for row in third_query]

if __name__ == "__main__":

    mysql_user = 'root'
    mysql_password = '1999'
    mysql_host = 'localhost'
    mysql_port = '3306'
    mysql_database = 'db_rtitest'

    mysql_engine = mysql_connect(mysql_user, mysql_password, mysql_host, mysql_port, mysql_database)

    models(mysql_engine, 3)
    row_query(mysql_engine, 3)



# ##########################################################################

# Base = declarative_base(mysql_engine)
# metadata = MetaData(bind=mysql_engine)

# session = sqlalchemy.orm.create_session(bind=mysql_engine)

# class Class(base):
#     __table__= sqlalchemy.Table('tbl_class',metadata,autoload=True)

# class Techer(base):
#     __table__ = sqlalchemy.Table('tbl_teacher',metadata,autoload=True)

# class_list = session.query(Class).all()

# for res in class_list:
#     print(res.title)
#     print('{} - {}'.format(res.idclass, res.name))


# existing_databases = mysql_engine.execute("show databases;")
# # Results are a list of single item tuples, so unpack each tuple
# existing_databases = [d[0] for d in existing_databases]

# for database in existing_databases:
#     print('Database: {}'.format(database))


# print(mysql_engine.table_names())

# existing_tables = mysql_engine.execute("show tables;")
# # Results are a list of single item tuples, so unpack each tuple
# existing_tables = [d[0] for d in existing_tables]

# [print('Table: {}'.format(tbl)) for tbl in existing_tables]
# print('\n{}'.format(existing_tables[1]))

# select_tbl1 = mysql_engine.execute("select * from {} where idclass >= 3".format(existing_tables[0]))
# print(select_tbl1.keys())
# for t in select_tbl1:
#     print(str(t) + ' KEK')
