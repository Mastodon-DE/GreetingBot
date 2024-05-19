import requests
from mastodon import Mastodon
import tomllib
import logging
import os


PAT = os.environ.get('PAT')
NTFY = os.environ.get('NTFY')
INSTANCE = os.environ.get('INSTANCE')

mastodon = Mastodon(access_token = PAT, api_base_url = INSTANCE)
logging.info("Logged into Mastodon")

resp = requests.get(NTFY, stream=True)
for line in resp.iter_lines():
    if line["event"] == "account.created":
        username = line["object"]["username"]
        print(username)

        mastodon.status_post(f"""## @{username} Willkommen auf Mastodon.de
Schön, dass du dich registriert hast 🥳 
                     
Damit du dich auf Mastodon.de :MastodonDE:​ wohlfühlst kannst du dich jeder Zeit an uns über den @MastodonDE Account wenden.

Solltest du neu auf Mastodon sein kannst du gerne [hier](https://fedi.tips) für hilfreiche Resourcen vorbeischauen. So wird der überwältigende Start auf Mastodon etwas leichter.

Falls du von einer anderen Instanz kommst, findest du [hier](https://mastodon.de/@MastodonDE/111178039788718676) eine kleine Liste an Dingen, die auf MastodonDE anders/neu sein können. Schau dich erstmal um und komme später auf diese Tipps zurück oder frag einfach uns :D

Eine schöne Zeit auf MastodonDE wünscht dir @feuerstein im Namen des MastodonDE Teams.

**[Info]** *Diese Nachricht ist automatisiert 🤖​.
Bei Antwort erreichst du jedoch ein Team Mitglied :D*              
                    """, language="DE", visibility="direct")
    