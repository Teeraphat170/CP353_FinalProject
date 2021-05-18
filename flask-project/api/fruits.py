from flask import request,jsonify,Response,current_app
from flask_restful import Resource
import json

class FruitsAPI(Resource):
    def get(self)-> Response:
        if 'name' not in request.args:
            return readJsonALL(),200
        elif 'name' in request.args:
            name = request.args.get('name')
            data = readJsonFile()
            res = []
            obj = json.loads(data)
            for i in obj:
                if i['name'] == name:
                    res = i
                    break
            res = jsonify(res)
            res.status_code = 200
            return res
        else:
            return Response(status=204)
    
    def post(self)->Response:
        body = request.get_json()
        #print(body)
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        for i in obj:
            data.append(i)
        
        if len(body) > 0:
            data.append(body)

        with open('fruits.json','w') as outfile:
            json.dump(data, outfile)
            response = jsonify(data)
            response.status_code = 200
            return response
    
    def put(self)->Response:
        body = request.get_json()
        key = body['key']
        #print(key)
        read = readJsonFile()
        obj = json.loads(read)
        isSucess = False
        data = list()
        i = 2
        for i in obj:
            data.append(i)
            if i['name'] == key:
                data.remove(i)
                isSucess = True

        del body['key']
        data.append(body)

        if isSucess is True:
            with open('fruits.json','w') as outfile:
                json.dump(data, outfile)
                response = jsonify(data)
                response.status_code = 200
                return response
        else:
            return Response(status=204)
#{"color": "Green", "name": "Green Apple", "types": "Apples and pears", "pic": "static/pic/green apple.jpg"}
class FruitsDelAPI(Resource):
    def delete(self,name: str)->Response:
        key = name
        read = readJsonFile()
        obj = json.loads(read)
        data = list()
        isSucess = False
        for i in obj:
            data.append(i)
            if i['name'] == key:
                data.remove(i)
                isSucess = True

        with open('fruits.json','w') as outfile:
            json.dump(data, outfile)

        if isSucess is True:
            response = jsonify(data)
            response.status_code = 200
            return response
        else:
            return Response(status=204)

def readJsonALL():
    open_json_file = open('fruits.json', 'r') 
    read_json_file = open_json_file.read()
    data = json.loads(read_json_file)
    return data

def readJsonFile():
    with open('fruits.json','r') as plant:
            data = plant.read()
    return data