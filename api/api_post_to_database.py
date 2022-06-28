from flask import Flask,redirect,request
import mysql.connector

app =  Flask(__name__)

mydb = mysql.connector.connect(
  host="",
  user="s58198",
  password="116396",
  database="s58198"
)


@app.route('/')

def hello_world():
    return "hello world"


@app.route('/api/get/', methods=['GET','POST'])

def get_data_from_backend():
    if request.method == 'POST':
        time_p = request.form["time"]
        magnitude_p = request.form["mag"]
        place_p = request.form["place"]



    time_post = time_p
    magnitude_post = magnitude_p
    place_post =  place_p
    mycursor = mydb.cursor()
    final_sql_statement2 = """ INSERT INTO all_in_one (time_stamp,magnitude,City) VALUES (%s,%s,%s)"""
    entry_tuple = (time_post, magnitude_post, place_post)


    mycursor.execute(final_sql_statement2, entry_tuple)
    mydb.commit()

    print("data posted")
    return "data posted"



if __name__ == '__main__':
    app.run(port = 5002)
