from flask import Flask, jsonify, request
from flask_restful import Api, Resource

from Config import DBconfig

import json
import pymongo
import bson.errors
from bson.json_util import dumps, loads

# instantiate the app with flask constructor
app = Flask(__name__)

# Here we load the configurations  to the flask instance
app.config.from_object(DBconfig)

# Aun use the API from resource, that permit us, to built APIS, with flask
api = Api(app)

# Create a engine with the database
mongoClient = pymongo.MongoClient(app.config['URI'])


class CRUD(Resource):
    """
    The class CRUD inherit from Resource that permit us to overwrite, some methods like, GET, POST,PUT AND POST,
    To build a API
    """

    def __init__(self):
        """
        here we initiate the connection with the database, and we capture the request in the global context

        Args:
            db : cursor of the database
            Data : json information

        """
        self.db = mongoClient['foundation-test1']
        if not request.method in ['GET', 'DELETE']:
            self.Data = request.get_json()

    def get(self, Key=None):
        """
        Here we consult all the existing collections in the database

        :return: A list containing all the serialized jsons from the database
        """

        # In the case that the Key is empty, that mean that we have return all the records
        if Key is None:
            Provider = [dumps(Prov) for Prov in self.db.providers.find()]
        else:

            '''
                We verify if the path contain in his second pisition have Object id, that means
                that the user what to get a record where his index is a object id string
            '''

            # Use list comprehension, to dumps all the json with ObjectID and other bson objects

            if request.path.split('/')[2] == 'ObjectId':
                ID = {'$oid': eval(Key)}

                Provider = [dumps(Prov) for Prov in self.db.providers.find({"_id": loads(str(json.dumps(ID)))})]
            else:
                # If the id is  a normal string, just loads the variable and get the record
                Provider = [dumps(Prov) for Prov in self.db.providers.find({"_id": loads(Key)})]
            if not Provider:
                Response = jsonify({'Information': 'The id ' + str(Key) + ' dont exist on the db'})
                Response.status_code = 404
                return Response

        Response = jsonify(list(map(json.loads, Provider)))
        Response.status_code = 200
        return Response

    def delete(self, Key):
        """
        Here we delete some collection from the database, with some particular key

        :return: A message indicating if the operation was successful or if an exception was triggered
        """
        try:
            '''
              We verify if the path contain in his second pisition have Object id, that means
              that the user what to delete a record where his index is a object id string
             '''
            if request.path.split('/')[3] == 'ObjectId':
                ID = {'$oid': eval(Key)}
                # Use dumps and load, to  convert some bson object, for the correct processing on the database
                self.db.providers.remove(loads(str(json.dumps(ID))))
            else:
                # If the id is  a normal string, just loads the variable and delete  the record
                self.db.providers.remove(loads(Key))

        except bson.errors.InvalidId:
            # Id  InvalidID error is triggered, it's mean that the value sended, don't exist on the db
            Response = jsonify({'Information': 'The value ' + str(self.Data) + ' dont exist on the db'})
            Response.status_code = 404
            return Response
        # If all run successfully
        Response = jsonify({'Message': 'The user have been deleted'})
        Response.status_code = 200
        return Response

    def put(self, Key):
        """
        Here we update some collecion from the database, taken the _id as a search index
        :return: A message indicating if the operation was successful or if an exception was triggered
        """

        try:
            '''
                We verify if the path contain in his second pisition have Object id, that means
                that the user what to update a record where his index is a object id string
            '''
            if request.path.split('/')[3] == 'ObjectId':
                ID = {'$oid': eval(Key)}
                self.db.providers.update({"_id": loads(str(json.dumps(ID)))}, {"$set": self.Data})
            else:
                # If the id is  a normal string, just loads the variable and update  the record
                self.db.providers.update({"_id": loads(Key)}, {"$set": self.Data})

        except bson.errors.InvalidId:
            # Id  InvalidID error is triggered, it's mean that the value sanded, don't exist on the db
            Response = jsonify({'Information': 'The id ' + str(Key) + ' dont exist on the db'})
            Response.status_code = 404
            return Response

        # If all run successfully
        Response = jsonify({'Message': 'The user have been update'})
        Response.status_code = 202
        return Response

    def post(self):
        """
        Here we just create a new provider, with the json data sended

        :return:  A message indicating if the operation was successfull or if an exception was triggered
        """
        try:
            self.db.providers.insert(self.Data)
        except pymongo.errors.DuplicateKeyError:
            # If exist some record with the same _id the exception gonna raise, and the message gonna display
            Response = jsonify({'Message': 'The _id  ' + str(self.Data['_id']) + ' already exist'})
            Response.status_code = 404
            return Response

        # If all run successfully
        Response = jsonify({'Message': 'The user have been created'})
        Response.status_code=201
        return Response


# Here we add the URL resource to the API object
api.add_resource(CRUD, '/Provider',
                 '/Provider/<Key>', '/Provider/ObjectId/<Key>',
                 '/Provider/Delete/<Key>', '/Provider/Delete/ObjectId/<Key>',
                 '/Provider/Update/<Key>', '/Provider/Update/ObjectId/<Key>',
                 '/Provider/Add')

if __name__ == '__main__':
    """
    Here we just run the instance app with the run method, indicating, what addrees and port
    
    """
    try:
        # On this occasion we use self-signed https certificates just like extra :V
        app.run(debug=True, host='127.0.0.1', port=4444,ssl_context=('Certificate/public.pem', 'Certificate/private.pem'))
    except IOError as e:
        # If something bad happend
        print(e)
