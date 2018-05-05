from flask import Flask, request, render_template
import operator
import json

import datetime
import dateutil.parser
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def Transactions():

    Today = datetime.date.today()
    Currentday = str(Today.month) + '/' + str(Today.isoweekday()) + '/' + str(Today.year)


    '''
    for practical uses the request just gonna ser with the FL state parameter and the actual date, that because the web 
    explooit, and sthe filter data range does not work as I expectec
    '''
    Payload = requests.get('https://api.cebroker.com/v1/cerenewaltransactions/GetLogsRecordData?enddate=' + Currentday + '&state=FL' )
    # Here we sort the list of records by date start log
    Ordered = sorted(Payload.json(), key=lambda k: dateutil.parser.parse(k['dt_Start_Log']))
    return render_template('index.html', Logs=Ordered)


if __name__ == '__main__':

    app.run(host="127.0.0.1", port=4444)
