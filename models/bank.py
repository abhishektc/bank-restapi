from db import db

class BankModel(db.Model):
    __tablename__ = 'bank_details'

    id = db.Column(db.Integer, primary_key=True)
    bank_name = db.Column(db.String(50))
    bank_ifsc = db.Column(db.String(11))
    bank_branch = db.Column(db.String(100))
    bank_address = db.Column(db.String(200))
    bank_city = db.Column(db.String(50))
    bank_district = db.Column(db.String(50))
    bank_state = db.Column(db.String(30))


    def __init__(self, bank_name, bank_ifsc, bank_branch, bank_address, bank_city, bank_district, bank_state):
        self.bank_name = bank_name
        self.bank_ifsc = bank_ifsc
        self.bank_branch = bank_branch
        self.bank_address = bank_address
        self.bank_city = bank_city
        self.bank_district = bank_district
        self.bank_state = bank_state

    def json(self):
        return {
            'bank_name': self.bank_name, 
            'bank_ifsc': self.bank_ifsc, 
            'bank_branch': self.bank_branch, 
            'bank_address': self.bank_address,
            'bank_city': self.bank_city, 
            'bank_district': self.bank_district, 
            'bank_state': self.bank_state,
        }