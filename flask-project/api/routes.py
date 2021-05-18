from flask_restful import Api

from api.fruits import FruitsAPI,FruitsDelAPI

def create_route(api: Api):
    api.add_resource(FruitsAPI, '/Fruit')
    api.add_resource(FruitsDelAPI, '/Fruit/delete/<name>')
