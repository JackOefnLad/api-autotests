from clients.authentication.authentification_schema import TokenSchema

print(TokenSchema.model_json_schema())

schema = {
    {'properties': {'tokenType': {'title': 'Tokentype', 'type': 'string'},
    'accessToken': {'title': 'Accesstoken', 'type': 'string'},
    'refreshToken': {'title': 'Refreshtoken', 'type': 'string'}},
    'required': ['tokenType', 'accessToken', 'refreshToken'],
    'title': 'TokenSchema', 'type': 'object'
    }
}