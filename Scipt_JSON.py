
import sqlalchemy

mysql_user = 'root'
mysql_password = '1999'
mysql_host = 'localhost'
mysql_port = '3306'
mysql_database = 'db_rtitest'

mysql_url = 'mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(mysql_user,mysql_password,mysql_host,mysql_port,mysql_database)
mysql_engine = sqlalchemy.create_engine(mysql_url)

# existing_databases = mysql_engine.execute("show databases;")
# # Results are a list of single item tuples, so unpack each tuple
# existing_databases = [d[0] for d in existing_databases]

# for database in existing_databases:
#     print('Database: {}'.format(database))


# print(mysql_engine.table_names())

existing_tables = mysql_engine.execute("show tables;")
# Results are a list of single item tuples, so unpack each tuple
existing_tables = [d[0] for d in existing_tables]

[print('Table: {}'.format(tbl)) for tbl in existing_tables]

select_tbl1 = mysql_engine.execute("select * from {} where idclass >= 3".format(existing_tables[0]))
print(select_tbl1.keys())
for t in select_tbl1:
    print(str(t) + ' KEK')
