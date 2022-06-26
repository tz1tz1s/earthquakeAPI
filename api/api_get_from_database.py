import json

from flask import Flask,redirect,request,jsonify

import mysql.connector

app =  Flask(__name__)

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

@app.route("/get_data",methods=['GET','POST'])

def get_data_from_database():


    get_data_sql = """
    SELECT JSON_OBJECT ('id', ID,'magnitude', magnitude,'timestamp', time_stamp,'Place',City) FROM all_in_one;
    """
    mycursor.execute(get_data_sql)
    data = mycursor.fetchall()
    print(data[1][0])
    return str(data[1][0])



if __name__ == '__main__':
    app.run(port = "5003")