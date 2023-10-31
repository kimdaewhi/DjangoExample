from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random

# 동적 Web Application을 활용한 예제    
# 위에서 선언한 topics 리스트를 가지고 list 및 a태그를 만들어준다.

nextID = 4
topics = [
        { "id": 1, "title": "routing", "body" : "Routing is..." },
        { "id": 2, "title": "view", "body" : "View is..." },
        { "id": 3, "title": "model", "body" : "Model is..." },
    ]

def HTMLTemplate(articleTag, id=None): 
    global topics
    contextUI = ''
    
    # ID가 있을 때만 delete 버튼 visible
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
        '''
    
    # topics 리스트 개수만큼 li 태그 생성
    ul = ''
    for topic in topics:
        ul += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
        
    return f'''
        <html>
            <body>
                <h1><a href="/">Django</a></h1>
                <ul>
                    {ul}
                </ul>
                {articleTag}
                
                <ul>
                    <li><a href="/create/">Create</a></li>
                    {contextUI}
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
    global nextID
    # post 방식으로 처리
    if request.method == "GET":
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title" autocomplete="off"></p>
                <p><textarea name="body" placeholder="body" autocomplete="off"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    
    elif request.method == "POST":
        # POST로 받아온 데이터를 topic 리스트에 추가
        title = request.POST["title"]
        body = request.POST["body"]
        newTopic = { "id": nextID, "title": title, "body": body }
        topics.append(newTopic)
        
        # nextID를 만들어주기 전에 새로 추가한 nextID 기반의 read url 생성, 이후에 nextID 변경
        url = '/read/' + str(nextID)
        nextID += 1
        
        # redirect 처리
        return redirect(url)



def read(request, id):
    id = int(id)
    
    # topics 리스트에서 id값이 일치하는 요소 검색(컴프리헨션 표현식)
    selTopic = next((t for t in topics if t['id'] == id), None)
    
    if selTopic:
        title = selTopic["title"]
        body = selTopic["body"]
    else:
        title = 'Topic Not Found'
        body = 'The requested topic was not found.'
        
    article = f'''
            <p><h3>{title}</h3></p>
            <p>{body}</p>
        '''
    return HttpResponse(HTMLTemplate(article, id))


def update(request): 
    
    return HttpResponse('update')

@csrf_exempt
def delete(request):
    global topics
    
    # delete는 기존 데이터를 삭제 요청을 통해 '서버 데이터를 변경하는 것'이기 때문에 get방식이 아닌 post방식을 활용해야 함.
    if request.method == 'POST':
        id = request.POST["id"]
        newTopics = []
        for topic in topics:
            if topic["id"] != int(id):
                newTopics.append(topic)
        
        topics = newTopics
    
    return redirect('/')