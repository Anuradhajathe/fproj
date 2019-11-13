from model_ui mapping.models import *
from flask import session
from flask import render_template,request,redirect,url_for

@app.route("/emp/welcome/")
def welcome_page():
    return render_template('emp.html',
                           emp=Employee(id=0, cname=""),
                           emps=Employee.query.all(),
                           adrs=Address.query.all())

@app.route("/emp/save/",methods=['POST'])
def save_employee():
    eid = int(request.form['eid'])

    if eid==0:
        emodel = Employee(cname=request.form['ename'])
        selectedAdrs = request.form.getlist('sadr')
        if selectedAdrs:
            for aid in selectedAdrs:
                emodel.address.append(Address.query.filter_by(id=aid).first())

            db.session.add(emodel)
            db.session.commit()
            msg = "Added Successfully....!"
        else:
            msg="Addresses are mandatory.."

    else:
        empinstance = Employee.query.filter_by(id=eid).first()
        empinstance.cname=request.form['ename']
        empinstance.address.clear()
        selectedAdrs = request.form.getlist('sadr')
        if selectedAdrs:
            for aid in selectedAdrs:
                empinstance.address.append(Address.query.filter_by(id=aid).first())

        db.session.commit()
        msg= "Updated Successfully....!"
    return render_template('emp.html',
                           amsg = msg,adrs=Address.query.all(),
                           emp= Employee(id=0,cname=""),
                           emps = Employee.query.all(),a=0)


@app.route("/edit/emp/<int:eid>")
def edit_emp(eid):
    empinstance = Employee.query.filter_by(id=eid).first()
    return render_template('emp.html',
                           emp=empinstance,adrs=Address.query.all(),
                           emps=Employee.query.all(),a=1)

@app.route("/delete/emp/<int:eid>")
def delete_emp(eid):
    empinstance = Employee.query.filter_by(id=eid).first()
    if empinstance:
        db.session.delete(empinstance)
        db.session.commit()
        msg="Deleted Successfully...."

    return render_template('emp.html',
                           amsg=msg,adrs=Address.query.all(),
                           emp=Employee(id=0, cname=""),
                           emps=Employee.query.all(),a=0)



#------------------------------------------------------------
def bynamesort(emp):
    return emp.cname.upper()

def sortedemps():
    emps = Employee.query.all()
    emps.sort(key=bynamesort)
    return emps

@app.route("/address/welcome/")
def welcome_page_address():
    return render_template('address.html',
                           adr=Address(id=0, city=""),
                           adrs=Address.query.all(),
                           emps = sortedemps(),a=0
                           )

@app.route("/address/save/",methods=['POST'])
def save_address():
    adrid = int(request.form['aid'])
    adrcity = request.form['acity']

    if adrid==0:
        db.session.add(Address(city=adrcity))
        db.session.commit()
        msg="Address Saved Successfully..."
    else:
        adr = Address.query.filter_by(id=adrid).first()
        adr.city=adrcity
        #adr.eid=int(request.form['semp'])
        db.session.commit()
        msg = "Address Updated Successfully..."
    return render_template('address.html',emps = sortedemps(),
                           adr=Address(id=0, city=""),a=0,
                           adrs=Address.query.all(),amsg=msg)


@app.route("/edit/address/<int:aid>")
def edit_address(aid):

    return render_template('address.html',emps = sortedemps(),
                           adr=Address.query.filter_by(id=aid).first(),
                           adrs=Address.query.all(),a=1)


@app.route("/delete/address/<int:aid>")
def delete_address(aid):
    adr = Address.query.filter_by(id=aid).first()
    if adr:
        db.session.delete(adr)
        msg="Address Deleted Successfully...!"
    return render_template('address.html',
                           adr=Address(id=0, city=""),
                           adrs=Address.query.all(),a=0,
                           amsg=msg,emps =sortedemps())


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

