# py_elasticsearch

#pip freeze > requirements.txt
#pip install -r requirements.txt


#1
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

#2 mysql 설치 (https://goddaehee.tistory.com/277)
1. pymysql 라이브러리 이용 mysql db생성 (mysqlControl.py)
2. python manage.py migrate


#migrations
-모델 변경내역 히스토리 관리
-모델의 변경내역을 DB Schema (데이터베이스 데이터 구조)로 반영시키는 효율적인 방법을 제공
-migration 옵션을 끌수도 있다.

#model
파이썬(python)의 장고(django)로 서버사이드를 개발해보려고 합니다. 
이 블로그 포스트에서는 장고(django) 명령어를 새로운 어플리케이션을 생성하고
, 그 어플리케이션에서 사용할 데이터를 저장하기 위해 모델(models)를 생성하고 사용하는 방법에 대해서 알아보려고 합니다.
#모델 추가 설명 (https://tutorial.djangogirls.org/ko/django_models/)

#블로그 app 생성
1. python manage.py startapp blog

|-- blog
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- manage.py
   
admin.py: 장고(django)에서 기본적으로 제공하는 관리화면 설정
apps.py: 어플리케이션 메인 파일
models.py: 어플리케이션의 모델(models) 파일
tests.py: 테스트 파일
views.py: 어플리케이션의 뷰(views) 파일


#이 밖에도 아래와 같이 장고(django)에서 사용하는 파일들이 있습니다.
urls.py: 어플리케이션의 url 관리
forms.py: 입력 폼 관리
behaviors.py: 모델 믹스인 위치에 대한 옵션
constants.py: 어플리케이션 상수 관리
decorators.py: 데코레이터 관리
factories.py: 테스트 데이터 팩토리 파일
helpers.py: 뷰(views)와 모델(models)을 도와주는 함수 관리
managers.py: 커스텀 모델 매니저 파일
signals.py: 커스텀 시그널 관리
viewmixins.py: 뷰(views) 믹스인 관리

#blog/models.py
Post는 author, title, content, created_at, updated_at, published_at 필드를 가지고 있습니다.
author는 ForeignKey 함수를 사용하여, 장고(django)에서 기본적으로 제공하는 auth 어플리케이션의 User 모델을 참조하게 만들었습니다.(auth.User: 앱이름.모델)
title은 블로그의 제목으로 CharField 함수를 사용하여 길이가 정해진 문자열을 저장하도록 하였습니다. max_length 옵션을 사용해 길이가 100인 문자열을 저장하도록 설정하였습니다.
content는 블로그의 내용으로 TextField 함수를 통해 길이가 정해져있지 않는 문자열을 저장할 수 있도록 하였습니다
created_at은 블로그 생성 날짜로 DateTimeField을 통해 날짜와 시간을 저장할 수 있도록 하였으며, auto_now_add 옵션을 사용하여 데이터 생성시 현재 시간을 저장하도록 하였습니다.
updated_at는 블로그 수정일로 역시 DateTimeField을 통해 날짜와 시간을 저장할 수 있도록 하였으며, auto_now 옵션을 사용하여 데이터가 갱신될 때 현재 시간을 저장하도록 하였습니다.
published_at는 블로그를 공개한 날짜로 역시 DateTimeField을 통해 날짜와 시간을 저장할 수 있도록 하였습니다.
위에서는 설명하지 않은 blank = True, null = True는 별도로 설명하려고 합니다.

blank: 유효성(validation) 처리와 관련이 있는 옵션으로, form.is_valid()를 사용하여 입력폼의 유효성 검사를 할때 사용됩니다. 데이터의 공백(blank)을 허용합니다.
null: 데이터베이스와 관련이 있는 옵션으로, 데이터베이스의 null을 저장할 수 있도록 하는 옵션(nullable)
이 모델에는 publish, __str__ 함수를 가지고 있습니다.

publish: 블로그 서비스에서 자주 사용되는 기능인 공개(publish) 기능을 함수로 만들었습니다. 이 함수를 통해 블로그를 공개(publish)할 때 날짜를 갱신하기 위해 만들었습니다.
__str__: 표준 파이썬 클래스 메소드이며 사람이 읽을 수 있는 문자열을 반환하도록 합니다.

python manage.py makemigrations blog
우선 아래에 장고(django) 명령어로 우리가 만든 모델(models)로부터 데이터베이스(database)의 테이블을 생성하기 위한 마이그레이션(migration) 파일을 생성합니다

#마이그레이션(Migration)이란?
장고 공식 문서에서는 마이그레이션이 모델의 변경 내역을 DB *스키마에 적용시키는 장고의 방법이라고 설명하고 있습니다.

장고는 ORM을 사용하기 때문에 models.py와 클래스를 통해 DB 스키마를 생성하고 컨트롤 하게 되는데, 이 때 DB 스키마를 git처럼 버전으로 나눠서 관리 할 수 있게 해 주는 시스템이라 생각하시면 됩니다.

즉 하나의 마이그레이션 파일은 해당 마이그레이션이 생성된 시점의 모델의 구조(DB의 스키마)를 담고 있습니다.

*스키마(Schema)란? : DB 내에서 데이터가 저장되는 구조와 제약 조건을 정의한 것. 장고로 치면 하나의 어플리케이션의 models.py 파일이라고 할 수 있습니다.

아래에 장고(django) 명령어로 모델(models)로부터 생성한 마이그레이션(migration) 파일을 이용하여 데이터베이스의 테이블을 생성합니다.
python manage.py migrate blog

이것으로 장고(django)에서 모델(models)을 생성하고 생성한 모델(models)을 활용하여 DB 테이블을 생성하는 방법을 알아보았습니다. 이로써 개발에 필요한 정보를 저장할 수 있게 되었습니다. 이제 서비스에 필요한 DB를 설계하고 그에 따른 모델(models)과 마이그레이션(migration)을 생성하여 DB 테이블을 생성해 봅시다!

#슈퍼 유저 생성
python manage.py createsuperuser

#python manage.py runserver
http://127.0.0.1:8000/admin

#모델 등록
blog/admin.py 

#라우팅 
TCP/IP 라우팅 (https://www.ibm.com/docs/ko/aix/7.1?topic=protocol-tcpip-routing)
라우트는 인터넷 네트워크를 통해 다른 네트워크의 주소로 패킷을 전송하는 경로를 정의합니다.

라우트는 전체 경로를 정의하는 것이 아니라, 패킷을 대상에 전달할 수 있는 한 호스트에서 게이트웨이로(또는 한 게이트웨이에서 다른 게이트웨이로)의 경로 세그먼트만을 정의합니다. 라우트 유형은 5개입니다.

#django_exercise/urls.py
#blog/posts.html 생성 
#blog/urls.py 생성
#blog/templates/blog/posts.html ?왜 두개?


#ORM
ORM(Object-Relation Mapping)란, 객체(Object)와 관계형 데이터베이스(Relational)을 연결(Mapping)해 주는 것을 의미한다. 간단하게 설명하면 데이터베이스의 테이블을 객체(Object)와 연결하여 테이블에 CRUD를 할 때, SQL 쿼리를 사용하지 않고도, 가능하게 하는 것을 말합니다

from .models import Post: 우리가 만든 Post 모델(Models)을 불러옵니다.
posts = Post.objects.filter(published_at__isnull=False).order_by('-published_at')
published_at__isnull=False: published_at 필드가 null이 아닌 경우(__isnull=False)에 데이터를 가져옵니다
order_by('-published_at'): 데이터를 published_at 필드로 내림차순 정렬합니다.
return render(request, 'blog/posts.html', {'posts': posts}): 가져온 데이터를 blog/posts.html 페이지에 {'posts': posts} posts란 변수명으로 전달합니다.
