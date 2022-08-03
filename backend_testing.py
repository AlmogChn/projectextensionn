import requests
import db_connector

try:
    res = requests.post('http://127.0.0.1:5000/users/86', json={"user_name": 'try'})
    print(res.json())

    res = requests.get('http://127.0.0.1:5000/users/86', json={"user_name": 'try'})
    print(res.json(), 'status code:', res.status_code)
    res_dict = dict(res.json())
    user_name1 = (res_dict['user_name'])

    user_name2 = db_connector.Msql(table='users', user_id=86)           # please make sure you enter the new user id
    if db_connector.Msql.select_name(user_name2) == user_name1:
        print('Ok - Match username')
    else:
        print('Error - Username does not match')

except ValueError as v_error:
    print({"Try again": "id allows only integers", "info": v_error})




