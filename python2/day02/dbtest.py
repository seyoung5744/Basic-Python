"""
    pip install PyMySQL
"""
"""
    1. 커넥션 수립
    2. cursor 객체 생성
    3. cursor 객체로 sql 실행 ( 읽기 - select/ 쓰기 - insert, update, delete)
    4. sql이 읽기 작업이면 검색한 결과를 추가 작업
    5. 커넥션 닫기
"""
import pymysql
#1. 커넥션 수립
conn = pymysql.connect(host='localhost', user='pythonUser', password='won9975744!', db='pythonTest', charset='utf8')

# 변수 sql에 실행할 sql문 작성
sql = 'select * from test'

cursor = conn.cursor() # 사용할 커서 객체 생성

cursor.execute(sql) # sql 실행. 실행한 결과는 cursor 객체에 return됨.

for row in cursor: # 검색된 결과를 한 줄씩 추출
    print(row[0],'/',row[1],'/',row[2],'/',row[3])

conn.close()



# insert 테스트
name = 'ddd'
price = 2500
disc = 'poiu'

conn = pymysql.connect(host='localhost', user='pythonUser', password='won9975744!', db='pythonTest', charset='utf8')

sql = "insert into test(name, price, disc) values(%s, %s, %s)" # 자바의 ? == 파이썬 %s
cursor = conn.cursor() # 사용할 커서 객체 생성

d = (name, price, disc)

cursor.execute(sql, d) # sql 실행. 실행한 결과는 cursor 객체에 return됨.

# for row in cursor: # 검색된 결과를 한 줄씩 추출
#     print(row[0],'/',row[1],'/',row[2],'/',row[3])

conn.commit() # 쓰기 완료
conn.close()