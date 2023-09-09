from flask import Flask
import json


app = Flask(__name__)

simu_id_file = open("samples/simu_id.txt", "r")
simu_file = open("samples/simu.json", "r")
simu_data = json.loads(simu_file.read())
simu_id = []
for row in simu_id_file:
    simu_id.append(row.strip())

sime_id_file = open("samples/sime_id.txt", "r")
sime_file = open("samples/sime.json", "r")
sime_data = json.loads(sime_file.read())
sime_id = []
for row in sime_id_file:
    sime_id.append(row.strip())


@app.route("/")
def index():
    output = ""
    output += "<h1>Valid SIMU IDs</h1><br>"
    for id in simu_id:
        output += "<a href=simu/id=" + id + ">" + id + "</a><br>"
    output += "<br><h1>Valid SIME IDs</h1><br>"
    for id in sime_id:
        output += "<a href=sime/id=" + id + ">" + id + "</a><br>"

    return output


@app.route("/simu/id=<id>")
def simu(id):
    return simu_data[str(id)]


@app.route("/sime/id=<id>")
def sime(id):
    return sime_data[str(id)]


app.run()
