from helpers.secret_fetcher import fetch_secret


def do_important_thing():
    fetch_secret()
    print('I am doing something important')