import uuid
from flask import Blueprint, request, jsonify
from firebase_admin import firestore

db = firestore.client()
user_Ref = db.collection('user')

userAPI = Blueprint('userAPI', __name__)

@userAPI.route('/add', methods=['POST'])
def createUser():
        try:
            id = uuid.uuid4()
            user_Ref.document(id.hex).set(request.json)
            return jsonify({"success":True}), 200
        except Exception as e:
              return f"Error: {e}"
        
@userAPI.route('/get-user', methods=['GET'])
def get_user():
      users = []
      for user in user_Ref.stream():
            users.append(user.to_dict())
      return jsonify(users)