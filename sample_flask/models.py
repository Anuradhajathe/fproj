from flask import Flask   #webapp
from flask_sqlalchemy import SQLAlchemy #ORM
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Employee(db.Model):
    eid = db.Column("emp_id",db.Integer(),primary_key=True)
    ename = db.Column("emp_name", db.String(50))
    eemail = db.Column("emp_email", db.String(50),unique=True)
    eage = db.Column("emp_age", db.Integer())
    esalary = db.Column("emp_sal", db.Float())

    def __str__(self):
        return f'''\n
            Emp ID : {self.eid},
            Emp NAME : {self.ename},
            Emp SAL : {self.esalary},
            Emp EMAIL : {self.eemail},
            Emp AGE : {self.eage},
        '''
    def __repr__(self):
        return str(self)
