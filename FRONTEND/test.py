


import datetime
import dateutil.parser

a=[{'b':"2018-07-31T00:00:00"},{'b':"2018-07-31T00:00:02"},{'b':"2018-07-31T00:00:01"}]
print(sorted(a, key=lambda k: dateutil.parser.parse(k['b'])))
print(a)