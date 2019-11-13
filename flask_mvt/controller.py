from flask_mvt.dbconfig import app,db
from flask_mvt.model import Product
from flask import render_template as rt,request as req

def dummyprod():
    return Product(pid=0,pname='',pcat='',pdsc='',pven='',
                   pprice=0.0,pqty=0)

@app.route("/product/welcome/",methods=["GET"])
def welcome_page():
    return rt('product.html',products=Product.query.all(),prod=dummyprod())

@app.route("/product/save/",methods=["POST"])
def save_product():
    print(req.form)
    pid = int(req.form['pid']) #get product id from form,req

    dbprodsc = Product.query.filter_by(pcat=req.form['pcat']).first() # check in db

    prd = Product(pid=req.form['pid'],  # names referred from html name attribute
                  pname=req.form['pnm'],
                  pcat=req.form['pcat'],
                  pdsc=req.form['pdesc'],
                  pven=req.form['pven'],
                  pprice=req.form['pprice'],
                  pqty=req.form['pqty'])

    if dbprodsc:
        return rt('product.html', msg="Product Category Duplicate one", products=Product.query.all(), prod=prd)

    dbprod = Product.query.filter_by(pid=pid).first()  # check in db
    if dbprod: # if already present -- update
        dbprod.pname = req.form['pnm']
        dbprod.pcat = req.form['pcat']
        dbprod.pven = req.form['pven']
        dbprod.pprice = req.form['pprice']
        dbprod.pdsc = req.form['pdesc']
        dbprod.pqty = req.form['pqty']
        db.session.commit()
        actionmsg = "Product Updated Successfully...!"
    else: #if not present -- add new
        db.session.add(prd)
        db.session.commit()
        actionmsg = "Product Added Successfully...!"
    return rt('product.html',msg=actionmsg,products=Product.query.all(),prod=dummyprod())

@app.route("/product/edit/<int:pid>",methods=["GET"])
def edit_product(pid):
    dbprod = Product.query.filter_by(pid=pid).first()  # check in db
    return rt('product.html', products=Product.query.all(),
              prod=dbprod)


@app.route("/product/delete/<int:pid>",methods=["GET"])
def delete_product(pid):
    dbprod = Product.query.filter_by(pid=pid).first()  # check in db
    db.session.delete(dbprod)
    db.session.commit()
    actionmsg="Product record deleted..!"
    return rt('product.html',products=Product.query.all(),
              prod=dummyprod(),msg=actionmsg)

@app.route("/product/welcome/",methods=["GET"])
def get_all_products():
    pass

if __name__ == '__main__':
    app.run(debug=True)

