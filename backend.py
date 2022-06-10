from flask import Flask
from flask import request, render_template, jsonify
import requests
import json
from datetime import datetime
from flask import g, globals

app = Flask(__name__)


@app.route("/input")
def backend_index():
    return render_template('backend_form.html')

@app.route("/input/<int:a>", methods=['GET','POST'])
def backend(a):
    if request.method == "POST":
        url = request.form.get("url")
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        global y
        y = json.loads(response.text)
        for i in range(len(y["features"])):
            temp = int(y["features"][i]["properties"]["time"])
            timestamp = temp / 1000
            global time,mag,place
            time = str(datetime.fromtimestamp(timestamp).strftime('%d-%m-%y'))
            mag = y["features"][i]["properties"]["mag"]
            place = y["features"][i]["properties"]["place"]
        if a==2:
            payload1 = {}
            for i in range(len(y["features"])):
                for variable in ["time", "mag", "place"]:
                    payload1[variable] = eval(variable)
                    api_url = "https://127.0.0.1/5001/api/get/"
                    headers1 = {}
                    x = requests.request("POST",api_url, headers=headers1, data=payload1)
            return ("DATA POSTED SUCCESSFULLY",payload1)
    return render_template('backend_form.html')

if __name__ == '__main__':
    app.run(port = 5000)