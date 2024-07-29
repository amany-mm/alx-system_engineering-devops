#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == '__main__':
    EMPLOYEE_ID = argv[1]
    USER_URL = "https://jsonplaceholder.typicode.com/users"
    URL = USER_URL + "/" + EMPLOYEE_ID

    response_user = requests.get(URL)
    EMPLOYEE_NAME = response_user.json().get('name')

    TODO_URL = URL + "/todos"
    response_task = requests.get(TODO_URL)
    tasks = response_task.json()
    TOTAL_NUMBER_OF_TASKS = len(tasks)

    NUMBER_OF_DONE_TASKS = 0
    tasksList = []

    for task in tasks:
        if task.get('completed'):
            tasksList.append(task)
            NUMBER_OF_DONE_TASKS += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    for task in tasksList:
        print("\t {}".format(task.get('title')))
