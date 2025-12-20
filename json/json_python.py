import json

json_data = '{"name": "Иван","age": 30,"is_student": false,"courses": ["Python", "QA Automation", "API Testing"],"address": {"city": "Москва","zip": "101000"}}'
parsed_data=json.loads(json_data)

#print(parsed_data['courses']) #,parsed_data['address']



data = {"name": "Fella","age": 20,"is_student": True}
json_string = json.dumps(data, indent=4)

# print(json_string)

# Чтение json из файла в словарь
# with open("json_example.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     print(data)

# Записать словарь в json
with open ("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)