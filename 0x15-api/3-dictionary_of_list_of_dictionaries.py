#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python script to export
    data in the JSON format.
"""

import requests
from sys import argv
import json


def json_export(employee_id):
    """Function to export data in JSON format"""
    # Fetch employee details
    url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}users".format(url)
    employee_data = requests.get(employee_url).json()
    employee_name = employee_data.get("name")
    user_name = employee_data.get("username")

    # Fetch employee's todos
    todos_url = "{}todos".format(url)
    todos_data = requests.get(todos_url).json()

    # Export in JSON formart
    my_dict = {}
    username_dict = {}

    for info in employee_data:
        user_id = info.get('id')
        my_dict[user_id] = []
        username_dict[user_id] = info.get("username")

    for info in tasks_dict:
        all_tasks = {}
        user_id = info.get("userId")
        all_tasks["task"] = info.get("title")
        all_tasks["completed"] = info.get("completed")
        all_tasks["username"] = username_dict.get(user_id)
        my_dict.get(user_id).append(all_tasks)

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as json_file:
        json.dump(my_dict, json_file)


if __name__ == "__main__":
    json_export(argv[1])
