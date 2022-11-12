import json
import random
import string
from typing import *
import config
import mimetypes
from framework import HTTPServer, HTTPRequest, HTTPResponse
from framework import HTTPHeader
import os


def random_string(length=20):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def default_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 404, 'Not Found'
    print(f"calling default handler for url {request.request_target}")


def task2_data_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 2: Serve static content based on request URL (20%)
    type = request.method
    request.request_target = request.request_target[1:]
    if type == 'GET':
        try:
            f = open(request.request_target, 'rb')
            response.status_code, response.reason = 200, 'OK'
            response.headers.append(HTTPHeader('Content-Length', str(os.path.getsize(request.request_target))))
            response.headers.append(
                HTTPHeader('Content-Type', mimetypes.MimeTypes().guess_type(request.request_target)[0]))
            response.body = f.read()
            f.close()
        except FileNotFoundError:
            response.status_code, response.reason = 404, 'Not Found'
    if type == 'HEAD':
        try:
            f = open(request.request_target, 'rb')
            response.status_code, response.reason = 200, 'OK'
            response.headers.append(HTTPHeader('Content-Length', str(os.path.getsize(request.request_target))))
            response.headers.append(
                HTTPHeader('Content-Type', mimetypes.MimeTypes().guess_type(request.request_target)[0]))
            f.close()
        except FileNotFoundError:
            response.status_code, response.reason = 404, 'Not Found'


def task3_json_handler(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 3: Handle POST Request (20%)
    response.status_code, response.reason = 200, 'OK'
    if request.method == 'POST':
        binary_data = request.read_message_body()
        obj = json.loads(binary_data)
        # TODO: Task 3: Store data when POST
        for i in request.headers:
            if i[0] == 'Content-Length':
                server.task3_length = i[1]
            if i[0] == 'Content-Type':
                server.task3_type = i[1]
        server.task3_data = obj['data']
        print(server.task3_data)
    else:
        obj = {'data': server.task3_data}
        return_binary = json.dumps(obj).encode()
        response.headers.append(HTTPHeader('Content-Length', server.task3_length))
        response.headers.append(HTTPHeader('Content-Type', server.task3_type))
        if request.method == 'GET':
            response.body = return_binary


def task4_url_redirection(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 4: HTTP 301 & 302: URL Redirection (10%)
    type = request.method
    request.request_target = request.request_target[1:]
    if (type == 'GET' or type == 'HEAD') and request.request_target == 'redirect':
        response.headers.append(HTTPHeader('Location', 'http://127.0.0.1:8080/data/index.html'))
        response.status_code, response.reason = 302, 'Found'


def task5_test_html(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    response.status_code, response.reason = 200, 'OK'
    with open("task5.html", "rb") as f:
        response.body = f.read()


def task5_cookie_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        response.headers.append(HTTPHeader('Set-Cookie', 'Authenticated=yes'))
        response.status_code, response.reason = 200, 'OK'
    else:
        response.status_code, response.reason = 403, 'Forbidden'


def task5_cookie_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    flag = False
    for i in request.headers:
        if i[0] == 'Cookie':
            if i[1].split("=")[1] == 'yes':
                flag = True
                break
    if not flag:
        response.status_code, response.reason = 403, 'Forbidden'
    else:
        response.status_code, response.reason = 200, 'OK'
        with open('data/test.jpg', 'rb') as f:
            response.headers.append(HTTPHeader('Content-Length', str(os.path.getsize('data/test.jpg'))))
            response.headers.append(
                HTTPHeader('Content-Type', mimetypes.MimeTypes().guess_type('data/test.jpg')[0]))
            response.body = f.read()
            request.buffer = response.body


def task5_session_login(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 1 Login Authorization
    obj = json.loads(request.read_message_body())
    if obj["username"] == 'admin' and obj['password'] == 'admin':
        session_key = random_string()
        while session_key in server.session:
            session_key = random_string()
        server.session[session_key] = ''
        session_key = 'SESSION_KEY=' + session_key
        response.headers.append(HTTPHeader('Set-Cookie', session_key))
        response.status_code, response.reason = 200, 'OK'
    else:
        response.status_code, response.reason = 403, 'Forbidden'


def task5_session_getimage(server: HTTPServer, request: HTTPRequest, response: HTTPResponse):
    # TODO: Task 5: Cookie, Step 2 Access Protected Resources
    flag = False
    for i in request.headers:
        if i[0] == 'Cookie':
            s = i[1].split('=')[1]
            if server.session.get(s) is not None:
                flag = True
                break
    if not flag:
        response.status_code, response.reason = 403, 'Forbidden'
    else:
        response.status_code, response.reason = 200, 'OK'
        with open('data/test.jpg', 'rb') as f:
            response.headers.append(HTTPHeader('Content-Length', str(os.path.getsize('data/test.jpg'))))
            response.headers.append(
                HTTPHeader('Content-Type', mimetypes.MimeTypes().guess_type('data/test.jpg')[0]))
            response.body = f.read()
            request.buffer = response.body


# TODO: Change this to your student ID, otherwise you may lost all of your points
YOUR_STUDENT_ID = 12011904

http_server = HTTPServer(config.LISTEN_PORT)
http_server.register_handler("/", default_handler)
# Register your handler here!
http_server.register_handler("/data", task2_data_handler, allowed_methods=['GET', 'HEAD'])
http_server.register_handler("/post", task3_json_handler, allowed_methods=['GET', 'HEAD', 'POST'])
http_server.register_handler("/redirect", task4_url_redirection, allowed_methods=['GET', 'HEAD'])
# Task 5: Cookie
http_server.register_handler("/api/login", task5_cookie_login, allowed_methods=['POST'])
http_server.register_handler("/api/getimage", task5_cookie_getimage, allowed_methods=['GET', 'HEAD'])
# Task 5: Session
http_server.register_handler("/apiv2/login", task5_session_login, allowed_methods=['POST'])
http_server.register_handler("/apiv2/getimage", task5_session_getimage, allowed_methods=['GET', 'HEAD'])

# Only for browser test
http_server.register_handler("/api/test", task5_test_html, allowed_methods=['GET'])
http_server.register_handler("/apiv2/test", task5_test_html, allowed_methods=['GET'])


def start_server():
    try:
        http_server.run()
    except Exception as e:
        http_server.listen_socket.close()
        print(e)


if __name__ == '__main__':
    start_server()
