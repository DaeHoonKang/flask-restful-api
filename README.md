# flask-restful-api
Sample Flask-RESTful API 

## 개발 환경
```buildoutcfg
os  : mac
python : 3.6.8
ide : pycharm
db  : mongodb
test : windows, mac
```

## API 명세서
프로젝트의 Wiki페이지에 작성되어 있음

[API 명세서](https://github.com/DaeHoonKang/flask-restful-api/wiki/RESTful-API-%EB%AA%85%EC%84%B8%EC%84%9C)

## 설치
아래 순서와 같이 설치 하도록 함 
 - 파이썬 3.6.8 설치
 - MongoDB 설치
 - Git Clone
 - Install requirements.txt
 - 샘플 데이터 저장(to MongoDB)
 - run app
 
 ### 파이썬 3.6.8
 3.7x 버전을 사용하지 않은 이유는 MongoDB ORM 패키지인 mongoengine이 3.7x을 지원하지 않아서 3.6.8로 선택함
  
 [파이썬 다운로드](https://www.python.org/downloads/release/python-368/)
 or
 [pyenv](https://github.com/pyenv/pyenv)
 
 ### MongoDB 설치
 샘플 프로젝트로 개발된 버전이라 설치 시 MongoDB 보안 설정은 생략하도록 함
 
 윈도우즈의 경우 [MongoDB 다운로드](https://www.mongodb.com/download-center/community?jmp=nav) 페이지에서 다운 받아서 설치하면 됨
 Mac의 경우 brew 를 사용하면 됨
 
 ``` brew install mongodb```
 
 데이터베이스 저장할 폴더 만들기
 
 MongoDB 실행할 때 저장할 기본 폴더가 /data/db를 가리키므로 해당 폴더를 미리 만들어 준다
 
 ``` Mac > mkdir -p /data/db```
  
 ```Windows PowerShell > mkdir c:/data/db```
 
 기본 Host, Port는 127.0.0.1, 27017이다
 
 ### Git Clone
 ``` git clone https://github.com/DaeHoonKang/flask-restful-api```
 
 ### Requirements.txt
 ``` pip install -r requirements.txt```
 
 ### 샘플 데이터 저장
 ``` 
 $ python company2db.py
 Company rows: 110
 $ mongo
 MongoDB shell version v4.0.8
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("33179cfc-9835-4125-9382-a9736cda7bea") }
MongoDB server version: 4.0.8
Server has startup warnings:
2019-04-08T08:59:19.981+0900 I CONTROL  [initandlisten]
2019-04-08T08:59:19.982+0900 I CONTROL  [initandlisten] ** WARNING: Access control is not enabled for the database.
2019-04-08T08:59:19.984+0900 I CONTROL  [initandlisten] **          Read and write access to data and configuration is unrestricted.
2019-04-08T08:59:19.985+0900 I CONTROL  [initandlisten]
2019-04-08T08:59:19.990+0900 I CONTROL  [initandlisten] ** WARNING: This server is bound to localhost.
2019-04-08T08:59:19.991+0900 I CONTROL  [initandlisten] **          Remote systems will be unable to connect to this server.
2019-04-08T08:59:19.995+0900 I CONTROL  [initandlisten] **          Start the server with --bind_ip <address> to specify which IP
2019-04-08T08:59:19.997+0900 I CONTROL  [initandlisten] **          addresses it should serve responses from, or with --bind_ip_all to
2019-04-08T08:59:19.998+0900 I CONTROL  [initandlisten] **          bind to all interfaces. If this behavior is desired, start the
2019-04-08T08:59:20.004+0900 I CONTROL  [initandlisten] **          server with --bind_ip 127.0.0.1 to disable this warning.
2019-04-08T08:59:20.006+0900 I CONTROL  [initandlisten]
---
Enable MongoDB's free cloud-based monitoring service, which will then receive and display
metrics about your deployment (disk utilization, CPU, operation statistics, etc).

The monitoring data will be available on a MongoDB website with a unique URL accessible to you
and anyone you share the URL with. MongoDB may use this information to make product
improvements and to suggest MongoDB products and deployment options to you.

To enable free monitoring, run the following command: db.enableFreeMonitoring()
To permanently disable this reminder, run the following command: db.disableFreeMonitoring()

> show dbs
admin    0.000GB
company  0.000GB
config   0.000GB
local    0.000GB
> use company
switched to db company
> db.company.find().count()
110
> exit
bye
```
### Run
``` python run.py ```

