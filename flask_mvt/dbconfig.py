from flask import Flask  #controller
from flask_sqlalchemy import SQLAlchemy #ORM
app = Flask(__name__) #FLASK obj
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)