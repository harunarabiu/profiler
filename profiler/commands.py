import requests
import click
import json
from datetime import datetime
from time import sleep

from profiler import app, db
from profiler.models.profile import Profile


@app.cli.command("seedprofiles")
@click.argument("limit")
def seed_profiles(limit):

    limit=int(limit)

    max_limit_per_request = 5000
    if limit < max_limit_per_request:
        max_limit_per_request = limit

    for i in range(0, limit, max_limit_per_request):
        if (limit - i) < max_limit_per_request:
            max_limit_per_request = limit - i

        print(f"fetching {i + max_limit_per_request} of {limit} ....")
        r = requests.get("https://randomuser.me/api/?results="+str(max_limit_per_request))

        if r.status_code == 200:
            data = json.loads(r.content)
            new_profiles = []
            s = db.Session()
            for profile in data['results']:
                
                dob = profile['dob']["date"]
                dob = datetime.fromisoformat(dob[:-1]).date()

                new_profile = {
                    "id": profile["login"]["uuid"],
                    "title": profile['name']['title'],
                    "first_name": profile['name']['first'],
                    "last_name": profile['name']['last'],
                    "dob": dob,
                    "gender": profile['gender'],
                    "email": profile['email'],
                    "phone": profile['phone'],
                    "nationality": profile['nat'],
                }

                new_profiles.append(Profile(**new_profile))
        
            # db.session.add_all(new_profiles)
            db.session.bulk_save_objects(new_profiles)
            db.session.commit()

        else:
            print(f"{r.status_code} - {r.text}")
            i = i - max_limit_per_request

        if (limit - i) < max_limit_per_request:
            max_limit_per_request = limit - i
        else:
            sleep(10)
    
    print("Seeding completed.")

