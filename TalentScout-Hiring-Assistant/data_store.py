import json


def save_candidate(data):

    try:
        with open("candidates.json", "a") as file:
            json.dump(data, file)
            file.write("\n")
    except:
        pass