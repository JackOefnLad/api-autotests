from pydantic import BaseModel, Field, ConfigDict

class UserSchema(BaseModel):
    model_config = ConfigDict(populated_by_name=True) # Настройка позволяет заполнять по alias и по базовому значению
    id: str
    email: str 
    last_name: str = Field(alias = 'lastName')
    first_name: str = Field(alias = 'firstName')
    middle_name: str = Field(alias = 'middleName')


class CreateUserSchema(BaseModel):
    model_config = ConfigDict(populated_by_name=True)

    email: str 
    password: str
    last_name: str = Field(alias = 'lastName')
    first_name: str = Field(alias = 'firstName')
    middle_name: str = Field(alias = 'middleName')

class UpdateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populated_by_name=True)

    email: str | None
    last_name: str | None = Field(alias = 'lastName')
    first_name: str | None = Field(alias = 'firstName')
    middle_name: str | None = Field(alias = 'middleName')

