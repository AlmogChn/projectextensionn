import sys
import pymysql
import db_connector
from flask import Flask, request
import os
import signal

app = Flask(__name__)

@app.route('/users/<int:user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':         # get the username from table by user id
        request_data = request.json
        get_name = db_connector.Msql(table='users', user_id=user_id)
        if not db_connector.Msql.check_id(get_name):
            return {"status": "error", "reason": "no such id”"}, 500
        user_name = db_connector.Msql.select_name(get_name)
        return {'user_id': user_id, 'user_name': user_name}, 200

    elif request.method == 'POST':          # post new username to table by user id if id not exists
        request_data = request.json
        user_name = request_data.get('user_name')
        post_id = db_connector.Msql(table='users', user_id=user_id, user_name=user_name)
        if db_connector.Msql.check_id(post_id):
            return {"status": "error", "reason": "id already ex"
                                                 "ists"}, 500
        db_connector.Msql.insert_into(post_id)
        return {"status": "ok", "user_post": user_name}, 200

    elif request.method == 'PUT':           # update username in table by user id
        request_data = request.json
        user_name = request_data.get('user_name')
        update_id = db_connector.Msql(table='users', user_id=user_id, user_name=user_name)
        if not db_connector.Msql.check_id(update_id):
            return {"status": "error", "reason": "no such id”"}, 500
        db_connector.Msql.update_name_from_id(update_id)
        return {"status": "ok", "user_updated": user_name}, 200

    elif request.method == 'DELETE':            # delete user name from table by user id
        request_data = request.json
        del_id = db_connector.Msql(table='users', user_id=user_id)
        if not db_connector.Msql.check_id(del_id):
            return {"status": "error", "reason": "no such id”"}, 500
        user_name = db_connector.Msql.select_name(del_id)
        db_connector.Msql.del_from_id(del_id)
        return {"status": "ok", "user_deleted": user_name}, 200

    else:
        return 'wrong method'

@app.route('/stop_server')
def stop_server():
 os.kill(os.getpid(), signal.CTRL_C_EVENT)
 return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
