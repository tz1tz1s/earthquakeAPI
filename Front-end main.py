from flask import Flask
from flask import request, render_template
from flask_restful import Api, Resource
import mysql.connector
import json
import requests
from datetime import datetime
import self
import urllib.parse as urlparse
from urllib.parse import parse_qs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser


app = Flask(__name__)
api= Api(app)

mydb = mysql.connector.connect(
    host="dalab.ee.duth.gr",
    user='s58198',
    password="116396",
    database='s58198'
)

@app.route("/")
def start():

    return render_template('MainPage.html')

@app.route("/2")
def Search():
    #mycursor1 = mydb.cursor()
    #mycursor1.execute("SELECT City FROM Cities;")
    #myresults1 = mycursor1.fetchall()
    #mycursor2 = mydb.cursor()
    #mycursor2.execute("SELECT Mag FROM Magnitude;")
    #myresults2 = mycursor1.fetchall()
    #mycursor3 = mydb.cursor()
    #mycursor3.execute("SELECT Date FROM Date;")
    #myresults3 = mycursor1.fetchall()
    #mycursor4 = mydb.cursor()
    #mycursor4.execute("SELECT Id FROM Cities;")
    #myresults4 = mycursor1.fetchall()
    #num = len(myresults1)
    #return render_template('SearchWindow.html', list_header='Results:', Cities=myresults1, Mag=myresults2, Date=myresults3, Id=myresults4, test=num)
    responce = json.loads(requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson").text)
    City = []
    Mag = []
    Date= []
    num = len(responce["features"])
    for i in range(len(responce["features"])):
        City.append(responce["features"][i]["properties"]["place"])
        Mag.append(responce["features"][i]["properties"]["mag"])
        temp = int(responce["features"][i]["properties"]["time"])
        timestamp = temp / 1000
        time = datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')
        Date.append(time)
    return render_template('SearchWindow.html', list_header = 'Results',Cities=City, Mag=Mag, Date=Date, test=num)

@app.route("/3/<int:x>")
def all_results(x):
    responce = json.loads(
        requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson').text)
    City = []
    Mag = []
    Date = []
    types= []
    num = len(responce["features"])
    City.append(responce["features"][x]["properties"]["place"])
    Mag.append(responce["features"][x]["properties"]["mag"])
    temp = int(responce["features"][x]["properties"]["time"])
    types.append(responce["features"][x]["properties"]["types"])
    timestamp = temp / 1000
    time = datetime.fromtimestamp(timestamp).strftime('%d-%m-%y')
    Date.append(time)
    return render_template('Details.html', list_header='Results', Cities=City, Mag=Mag, Date=Date, test=num, Types=types)


if __name__ == '__main__':
    app.run(port=5002)