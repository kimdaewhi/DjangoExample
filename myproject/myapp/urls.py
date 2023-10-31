from django.urls import path
from myapp import views

# http://127.0.0.1/
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1

# ⭐여기가 라우팅과 관련된 정보⭐
# '<>' 를 이용하면 url을 가변적으로 받을 수 있다.(read/1 read/2 ....)
urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/', views.update),
]
