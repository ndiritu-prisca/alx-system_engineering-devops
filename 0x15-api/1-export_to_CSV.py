#!/usr/bin/python3
"""
    Using what you did in the task #0, extend your Python script to export
    data in the CSV format.
"""

import requests
from sys import argv
import csv


def export_csv(employee_id):
    """Function to export data in CSV format"""
    # Fetch employee details
    url = "https://jsonplaceholder.typicode.com/"
    employee_url = "{}users/{}".format(url, employee_id)
    employee_data = requests.get(employee_url).json()
    employee_name = employee_data.get("name")
    user_name = employee_data.get("username")

    # Fetch employee's todos
    todos_url = "{}todos?userId={}".format(url, employee_id)
    todos_data = requests.get(todos_url).json()

    # Exporting with csv
    file_name = "{}.csv".format(employee_id)

    with open(file_name, mode='w') as csv_file:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([employee_id, user_name,
                            todo.get("completed"), info.get("title")])


if __name__ == "__main__":
    export_csv(int(argv[1]))
