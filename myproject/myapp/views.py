from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random

# 동적 Web Application을 활용한 예제    
# 위에서 선언한 topics 리스트를 가지고 list 및 a태그를 만들어준다.
    
topics = [
        { "id": 1, "title": "routing", "body" : "Routing is..." },
        { "id": 2, "title": "view", "body" : "View is..." },
        { "id": 3, "title": "model", "body" : "Model is..." },
    ]

def HTMLTemplate(articleTag): 
    global topics
    ul = ''
    for topic in topics:
        ul += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        
    return f'''
        <html>
            <body>
                <h1><a href="https://docs.djangoproject.com/ko/4.2/" target="_blank">Django</a></h1>
                <ul>
                    {ul}
                </ul>
                {articleTag}
                
                <ul>
                    <li><a href="/create/">Create</a></li>
                </ul>
            </body>
        </html>
    '''

# 첫 번째 파라미터로 요청(request) 정보를 전달 해야 함.
def index(request):     
    # 동적으로 리스트 출력
    article = '''
        <h2>Welcome</h2>
        Hello, Django!
    '''
    return HttpResponse(HTMLTemplate(article))


@csrf_exempt
def create(request):
    article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    return HttpResponse('<h1>Read ' + id + '</h1>')


