from flask_mvt.dbconfig import db

#model -- since-- it is -- child of db.model
# this class is aware about -- fields+columns, class+tables,
#db constraints
# will have param constructor bydefault-- with defined params

class Product(db.Model):
    pid=db.Column('PROD_ID',db.Integer(),primary_key=True)
    pname=db.Column('PROD_NAME',db.String(100))
    pcat = db.Column('PROD_CAT', db.String(100),unique=True)
    pqty = db.Column('PROD_QTY', db.Integer())
    pdsc = db.Column('PROD_DESC', db.String(100))
    pven = db.Column('PROD_VEN', db.String(100))
    pprice=db.Column('PROD_PRICE',db.Float())

    def __str__(self):
        return f'''
            ProductID : {self.pid}
            Product Name :{self.pname}
            Product Cat :{self.pCat}
        '''

    def __repr__(self):
        return str(self)

#db.drop_all()
#import time
#time.sleep(3)
db.create_all()
if __name__ == '__main__':
    p1 = Product(pid=111,pname='AAAAA',pcat='A+',pdsc='XX',pven='flip',pprice=2993.4)
    db.session.add(p1)
    db.session.commit()