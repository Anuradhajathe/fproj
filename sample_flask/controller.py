from flask import Flask,render_template,request
from sample_flask.models import Employee,app,db



#http://localhost:5000/welcome/

@app.route("/welcome/")
def welcome_page():
    #Employee(eid=1, ename='PQRABC', eemail='pabc@gmail.com',eage=63, esalary=58854.45)
    return render_template('sample.html',emps = Employee.query.all(),
                           empob=Employee(eid=0,ename='',eemail='',eage=0,esalary=0.0))

@app.route("/emp/save/",methods=["POST"])
def save_employee():
    print(request.args)#request uri
    print(request.form) #request body


    emp = Employee(eid=request.form['eid'],
             ename=request.form['enam'],
             eemail=request.form['eemail'],
             eage=request.form['eage'],
             esalary=request.form['esal'])

    dbemp = Employee.query.filter_by(eid=int(request.form['eid'])).first()
    if dbemp:
        return render_template('sample.html',emps = Employee.query.all(),
                               msg = "Employee already exists..!",empob=emp)

    db.session.add(emp)
    db.session.commit()

    return render_template('sample.html',emps = Employee.query.all(),
                           msg="Emp Added Successfully...!",empob=Employee(eid=0,ename='',eemail='',eage=0,esalary=0.0))


if __name__ == '__main__':
    db.create_all() #will create table before server starts
    app.run(debug=True)