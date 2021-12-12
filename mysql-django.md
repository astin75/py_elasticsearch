# py_elasticsearch

#pip freeze > requirements.txt
#pip install -r requirements.txt

|-- django_exercise
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py

각 파일은 아래와 같은 기능을 합니다.

django_exercise/settings.py: 전반적인 설정을 가지고 있는 파일
django_exercise/urls.py: 프로젝트의 url을 관리하는 파일
django_exercise/wsgi.py: 웹서버(apache, nginx등)과 연동하기 위한 파일
manage.py: 프로젝트를 관리. 예를 들어, DB의 migration 생성 및 실행, 로컬에서 다른 설치없이 웹 서버를 기동 등
설정


#migrations
-모델 변경내역 히스토리 관리
-모델의 변경내역을 DB Schema (데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공
-migration 옵션을 끌수도 있다.

# 마이그레이션 파일 생성
$ python manage.py makemigrations <app-name>

# 마이그레이션 적용
$ python manage.py migrate <app-name>

# 마이그레이션 적용 현황
$ python manage.py showmigrations <app-name>

# 지정 마이그레이션의 SQL 내역
 python manage.py sqlmigrate <app-name> <migration-name>