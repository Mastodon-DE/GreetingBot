from mastodon import Mastodon
import tomllib
import logging

def parse_toml():
    with open("configuration.toml", "rb") as f:
        global config
        config = tomllib.load(f)
       



## Function for looping throught notifications

def greet_cycle():

    users = []
    ids = []

    ## Feching user Accounts

    for i in range(0, len(notification)):
        users.append(notification[i]["account"]["acct"])
        ids.append(notification[i]["id"])

    # Sending welcome message to every user

    for recipient in users:
        mastodon.status_post(f"""## @{recipient} Willkommen auf Mastodon.de
Schön, dass du dich registriert hast 🥳 
                     
Damit du dich auf Mastodon.de :MastodonDE:​ wohlfühlst kannst du dich jeder Zeit an uns über den @MastodonDE Account wenden.

Solltest du neu auf Mastodon sein kannst du gerne [hier](https://fedi.tips) für hilfreiche Resourcen vorbeischauen. So wird der überwältigende Start auf Mastodon etwas leichter.

Falls du von einer anderen Instanz kommst, findest du [hier](https://mastodon.de/@MastodonDE/111178039788718676) eine kleine Liste an Dingen, die auf MastodonDE anders/neu sein können. Schau dich erstmal um und komme später auf diese Tipps zurück oder frag einfach uns :D

Eine schöne Zeit auf MastodonDE wünscht dir @feuerstein im Namen des MastodonDE Teams.

**[Info]** *Diese Nachricht ist automatisiert 🤖​.
Bei Antwort erreichst du jedoch ein Team Mitglied :D*              
                    """, language="DE", visibility="direct")

    # Deleting the old notification (avoids double sending the message to one user)    
    
    for item in ids:
        mastodon.notifications_dismiss(item)





## Running everything


## Exceptions for handling config file errors
try:
    parse_toml()
except (NameError, FileNotFoundError):
    logging.error("Can't read file! Does it exist? Is the toml syntax valid?")


try:
    mastodon = Mastodon(access_token = config["access_token"], api_base_url= config["instance"])
    
except KeyError:
    logging.error("Could not find every necessary config options")
    quit(1)

logging.info("Config file was loaded")

## Fetching the admin.sign_up notification 

notification = mastodon.notifications(types=["admin.sign_up"])

## Processing said notification

greet_cycle()

logging.info("Detected every new sign up notification")