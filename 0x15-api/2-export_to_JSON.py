#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python script to export
    data in the JSON format.
"""

import requests
from sys import argv
import json


def export_json(employee_id):
    """Function to export data in JSON format"""
    # Fetch employee details
    url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}users/{}".format(url, employee_id)
    employee_data = requests.get(employee_url).json()
    employee_name = employee_data.get("name")
    user_name = employee_data.get("username")

    # Fetch employee's todos
    todos_url = "{}todos?userId={}".format(url, employee_id)
    todos_data = requests.get(todos_url).json()

    # Export in JSON formart
    with open("{}.json".format(employee_id), mode="w") as jsonfile:
        json.dump({employee_id: [{
                  "task": t.get("title"),
                  "completed": t.get("completed"),
                  "username": username
                  } for todo in todos_data]}, jsonfile)


if __name__ == "__main__":
    export_json(int(argv[1]))
