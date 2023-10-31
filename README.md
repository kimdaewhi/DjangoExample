# Django 환경 세팅

**1. 가상환경 세팅**
  ```powershell
  python -m venv myenv
  ```
**2. 가상환경 활성화**
  ```powershell
  [가상환경경로]\Scripts\activate
  ```
**3. 가상환경 활성화 상태에서 Django 설치**
   ```powershell
   pip install django
   ```
**4. django 프로젝트 생성**
   ```
   django-admin startproject myapp
   ```
**5. django 프로젝트 실행**
   ```
   python manage.py runserver [PORT]
   // migration 에러 발생 시 다음 명령어 실행
   python manage.py migrate
   ``` 


## Django 각 스크립트 역할
- ### manage
  유틸리티


## Django 앱 만들기
* ✏️ **앱(App) 이란?** 

  Django 내에서 의미하는 하나의 기능 or 모듈의 단위.
  Django의 단위는 크게 프로젝트 단위위 애플리케이션 단위가 있다.

  하나의 App 안에는 **urls.py, model, view**라는 주요 스크립트 존재.
  
  python manage.py startapp [앱 이름] 명령어를 통해서 생성.
  
  [애플리케이션]을 생성하게 되면 
  ```
  /* ⭐⭐⭐urls.py⭐⭐⭐ */
    👉🏻 path에 따라 요청을 어떻게 처리? 누가 처리할지?(라우팅)
    
  /* ⭐⭐⭐model⭐⭐⭐ */
    👉🏻

  /* ⭐⭐⭐view⭐⭐⭐ */
    👉🏻 라우팅(urls.py)으로 등록된 애플리케이션의 view 함수를 통해 웹페이지 출력
  ```


## 라우팅?(라우팅이 반이다.)
* **'사용자가 접속한 각각의 경로를 누가 처리할 것인가'** 지정하는 작업
  ```
  1. 프로젝트 폴더 내의 urls.py가 가장 큰 틀의 라우팅 역할
  2. 각 app으로 위임
  3. app이 view 안에 있는 특정 함수로 위임
  4. 함수 작업 실행
  ```
* ⭐ `path('', include('myapp.urls'))`
  - param1 : 
  - param2 : include('[app의 이름.urls]') 또는 import한 view의 함수
* urls.py 복사, app에 붙여넣기


## Web Server와 Web Application의 차이.
* Web Server : 정적(static)
* Web Application : 동적(dynamic)


## CRUD


### ⚠️ csrf 에러란?
**Cross-site request forgery** 공격의 약자 (자세한건 알아서...)

해결법
```python
from django.views.decorators.csrf import csrf_exempt

# 전처리를 통해서 csrf 방식을 해제할 view 함수에 작성
@csrf_exempt
```
