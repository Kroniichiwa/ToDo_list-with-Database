from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
api = Api(app)

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, server_default='f', nullable=False)

    def __repr__(self):
        return f"Todo(name: {name}, Task status: {status})"

# Fields to serialize the response object
resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "status": fields.Boolean
}

#Create the db tables (only use for the first time)
#db.create_all()

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_name):
        todo = TodoModel.query.all()
        return todo, 200

    @marshal_with(resource_fields)
    def post(self, todo_name):
        result = TodoModel.query.filter_by(name=todo_name).first()
        if result:
            abort(409, message="Name already exists!")
        new_todo = TodoModel(name=todo_name, status=False)
        db.session.add(new_todo)
        db.session.commit()
        return new_todo, 201
    
    @marshal_with(resource_fields)
    def patch(self, todo_name):
        result = TodoModel.query.filter_by(name=todo_name).first()
        if not result:
            abort(404,message="Name invalid!")
        if result.status == True :
            result.status = False 
        elif result.status == False :
            result.status = True 
        db.session.commit()
        return result,202
    
    @marshal_with(resource_fields)
    def delete(self, todo_name):
        result = TodoModel.query.filter_by(name=todo_name).first()
        if not result:
            abort(404, message="Name not found...")
        db.session.delete(result)
        db.session.commit()
        return '', 204


#call
api.add_resource(Todo, "/Todo/<string:todo_name>")

if __name__ == "__main__":
    app.run(debug=True)
