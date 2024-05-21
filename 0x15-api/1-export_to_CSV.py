#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests as r
import sys

# Define base URL
BASE_URL = "https://jsonplaceholder.typicode.com/"


# Define a function to get user data
def get_user_data(user_id):
    user = r.get(f"{BASE_URL}users/{user_id}").json()
    username = user.get("username")
    todos = r.get(f"{BASE_URL}todos", params={"userId": user_id}).json()
    return user_id, username, todos


# Define a function to export data to CSV
def export_to_csv(filename, data):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for element in data:
            writer.writerow(element)


if __name__ == "__main__":
    # Get user ID from command line arguments
    user_id = sys.argv[1]

    # Get user data
    user_id, username, todo_data = get_user_data(user_id)

    # Prepare data for CSV export
    csv_data = [[user_id, username, task.get("completed"), task.get(
        "title")] for task in todo_data]

    # Export data to CSV
    export_to_csv(f"{user_id}.csv", csv_data)
