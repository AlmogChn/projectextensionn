from pymysql import OperationalError
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import db_connector
import sys


db_user = sys.argv[1]
db_password = sys.argv[2]

try:
    res = requests.post('http://127.0.0.1:5000/users/1421', json={"user_name": 'fds'})
    print(res.json())

    res = requests.get('http://127.0.0.1:5000/users/1421', json={"user_name": 'sdf'})
    print(res.json(), 'status code:', res.status_code)
    res_dict = dict(res.json())
    user_name1 = (res_dict['user_name'])

    user_name2 = db_connector.Msql(table='users', user_id=1421)  # Please make sure you enter the new user_id in the test
    if db_connector.Msql.select_name(user_name2) == user_name1:
        print('Ok - Match username(db-backend)')
    else:
        print('Error - Username does not match(db-backend)')

    driver = webdriver.Chrome(executable_path="C:\\Users\אלמוג\\Downloads\\chromedriver_win32\\ChromeDriver.exe")
    driver.implicitly_wait(5)
    driver.get('http:///127.0.0.1:5001/users/1421') # Please make sure you enter the new user_id in the test
    try:
        user_name = driver.find_element(By.ID, value='user')
        print(f'the user name on this id : {user_name.text}')
    except NoSuchElementException:
        no_user = driver.find_element(By.ID, value='error')
        print(no_user.text)

    if db_connector.Msql.select_name(user_name2) == str(user_name.text):
        print('Ok - Match username(db-fronted)')
    else:
        print('Error - Username does not match(db-fronted)')

    driver.quit()
except ValueError or BaseException or OperationalError as error :
    print({'test failed': error})



