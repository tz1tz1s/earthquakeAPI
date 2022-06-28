from flask import Flask
from flask import request, render_template
from flask_restful import Api
import json
import requests



app = Flask(__name__)
api = Api(app)


@app.route("/")
def start():

    return render_template('MainPage.html')

@app.route("/Search_results/<int:x>")
def Search(x):
    length = int(requests.get("http://127.0.0.1:5006/get_data_length").text)
    City = []
    Mag = []
    time = []
    if x==0:
        for i in range(length):
            url1= "http://127.0.0.1:5006/get_data_by_id/"+str(i+1)
            data = json.loads(requests.get(url1).text)
            City.append(data[3])
            Mag.append(data[2])
            time.append(data[1])
        return render_template('SearchWindow.html', list_header='Results', Cities=City, Mag=Mag, Date=time, test=length)

    if x==1:
        mag = request.args.get("Magnitude")
        url2= "http://127.0.0.1:5006/get_data_mag/"+str(mag)
        data = json.loads(requests.get(url2).text)
        length= len(data)
        for i in range(length):
            City.append(data[i][3])
            Mag.append(data[i][2])
            time.append(data[i][1])
        return render_template('SearchWindowDiff.html', list_header = 'Results',Cities=City, Mag=Mag, Date=time, test=length,num=mag)
    return ("Something went wrongh")

@app.route("/Details/<int:x>/<int:y>")
def details(x, y):
    length = int(requests.get("http://127.0.0.1:5006/get_data_length").text)
    City = []
    Mag = []
    time = []
    if x == 0:
        url1 = "http://127.0.0.1:5006/get_data_by_id/" + str(y+1)
        data = json.loads(requests.get(url1).text)
        City.append(data[3])
        Mag.append(data[2])
        time.append(data[1])
    if x==1:
        mag = request.args.get("Magnitude")
        url2= "http://127.0.0.1:5006/get_data_mag/"+str(mag)
        data = json.loads(requests.get(url2).text)
        length= len(data)
        City.append(data[y][3])
        Mag.append(data[y][2])
        time.append(data[y][1])
    return render_template('Details.html', list_header = 'Results',Cities=City, Mag=Mag, Date=time, test=length)


if __name__ == '__main__':
    app.run(port=5004)
