from flask_restful import Resource
from models.bank import BankModel
from flask_cors import cross_origin
class BankListAutoComplete(Resource):
    
    # with limit and offset
    def get(self, name):
        return {'banks': [x.json() for x in BankModel.query.filter(BankModel.bank_branch.like(name.upper() + '%')).order_by(BankModel.bank_ifsc).limit(3).offset(0)]}, 200

    # def get(self, name):
    #     return {'banks': [x.json() for x in BankModel.query.filter(BankModel.bank_branch.like(name.upper() + '%')).order_by(BankModel.bank_ifsc).all()]}


class BankListCity(Resource):
    def get(self, name):
        if name == 'All':
            return {'banks': [x.json() for x in BankModel.query.order_by(BankModel.bank_ifsc).all()]}
        return {'banks': [x.json() for x in BankModel.query.filter_by(bank_city = name.upper()).order_by(BankModel.bank_ifsc).all()]}, 200

    # with limit and offset
    # def get(self, name):
    #     return {'banks': [x.json() for x in BankModel.query.filter_by(bank_city = name.upper()).order_by(BankModel.bank_ifsc).limit(4).offset(0)]}


class Bank(Resource):
    @cross_origin()
    def get(self, name):
        bank = BankModel.query.filter_by(bank_ifsc = name.upper()).first()
        return {'bank': BankModel.json(bank)}, 200

