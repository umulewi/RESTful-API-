from flask import Flask, request
from flask_restful import Resource, Api
from auth import auth_required
from models import User, Simulation

app = Flask(__name__)
api = Api(app)

# User CRUD endpoints
class UserResource(Resource):
    @auth_required
    def get(self, user_id):
        # Get user by ID
        user = User.query.get(user_id)
        if user:
            return user.serialize(), 200
        return {"message": "User not found"}, 404

    @auth_required
    def put(self, user_id):
        # Update user by ID
        user = User.query.get(user_id)
        if user:
            data = request.get_json()
            user.update(data)
            return {"message": "User updated successfully"}, 200
        return {"message": "User not found"}, 404

    @auth_required
    def delete(self, user_id):
        # Delete user by ID
        user = User.query.get(user_id)
        if user:
            user.delete()
            return {"message": "User deleted successfully"}, 200
        return {"message": "User not found"}, 404

# Simulation CRUD endpoints (similar structure as UserResource)

# Add resources to the API
api.add_resource(UserResource, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
