from flask_restful import Resource
from authz.controller.apiv1 import UserController

class UserResource(Resource):
    def get(self, user_id=None):
        """
        GET /users --> GET list of users
        GET /users/<user_id> --> Get user.
        """
        if user_id == None:
            return UserController.get_users()
        else:
            return UserController.get_user(user_id)
            
    def post(self):
        """
        POST /users --> create new user
        POST /user/<user_id> --> not allowed
        """
        return UserController.create_user()

    def patch(self, user_id):
        """
        PATCH /users --> not allowed
        PATCH /users/<user_id> --> update user
        """
        return UserController.update_user(user_id)

    def delete(self, user_id):
        """
        DELETE /users --> not allowd
        DELETE /users/<user_id> --> del user
        """
        return UserController.delete_user(user_id)
