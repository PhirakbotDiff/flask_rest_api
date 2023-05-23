from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

class RestFullApi(Resource):
	
	def get(self, name, method):
		return {"Name": name, "Method": method}
	
	def post(self, name, method):
		return {"Name": name, "Method": method}

api.add_resource(RestFullApi, "/RestFull/<string:name>/<string:method>")

# Storing Data in Memory
# Define dict
data_info = {
				"person1": {"name":"phirakbot", "gender":"male"},
				"person2": {"name":"phalla", "gender":"male"}
			}

class RestFullApiII(Resource):
	
	def get(self, person):
		return data_info.get(person, "")
	
	def post(self, person):
		return data_info.get(person, "")

api.add_resource(RestFullApiII, "/RestFull/<string:person>")

# Request Args Parsar, Sending Status code, Handing Delete request
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of this video.", required=True)
video_put_args.add_argument("like", type=int, help="Like of this video.", required=True)
video_put_args.add_argument("view", type=int, help="View of this video.", required=True)
video = {}

def validation_id(id):
	if id not in video:
		abort(404, message="not found a video...")

def validation_exist_id(id):
	if id in video:
		abort(409, message="existing video...")

class RestFullParsar(Resource):

	def get(self, id):
		validation_id(id)
		return video[id]

	def put(self, id):
		validation_exist_id(id)
		args 		= video_put_args.parse_args()
		video[id] 	= args
		print("video ====>", video[id])
		return video[id], 201
	
	def delete(self, id):
		validation_id(id)
		del video[id]
		return '', 204

api.add_resource(RestFullParsar, "/RestFull/<int:id>")

if __name__ in "__main__" :
	app.run(debug=True)