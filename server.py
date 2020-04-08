from flask import Flask, render_template, url_for, request , redirect
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template("index.html")


@app.route('/submit_from', methods=['GET'])
def submit_from():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print("++++++++++++++++++++++++++++++++++++")
    print(request.args.get("email"))
    print("++++++++++++++++++++++++++++++++++++")
    if request.method == 'GET':
        fields = [request.args.get("email"), request.args.get("subject"), request.args.get("message")]
        with open(r'./database.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)

        return redirect("/thnkt.html")
    else:
        return 'something went wrong. Try again'


@app.route('/<string:page>')
def home(page="index.html"):
    if (len(page) > 50):
        return render_template("index.html")
    try:
        return render_template(page)
    except:
        print("Page Error")
        # return render_template("index.html")

