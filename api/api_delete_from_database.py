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


@app.route("/delete_from_database_by_id/<int:ID>", methods=['GET', 'POST'])
def get_data_from_database(ID):
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM all_in_one WHERE ID = ",str(ID) )
    mycursor.commit()

    return "DELETED"


if __name__ == '__main__':
    app.run(port="5007")
