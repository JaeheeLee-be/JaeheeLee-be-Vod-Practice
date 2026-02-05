from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This Main Page!"

# Alt + Shitf + 화살표 위/아래
@app.route('/about')
def about():
    return "Hello, This about Page!"

@app.route('/company')
def about():
    return "Hello, This company Page!"

# 동적으로 URL 파라미터 값을 받아서 처리해 준다.
@app.route('/user/<username>')
def user_profile(username):
    return f'Username : {username}'

@app.route('/number/<int:number>')
def number(number):
    return f'number : {number}'

# post 요청 날리는 법
# 1. postman
# 2. requests
import requests # pip install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    response = requests.post(usr=url , data=data)

    return response()

@app.route('/submit', methods={'GET', 'POST', 'PUT', 'DELETE'})
def submit():
    print(request.method)

    if request.method == 'GET':
        print("GET method")

    if request.method == 'POST':
        print("***POST method***", request.data)

    return Response("Successfully submitted", status=200)

if __name__ == "__main__":
    app.run(debeg=True)