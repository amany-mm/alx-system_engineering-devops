#!/usr/bin/python3
"""
A Python script that, using this REST API, returns
all information all users' TODO list progress
and export data in the JSON format.
"""

import json
import requests


if __name__ == '__main__':
    USER_URL = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(USER_URL)
    users = response.json()

    dic = {}
    for user in users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')

        URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        TODO_URL = URL + '/todos/'

        response = requests.get(TODO_URL)
        tasks = response.json()
        dic[USER_ID] = []

        for task in tasks:
            dic[USER_ID].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": USERNAME
            })

    with open('todo_all_employees.json', 'w', encoding='UTF-8') as f:
        json.dump(dic, f)
