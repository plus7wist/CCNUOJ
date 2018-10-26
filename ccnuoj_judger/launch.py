from time import sleep

import requests

from command import execute
from local_config import api_base, token

session = requests.Session()
session.headers.update({"X-CCNU-AUTH-TOKEN": token})

def get_command_id(obj):
    return obj["id"]

def get_judge_command(obj):
    return obj["command"]

def fetch_and_execute():
    instance = session.get(api_base + "/judge_command/unfetched/5").json()

    if instance["status"] != "Success":
        print("Failed")
        print("Reason: %s" % instance["reason"])
        return

    print(instance)

    result = instance["result"]
    for obj in result:
        command_id = get_command_id(obj)
        command = get_judge_command(obj)
        fetch_response = session.post(api_base + "/judge_command/%d/fetched" % command_id).json()
        if fetch_response["status"] != "Success":
            print("Failed to fetch judge command #%d" % command_id)
            print("Reason: %s" % fetch_response["reason"])
        else:
            print("Successfully fetched judge command #%d: %s" % (command_id, command))
            execute(command)

while True:
    try:
        fetch_and_execute()
    except requests.RequestException as e:
        print("Error occurred:")
        print(e)
    sleep(1)
