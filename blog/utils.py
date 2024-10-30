import base64
from django.http import HttpResponse
from django.conf import settings

def basic_auth(func):
    def wrapper(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Basic "):
            return unauthorised_function()
        try:
            encoded_creds = auth_header.split(" ")[1]
            decoded_creds = base64.b64decode(encoded_creds).decode('utf-8')
            username, password = decoded_creds.split(":",1)
        except:
            return unauthorised_function()
        for i in settings.CREDENTIALS:
            if i[0] == username and i[1] == password:
                request.get_user_name = username
                return func(request, *args, **kwargs)
        else:
            return unauthorised_function()
    return wrapper
        
def unauthorised_function():
    response = HttpResponse("Unauthorized", status = 401)
    response["WWW-Authenticate"] = "Basic realm='Django'"
    return response