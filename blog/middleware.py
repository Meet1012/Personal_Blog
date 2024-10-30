import base64
from typing import Any
from django.http import HttpResponse
from django.conf import settings

class BasicAuthentication:
    def __init__(self, get_response) -> None:
        self.response = get_response
        
    def __call__(self, request) -> Any:
        if request.path.startswith('/protected/'):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Basic "):
                return self.unauthorized_response()
            try:
                encoded_creds = auth_header.split(" ")[1]
                decoded_creds = base64.b64decode(encoded_creds).decode('utf-8')
                username, password = decoded_creds.split(":", 1)
            except Exception as e:
                return self.unauthorized_response()
            if settings.BASIC_USERNAME == username and settings.BASIC_PASSWORD == password:
                return self.response(request)
            else:
                return self.unauthorized_response()
        return self.response(request)
            
    def unauthorized_response(self):
        response = HttpResponse("Unauthorized", status=401)
        response['WWW-Authenticate'] = 'Basic realm="Django"'
        return response