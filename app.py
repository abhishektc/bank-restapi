from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.bank import BankListAutoComplete, BankListCity, Bank

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:abhishek@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'abhishek'
api = Api(app)

api.add_resource(BankListAutoComplete, '/api/branches/autocomplete/<string:name>')
api.add_resource(BankListCity, '/api/branches/<string:name>')
api.add_resource(Bank, '/api/bankDetails/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
