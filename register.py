from mastodon import Mastodon
import tomllib
import logging

## Register the Application

def parse_toml():
    with open("configuration.toml", "rb") as f:
        global config
        config = tomllib.load(f)
       

def login():
    Mastodon.create_app(
        'MastodonDE-BOT',
        api_base_url = config["instance"],
        to_file = 'mdeb_clientcred.secret'
    )

try:
    parse_toml()
    login()
except Exception:
    logging.error("Config file invalid or inexistent")

