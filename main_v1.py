"""
Digital Ocean API  helper
"""
import configparser
import requests
import pandas as pd


print("Digital Ocean export script \n")

drop = "dropelts"
keys = "ssh_keys"
image = "images"
# auth_header = ""
# headers = {}
# endpt = ""


def read_config():
    """Reading settings.ini"""
    config = configparser.ConfigParser()
    config.read("settings.ini")
    auth_header = config["DEFAULT"]["token"]
    return auth_header


### Function for choosing endpoints
def chf():
    """Menu Function"""
    while True:
        print("####Info section####")
        print(
            """Digital Ocean API endpoints: \n
            1. droplets: https://api.digitalocean.com/v2/droplets
            2. ssh_keys: https://api.digitalocean.com/v2/account/keys
            3. images: https://api.hetzner.cloud/v1/images
            0. Exit\n"""
        )
        choose = int(input("Choose endpoint \n >>"))
        match choose:
            case 1:
                # print("List all", drop ,"\n")
                endpt = "https://api.digitalocean.com/v2/droplets"
                filename = "droplets"
                return invoke(endpt, filename)
            case 2:
                # print("List all",keys,"\n")
                endpt = "https://api.digitalocean.com/v2/account/keys"
                filename = "ssh_keys"
                return invoke(endpt, filename)
            case 3:
                # print("List all", image,"\n")
                endpt = "https://api.digitalocean.com/v2/images"
                filename = "images"
                return invoke(endpt, filename)
            case 0:
                break


### Function for authorization
def auth(auth_header):
    """Generating auth header"""
    headers = {"Authorization": "Bearer none", "Content-Type": "application/json"}
    headers["Authorization"] = str("Bearer") + " " + str(auth_header)
    return headers


def get_data(headers, endpt):
    """Sending HTTP request"""
    data = {}
    json_dict = requests.get(str(endpt), data=data, headers=headers).json()
    return json_dict


def write_output(filename, json_dict):
    """Write=ing output to disk"""
    df = pd.json_normalize(json_dict, record_path=[filename])
    df.to_csv("./" + filename + ".csv")
    chf()


def invoke(endpt, filename):
    """Invoke other functions from menu function"""
    auth_header = read_config()
    headers = auth(auth_header)
    write_output(filename, get_data(headers, endpt))


### Waiting user's input

if __name__ == "__main__":
    chf()
