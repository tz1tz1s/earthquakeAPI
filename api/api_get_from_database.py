import json

from flask import Flask, redirect, request, jsonify

import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="final_db"
)
mycursor = mydb.cursor()


@app.route('/')
def hello():
    print("Hello World")
    return "hello world"


@app.route("/get_data_length", methods=['GET', 'POST'])
def get_data_from_database():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM all_in_one")
    myresult = mycursor.fetchall()
    print(jsonify(myresult))
    num_of_id = len(myresult)
    return str(num_of_id)


@app.route("/get_data_by_id/<int:ID>", methods=['GET'])

def return_data_by_id(ID):
    mycursor = mydb.cursor()
    #mycursor.execute("SELECT * FROM all_in_one WHERE ID=" + str(ID))
    mycursor.execute("SELECT * FROM all_in_one ")
    myresult = mycursor.fetchall()
    return jsonify(myresult)


@app.route("/get_data_mag/<int:magn>", methods=['GET'])

def return_data_by_magnitude(magn):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM all_in_one WHERE magnitude >" + str(magn))
    myresult = mycursor.fetchall()
    return jsonify(myresult)



if __name__ == '__main__':
    app.run(port="5006")
