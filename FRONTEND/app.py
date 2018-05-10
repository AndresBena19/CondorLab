from flask import Flask, request, render_template
import operator
import json

import datetime
import dateutil.parser
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def Transactions():
    """
    for practical uses the amount of date passed to the view is going to be less than the real,
    because the web browser doesn't support it then exploit.

    """
    Today = datetime.date.today()
    Currentday =datetime.datetime.now().strftime("%m/%d/")+str(Today.year)

    """
       This is done for fast respond os the application
    """
    Payload = requests.get('https://api.cebroker.com/v1/cerenewaltransactions/GetLogsRecordData?enddate=' + str(Currentday) + '&state=FL')

    """
    If you want to retrieve all the record just uncomment next line, and comment the previous
    """
    #Payload = requests.get('https://api.cebroker.com/v1/cerenewaltransactions/GetLogsRecordData?enddate=' + str(Currentday))


    # Here we sort the list of records by date start log
    Ordered = sorted(Payload.json()[:3000], key=lambda k: dateutil.parser.parse(k['dt_Start_Log']))

    return render_template('index.html', Logs=Ordered)


if __name__ == '__main__':

    app.run(host="127.0.0.1", port=4444)
