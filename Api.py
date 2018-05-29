from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from Check_Pnr.Search_api import SearchAPI

app = Flask(__name__)
CORS(app)
api = Api(app)



api.add_resource(SearchAPI,'/')

if __name__ == '__main__':
    app.run(debug=True)