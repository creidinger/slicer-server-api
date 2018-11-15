'''
Basic Flask App
'''

from flask import Flask, url_for, request, render_template, redirect
app = Flask(__name__)


#
# ROUTERS
#
@app.route('/')
@app.route('/<name>')
def index(name=None):
    # return 'PerceptEngine - Slicer'
    return render_template('index.html', name=name)

@app.route('/slicer')
def slicer():
    return redirect(url_for('index'))

@app.route('/about')
def about():
    return 'About Page'

@app.route('/s3')
def s3_transport():
    return 'Send/Receive data from the s3'

@app.route('/s3/<company>')
def show_company(company):
    return 'Your company is ' + company

@app.route('/s3/<int:company_code>')
def show_company_code(company_code):
    return 'Your company code is ' + company_code

# URL Building
with app.test_request_context():
    print(url_for('index'))
    print(url_for('slicer'))


# HTTP Methods
#from flask import request

@app.route('/gui-exchange', methods=['GET', 'POST'])
def gui_exchange():
    if request.method == 'POST':
        return 'Request from Gui Received'
    else:
        return 'Sending data to gui'

# Rendering Templates
#from flask import render_template

@app.route('/slicing/')
@app.route('/slicing/<name>')
def slicing(name=None):
    return render_template('slicing.html', name=name)

# The Request Objct
#from flask import request

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

# File Uploads
# from flask import request
#
# @app.route('upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')
