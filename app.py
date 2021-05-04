from flask import Flask, render_template, request, session, redirect
from db import create_contact, get_contact

app = Flask(__name__)
app.secret_key = 'as6d8a1sd89234#%%LKsadasmd78y3289y687314asd8'
@app.route('/',methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        nombre = request.form['name']
        email = request.form['email']
        msg = request.form['message']
        contact = (nombre,email,msg)
        create_contact(contact)
    return render_template('index.html')


@app.route('/kaizen-administrator',methods=['GET'])
def admin():
    if request.method == 'GET' and 'login' in session:
        if session['login'] == None:
            return redirect('/kaizen-login')
        elif session['login'][0] != 'superadminkaizen2021' and session['login'][1] != 'administrator123':
            return redirect('/kaizen-login')
    elif request.method == 'GET' and  not 'login' in session:
        return redirect('/kaizen-login')
    elif request.method == 'POST':
        return redirect('/')
    
    data = get_contact()
    if data == None:
        data = []
    return render_template('admin.html',data=data)


@app.route('/kaizen-login',methods=['GET','POST'])
def login():
    if request.method == 'GET' and 'login' in session:
        if session['login'] != None:
            if session['login'][0] == 'superadminkaizen2021' and session['login'][1] == 'administrator123':
                return redirect('/kaizen-administrator')
    if request.method == 'GET':
        return render_template('login.html',data=[False,False])
    if request.method == 'POST':
        data = [False,False]
        if request.form['name'] != 'superadminkaizen2021':
            data[0] = True
        if request.form['pass'] != 'administrator123':
            data[1] = True
        if  data[0] == False and data[1] == False:
            session['login'] = [request.form['name'],request.form['pass']]
            return redirect('/kaizen-administrator')
        else:
            return render_template('login.html',data=data)

 
@app.route('/kaizen-logout',methods=['GET'])
def logout():
    if 'login' in session:
        session['login'] = None
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True,port=3000)