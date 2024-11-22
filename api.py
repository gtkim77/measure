from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
import numpy as np
import json
from datetime import datetime
import gpib
import time

app = Flask(__name__)
api = Api(app)

class nanovoltmeter_2182A:
    def __init__(self, address):
        self.address = address
        self.con = gpib.dev(0, address)

    def fetch(self):
        gpib.write(self.con, ':FETC?\n')
        time.sleep(0.1)
        output = gpib.read(self.con,16).decode('ascii')
        time.sleep(0.1)
        return float(output)

    def read(self):
        gpib.write(self.con, ':READ?\n')
        time.sleep(0.1)
        output = gpib.read(self.con,16).decode('ascii')
        return float(output)

    def write_read(self, command):
        gpib.write(self.con,command)
        time.sleep(0.1)
        output = gpib.read(self.con,16).decode('ascii')
        return float(output)


class base_get(Resource):
  def get(self):
    try:
      volt = nanovoltmeter_2182A(7)
      return volt.write_read(':FETC?\n')
    except Exception as e:
      return {'error': str(e)}

api.add_resource(base_get, '/')

class param_get(Resource):
  def get(self):
    try:
      command = request.args.get('comm')
      volt = nanovoltmeter_2182A(7)
      return volt.write_read('%s\n' % command)
    except Exception as e:
      return {'error': str(e)}

api.add_resource(param_get, '/wr')

class base_post(Resource):
  def post(self):
    try:
      parser = reqparse.RequestParser()
      parser.add_argument('data', action='append')
      args = parser.parse_args()
      _data = args['data']
      print(_data)
      return {'data': args['data']}
    except Exception as e:
      return {'error': str(e) }

api.add_resource(base_post, '/')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=False)

#if __name__ == '__main__':
#  app.run()
