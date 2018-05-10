import MySQLdb

db = MySQLdb.connect('localhost', 'root', '123456',"TESTDB")
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Yuhan', 20, 'M', 22000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in Case1 there is any error
   db.rollback()


db.close()

print ('hello')