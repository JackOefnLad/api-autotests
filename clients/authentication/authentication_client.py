from clients.api_client import APIClient 
#папка -> файл -> класс
from httpx import Response
from typing import TypedDict

from clients.authentication.authentification_schema import LoginRequestSchema, LoginResponseSchema, RefreshTokenSchema

class LoginRequestDict(TypedDict):
    email: str
    password: str
class RefreshRequestDict(TypedDict):
    refreshToken: str

class AuthenticationClient(APIClient):
    def login_api(self, request: LoginRequestSchema)-> Response:
        #return self.post("/api/v1/authentication/login", json=request)
        response = self.login_api(request)
        return LoginRequestSchema.model_validate_json(response.text)
    def refresh_api(self,request: RefreshTokenSchema):
        return self.post("/api/v1/authentication/refresh", json = request)
# client = AuthenticationClient()
# client.login_api({'email':'', 'password':''})
