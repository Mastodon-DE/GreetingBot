# GreetingBot

A little bot sending a friendly greeting message to every user signing up on a mastodon instance.



**Please note:** This bot relies an the mastodon admin.sign_up permission, which needs to be visible to the account running the bot


## Setup (Docker)

1. Copy the Docker-Compose file into an empty directory for your bot

2. Create the data directory inside it and put the completed configuration.toml file here

3. Run `docker-compose up -d`

## Setup

1. Fill out the `configuration.toml` file

2. Run `python3 register.py` for the setup once

3. Run `python3 main.py`
