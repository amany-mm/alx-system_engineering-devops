#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress and
export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    EMPLOYEE_ID = argv[1]
    USER_URL = "https://jsonplaceholder.typicode.com/users"
    URL = USER_URL + "/" + EMPLOYEE_ID

    response = requests.get(URL)
    USERNAME = response.json().get('username')

    TODO_URL = URL + "/todos"
    response = requests.get(TODO_URL)
    tasks = response.json()

    dic = {EMPLOYEE_ID: []}
    for task in tasks:
        dic[EMPLOYEE_ID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": USERNAME
        })

    with open('{}.json'.format(EMPLOYEE_ID), 'w', encoding='UTF-8') as f:
        json.dump(dic, f)
