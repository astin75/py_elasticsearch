#장고 프로젝트 생성
django startproject xxx

#mysql DB
"CREATE DATABASE mse";
show databases;

#setting
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stu',  # DB name
        'USER': 'root',  # DB account
        'PASSWORD': '1q2w3e',  # DB account's password
        'HOST': '127.0.0.1',  # DB address(IP)
        'PORT': '3306',  # DB port(normally 3306)
    }
}

#migrate
python manage.py migrate

#app 생성
django-admin startapp members

#model (table 생성)
app/models/ class 

#admin 에 model 등록
admin.site.register(DBNAME)


#migrate
python manage.py migrate

#슈퍼 유저 생성
python manage.py createsuperuser


#runsserver
1. localhost/admin -> login
2. DB확인
-> 안돼있다면 migrate

#2 DB 조회-----------------

#views.py
app/views.py
-  model import 후 
- def memberList(request):
    member_List = memberData.objects.all()
    return render(request, 'member/memberList.html', {'member_List':member_List})
  render ( request, html, DB)

#url 생성 
app/url.py
urlpatterns = [
    path('', memberList, name='memberList'),
]
"http://localhost:8000/memList"

