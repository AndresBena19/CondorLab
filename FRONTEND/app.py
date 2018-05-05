from flask import Flask, request, render_template
import operator
import json

import datetime
import dateutil.parser
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def Transactions():


    '''
    for practical uses the amount of date passes to the view, gonna be less that real  
    this because the web browser dont support and exploit

    '''

    Today = datetime.date.today()
    Currentday = str(Today.month) + '/' + str(Today.isoweekday()) + '/' + str(Today.year)
    Payload = requests.get('https://api.cebroker.com/v1/cerenewaltransactions/GetLogsRecordData?enddate=' + Currentday)
    # Here we sort the list of records by date start log
    Ordered = sorted(Payload.json()[:3000], key=lambda k: dateutil.parser.parse(k['dt_Start_Log']))

    print(Ordered)
    return render_template('index.html', Logs=Ordered)


if __name__ == '__main__':

    app.run(host="127.0.0.1", port=4444)
