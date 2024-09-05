#  For Testing endpoints

import requests
import json

def post_data():
    data = {
        'name': 'Ahmad',
        'roll_no': 1222,
        'email' : 'sohailahmed34280@gmail.com',
        'city' : 'Pindi',
    }
    
    json_data = json.dumps(data)
    requests.post(url='http://127.0.0.1:8000/api/create_student/', data=json_data)
    
    
# post_data()

def put_data():
    data = {
        'id' : 1,
        'name': 'Updated Name',
        'roll_no': 23,
        'email' : 'ahmed34280@gmail.com',
        'city' : 'Pindi',
    }
    
    json_data = json.dumps(data)
    requests.put(url='http://127.0.0.1:8000/api/update_student/', data=json_data)
    
# put_data()

def delete_data():
    data = {
        'id' : 3,
    }
    
    json_data = json.dumps(data)
    requests.delete(url='http://127.0.0.1:8000/api/delete_student/', data=json_data)


delete_data()
    