#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python script to export
    data in the JSON format.
"""

import json
import requests
from sys import argv


def json_export():
    """Function to export data in JSON format"""
    # Fetch employee details
    url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}users".format(url)
    employee_data = requests.get(employee_url).json()

    # Fetch employee's todos
    todos_url = "{}todos".format(url)
    todos_data = requests.get(todos_url).json()

    # Export in JSON formart
    my_dict = {}

    for employee in employee_data:
        all_tasks = []
        for info in todos_data:
            task = {
                "task" = info.get("title")
                "completed" = info.get("completed")
                "username" = employee.get("username")
            }
            all_tasks.append(task)
        user_id = employee.get("id")
        my_dict[user_id] = all_tasks

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as json_file:
        json.dump(my_dict, json_file)


if __name__ == "__main__":
    json_export()
