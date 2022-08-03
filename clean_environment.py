import requests
try:
    requests.get('http://127.0.0.1:5000/stop_server')
    requests.get('http://127.0.0.1:5001/stop_server')
except requests.exceptions.RequestException as connection_err:
    print(connection_err)
