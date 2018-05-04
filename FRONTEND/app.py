from flask import Flask, request,render_template
import operator
import json

import datetime
import dateutil.parser
import requests
app = Flask(__name__)


@app.route('/',  methods=['GET','POST'])
def Transactions():
    Data = list(json.load(open('Logs.json')))
    print(Data)
    Current_date = datetime.date.today()

    '''
    Payload =requests.get('https://api.cebroker.com/v1/cerenewaltransactions/GetLogsRecordData?startdate='+str(Current_date) + '&enddate=' + str(Current_date)
    print(len(Logs.json))
    '''

    Ordered =  sorted(Data, key=lambda k: dateutil.parser.parse(k['dt_Start_Log']))

    return render_template('index.html',Logs=Ordered)



if __name__ == '__main__':
    app.DEBUG=True
    app.run(host="127.0.0.1", port=4444, debug=True)
