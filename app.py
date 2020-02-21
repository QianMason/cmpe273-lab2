from flask import Flask, escape, request

app = Flask(__name__)

stud = {
}


'''
class_id = {
    "0":"CMPE273"
}
class_list = {
    "CMPE273:[]
}
'''

class_id = {}
class_list = {}

sid = 0
cid = 0

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/students/', methods=['POST'])
def create_student():
    global sid
    ret_id = str(sid)
    sid += 1
    req = request.json
    stud[ret_id] = req["name"]
    return { "id":ret_id, "name":req["name"] }, 201

@app.route('/students/<id>', methods=['GET'])
def get_students(id=0):
    ret_id = str(id)
    return {"id":ret_id, "name":stud[ret_id]}, 201

@app.route('/classes/', methods=['POST'])
def create_class():
    global cid
    ret_id = str(cid)
    cid += 1
    req = request.json["name"]
    class_id[ret_id] = req
    class_list[req] = []
    return {"id":ret_id, "name":req, "students":[]}


@app.route('/classes/<id>', methods=['GET'])
def get_classes(id=0):
    ret_id = str(id)
    return {"id":ret_id, "name":class_id[ret_id], "students":class_list[class_id[ret_id]]}

@app.route('/classes/<id>', methods=['PATCH'])
def add_students(id=0):
    c_id = str(id) #called c_id for local variable
    s_id = str(request.json["student_id"])
    class_list[class_id[c_id]].append({"id":s_id, "name":stud[s_id]})
    return {"id":c_id, "name":class_id[c_id], "students":class_list[class_id[c_id]]}


# create student
# POST /students

# # Request
# {
#     "name": "Bob Smith"
# }

# # Response
# # HTTP Code: 201
# {
#     "id" : 1234456,
#     "name" : "Bob Smith"
# }

# retrieve student
# GET /students/{id}

# {
#     "id" : 1234456,
#     "name" : "Bob Smith"
# }

# create a class
# POST /classes

# # Request
# {
#     "name": "CMPE-273"
# }

# # Response
# {
#     "id": 1122334,
#     "name": "CMPE-273",
#     "students": []
# }

# retrieve a class
# GET /classes/{id}

# {
#     "id": 1122334,
#     "name": "CMPE-273",
#     "students": []
# }

# add a student to class
# PATCH /classes/{id}

# # Request
# {
#     "student_id": 1234456
# }

# # Response
# {
#     "id": 1122334,
#     "name": "CMPE-273",
#     "students": [
#         {
#             "id" : 1234456,
#             "name" : "Bob Smith"
#         }
#     ]
# }
