#!/usr/bin/python3
"""Returns task list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    employee_info = requests.get(
        base_url + "users/{}".format(employee_id)
    ).json()
    tasks = requests.get(
        base_url + "todos",
        params={"userId": employee_id}
    ).json()

    completed_tasks = [
        t.get("title") for t in tasks if t.get("completed") is True
    ]
    employee_name = employee_info.get("name")
    num_completed = len(completed_tasks)
    num_tasks = len(tasks)

    print(f"Employee {employee_name} is done with tasks "
          f"({num_completed}/{num_tasks}):")
    [print(f"\t {task}") for task in completed_tasks]
