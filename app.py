from flask import Flask, render_template, request, redirect, url_for, flash

import mysql.connector as connector
db = connector.connect(host="localhost",user="root",passwd="root",database="python")



app = Flask(__name__)
app.secret_key ='fsadfgsgs45ys3564'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        name = request.form["name"]
        dob = request.form["dob"]
        gender = request.form["gender"]
        weight = request.form["weight"]
        height = request.form["height"]
        color = request.form["color"]
        country = request.form["country"]

        print(name,gender,dob,weight,height,color,country)
        cursor = db.cursor()
        sql = "INSERT INTO `refugee`(`name`, `country`, `dob`, `gender`, `weight`, `height`, `color`)  VALUES (%s,%s,%s,%s,%s,%s,%s)"
        values = (name,country,dob,gender,weight,height,color)
        cursor.execute(sql,values)
        db.commit()
        flash('Saved Successfully to the Database')
        return redirect(url_for('matokeo'))

    return render_template("Refugee_form.html")

@app.route('/matokeo')
def matokeo():
    cursor = db.cursor()
    sql = "SELECT * FROM `refugee`"
    cursor.execute(sql)
    refugees = cursor.fetchall()
    return render_template('Refugee_output.html', refugees=refugees)

@app.errorhandler(404)
def error_page(e):
    print("error")
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)

