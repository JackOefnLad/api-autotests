# {
#   "course": {
#     "id": "string",
#     "title": "string",
#     "maxScore": 0,
#     "minScore": 0,
#     "description": "string",
#     "previewFile": {
#       "id": "string",
#       "filename": "string",
#       "directory": "string",
#       "url": "https://example.com/"
#     },
#     "estimatedTime": "string",
#     "createdByUser": {
#       "id": "string",
#       "email": "user@example.com",
#       "lastName": "string",
#       "firstName": "string",
#       "middleName": "string"
#     }
#   }
# }

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
import uuid

# from pydantic.alias_generators import to_camel

class FileSchema(BaseModel):
    id: str
    filename: str
    url: HttpUrl
    directory: str

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias = "lastName")
    first_name: str = Field(alias = "firstName")
    middle_name: str = Field(alias = "middleName")

    @computed_field
    def username(self)-> str:
        return f"{self.first_name} {self.last_name}"


    def get_username(self)-> str:
        return f"{self.first_name} {self.last_name}"
    # Для динамического формирования строки 

class CourseSchema(BaseModel):
    # model_config = ConfigDict(alias_generator=to_camel, populated_by_name = True)
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))    
    title: str = "test title"
    max_score: int = Field(alias = "maxScore", default=1000)
    min_score: int = Field(alias = "minScore", default=1)
    description: str = "test field"
    preview_file: FileSchema = Field(alias = 'previewFile') 
    estimated_time: str = Field(alias = "estimatedTime", default = 'Day')
    created_by_user: UserSchema = Field(alias = 'createdByUser')

course_default_model = CourseSchema(
    id = "course-id",
    title = "Playwright course",
    maxScore = 10,
    minScore = 1,
    description = "Top",
    previewFile = FileSchema(
        id="file_id",
        filename = "test file",
        url = "test url",
        directory = "test dir",
    ),
    estimatedTime ="A week",
    createdByUser = UserSchema(
        id = "user id",
        email = "user email",
        lastName = "last test",
        firstName = "first name",
        middleName = "middle test",
    )
)
# print(course_default_model)

# course_dict = {
#     "id": "string",
#     "title": "string",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "bong",
#     "estimatedTime": "Year"
# }
# course_dict_model = CourseSchema(**course_dict)
# # print(course_dict_model)

# course_json = """
# {
#     "id": "string",
#     "title": "string",
#     "maxScore": 100,
#     "minScore": 10,
#     "description": "bong",
#     "estimatedTime": "Year"
# }
# """
# course_json_model = CourseSchema.model_validate_json(course_json)
# print(course_json_model)
# print(course_json_model.model_dump_json())


# course = CourseSchema()

# print("Course: ", course)

try:
    user = UserSchema(
        id = "user id",
            email = "user email",
            lastName = "last test",
            firstName = "first name",
            middleName = "middle test"
    )
# print(user.get_username(), user.username)
except ValidationError as error:
    print(error)
    print(error.errors())