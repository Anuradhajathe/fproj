from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    cname = db.Column('COLLEGE_NAME', db.String(80), nullable=False)
    address = db.relationship('Address', backref='employee',
                              lazy=True, uselist=True,
                              cascade = "all,delete")
class Address(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column('COLLEGE_NAME', db.String(80), nullable=False)
    eid = db.Column('emp_id', db.Integer,
                    db.ForeignKey('employee.id'),
                    nullable=True)



if __name__ == '__main__':
    db.create_all()
    adrs = Address.query.all()
    for adr in adrs:
        print(adr.employee)