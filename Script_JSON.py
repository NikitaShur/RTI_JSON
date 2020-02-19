# coding: utf-8
import sqlalchemy
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dbsql import TblClass, TblLearningactivity, TblSubject, TblTeacher

import json
import argparse


def mysql_connect(user, password, host, port, database):

    mysql_url = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(user, password, host, port, database)
    mysql_engine = sqlalchemy.create_engine(mysql_url)

    return mysql_engine


def row_query(engine, teacher_id = None):

    existing_tables = engine.execute('show tables;')
    tables_list = [tbl[0] for tbl in existing_tables]
    tables_list.sort()
    
    query_class = engine.execute('select * from {}'.format(tables_list[0]))
    query_class_json = json.dumps([{'idclass': row[0], 'nameclass': row[1]} for row in query_class], indent=4, ensure_ascii=False)

    query_teacher = engine.execute('select * from {}'.format(tables_list[3]))
    query_teacher_json = json.dumps([{'idteacher': row[0], 'nameteacher': row[1], 'qualification': row[2]} for row in query_teacher], indent=4, ensure_ascii=False)

    if(teacher_id is None):
        query_tcs_json = None
    else:           
        teacher_count = mysql_engine.execute('select count(*) from {}'.format(tables_list[3])).scalar()
        if(teacher_id > teacher_count):
            print('The MAX value of teacher_id is: {}'.format(teacher_count))
            return

        query_tcs = engine.execute('select la.idteacher, t.fullname, la.idclass, c.name, la.idsubject, s.name from {} as la inner join {} as t on t.idteacher = la.idteacher inner join {} as c on c.idclass = la.idclass inner join {} as s on s.idsubject = la.idsubject where t.idteacher = {} order by la.idteacher, la.idclass, la.idsubject;'.format(tables_list[1], tables_list[3], tables_list[0], tables_list[2], teacher_id))
        
        query_tcs_dict = {}
        i = 0
        for row in query_tcs:
            dict_temp = {'idteacher':row[0], 'fullname': row[1], 'class_'+str(1+i): {'idclass': row[2], 'name':  row[3], 'subject': {'idsubject':  row[4], 'name':  row[5]}}}
            query_tcs_dict.update(dict_temp)
            i += 1

        query_tcs_json = json.dumps(query_tcs_dict, indent=6, ensure_ascii=False)

    return query_class_json, query_teacher_json, query_tcs_json


def models(engine, teacher_id = None):
   
    Session = sessionmaker(bind=engine)
    session = Session()

    first_query = session.query(TblClass).all()
    first_query_json = json.dumps([{'idclass': row.idclass, 'nameclass': row.name} for row in first_query], indent=4, ensure_ascii=False)

    second_query = session.query(TblTeacher).all()
    second_query_json = json.dumps([{'idteacher': row.idteacher, 'fullname': row.fullname, 'qualification': row.qualification} for row in second_query], indent=4, ensure_ascii=False)

    if(teacher_id is None):
        third_query_json = None
    else:
        teacher_count = session.query(TblTeacher).count()
        if(teacher_id > teacher_count):
            print('The MAX value of teacher_id is: {}'.format(teacher_count))
            return

        third_query = session.query(TblLearningactivity.idteacher.label('idteacher'), TblLearningactivity.idclass.label('idclass'), TblLearningactivity.idsubject.label('idsubject'), TblClass.name.label('classname'), TblTeacher.fullname.label('fullname'), TblSubject.name.label('subjectname')).join(TblTeacher).join(TblClass).join(TblSubject).filter(TblLearningactivity.idteacher.__eq__(teacher_id)).order_by(TblLearningactivity.idteacher, TblLearningactivity.idclass, TblLearningactivity.idsubject).all()
        
        third_query_dict = {'idteacher':third_query[0].idteacher, 'fullname': third_query[0].fullname}
        for i in range(len(third_query)):
            dict_temp = {'class_'+str(1+i): {'idclass': third_query[i].idclass, 'name':  third_query[i].classname, 'subject': {'idsubject':  third_query[i].idsubject, 'name':  third_query[i].subjectname}}}
            third_query_dict.update(dict_temp)
        
        third_query_json = json.dumps(third_query_dict, indent=6, ensure_ascii=False)

    return first_query_json, second_query_json, third_query_json



if __name__ == "__main__":

    input_params = argparse.ArgumentParser(description='', formatter_class=argparse.RawTextHelpFormatter)

    input_params.add_argument('-m', '--mode', dest = 'mode', choices=['rowsql', 'models'], required=True, help="Mode parameter:\n(rowsql - queries by rowSQL 'select');\n(models - queries by Models).")
    input_params.add_argument('-q', '--query', dest = 'query', choices=['class', 'teacher', 'tcs', 'all'], required=True, help='Which query you need:\n(class - list of classes);\n(teacher - list of teachers);\n(tcs - list of classes and subjects by teacher_id);\n(all - all lists).')
    input_params.add_argument('-t_id', '--teacher_id', dest='teacher_id', default=None, required=False, type=int, help='Teacher ID for third and fourth query.')   

    args = input_params.parse_args()

    if((args.query == 'tcs' or args.query == 'all') and (args.teacher_id is None)):
        print('Set teacher_id with terminal argument "-t_id"')
        raise SystemExit()  

    mysql_user = 'root'
    mysql_password = '1999'
    mysql_host = 'localhost'
    mysql_port = '3306'
    mysql_database = 'db_rtitest'


    mysql_engine = mysql_connect(mysql_user, mysql_password, mysql_host, mysql_port, mysql_database)

    if(args.mode == 'rowsql'):

        try:
            json_class, json_teacher, json_tcs = row_query(mysql_engine, args.teacher_id)
        except Exception as exp:
            print(exp)
            raise SystemExit()

        if(args.query == 'class'):
            print(json_class)
        elif(args.query == 'teacher'):
            print(json_teacher)
        elif(args.query == 'tcs'):
            print(json_tcs)
        else:
            print(json_class, '\n'*5)
            print(json_teacher, '\n'*5) 
            print(json_tcs)
    
    elif(args.mode == 'models'):

        try:
            json_class, json_teacher, json_tcs = models(mysql_engine, args.teacher_id)
        except Exception as exp:
            print(exp)
            raise SystemExit()

        if(args.query == 'class'):
            print(json_class)
        elif(args.query == 'teacher'):
            print(json_teacher)
        elif(args.query == 'tcs'):
            print(json_tcs)
        else:
            print(json_class, '\n'*5)
            print(json_teacher, '\n'*5) 
            print(json_tcs)  
    
