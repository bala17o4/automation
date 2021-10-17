from os import name
from flask import *

app = Flask(__name__)


@app.route('/login', methods = ['POST','GET'])
def login():
    return render_template('login.html')

@app.route('/submit')
def about():
    if request.method=='POST':
        data = request.form
        return render_template("submit.html",data = data)




@app.route('/')
def intro():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)