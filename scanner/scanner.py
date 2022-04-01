#!/usr/env python3

from sys import exit

from app import App
from util.config import Config
from util.environment import is_linux

if __name__ == "__main__":
    # currently the app doesn't support anything except of linux systems
    if not is_linux():
        print("only linux systems supported")
        exit(0)

    # load app config
    config = Config("config.ini")
    # init app
    app = App(config)

    # load credentials for bruteforce process
    app.load_credentials()
    # check and create folders and files if needed
    app.prepare_environment()
    # start scanning given IPs
    app.scan()
    # start bruteforce process against found IPs
    app.brute()
