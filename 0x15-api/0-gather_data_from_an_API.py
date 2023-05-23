#!/usr/bin/python3
"""
    A Python script that, using this REST API, for a given employee ID, returns
    information about his/her TODO list progress.
"""

import requests
from sys import argv


def todo_progress(employee_id):
    """Function to retrieve employee's TODO list progress"""
    # Fetch employee details
    url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}users/{}".format(url, employee_id)
    employee_data = requests.get(employee_url).json()
    employee_name = employee_data.get("name")

    # Fetch employee's todos
    todos_url = "{}todos?userId={}".format(url, employee_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    todos_done_dict = requests.get("{}todos?userId={}&completed=true"
                                   .format(url, employee_id)).json()
    tasks_done = len(todos_done_dict)

    # Display progress
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, tasks_done, total_tasks))
    for todo in todos_done_dict:
        task_title = todo.get("title")
        print("\t {}".format(task_title))


if __name__ == "__main__":
    todo_progress(int(argv[1]))
