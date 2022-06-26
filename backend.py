from flask import Flask
from flask import request, render_template
import requests
import json
from datetime import datetime

app = Flask(__name__)


@app.route("/input")
def backend_index():
    return render_template('backend_form.html')


@app.route("/input/<int:a>", methods=['GET', 'POST'])
def backend(a):
    if request.method == "POST":
        url = request.form.get("url")
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        global y
        y = json.loads(response.text)
        b_dict = {}

        for i in range(len(y["features"])):
            temp = int(y["features"][i]["properties"]["time"])
            timestamp = temp / 1000
            global time, mag, place
            time = str(datetime.fromtimestamp(timestamp).strftime('%d-%m-%y'))
            mag = y["features"][i]["properties"]["mag"]
            place = y["features"][i]["properties"]["place"]
            a_dict={}
            for variable in ["time","mag","place"]:
                a_dict[variable]=eval(variable)
                b_dict[i]=a_dict
        if a == 2:
            api_url = "http://127.0.0.1:5002/api/get/"
            for i in range(len(y["features"])):
                headers1=headers
                payload1=b_dict.get(i)
                #x = requests.request("POST", api_url, headers=headers1, data=payload1)
        return ("DATA POSTED SUCCESSFULLY")
    return render_template('backend_form.html')


if __name__ == '__main__':
    app.run(port=5000)
