from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict
from clients.users.user_schema import UserSchema, CreateUserSchema, UpdateUserRequestSchema



class privateUsersClient(APIClient):
    def get_user_me_api(self) -> Response:
        return self.get("api/v1/users/me")
    
    def get_user_id_api(self, user_id: str) -> Response:
        return self.get(f"api/v1/users/{user_id}")
    
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        response = self.update_user_api(request)
        # return self.patch(f"api/v1/users/{user_id}", json=request)
        return UpdateUserRequestSchema.model_validate_json(response.text)
     
    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"api/v1/users/{user_id}")