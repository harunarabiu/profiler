import requests
import os
import click
import json
import time
from datetime import datetime
from time import sleep

from flask_migrate import (  # type: ignore
    current,
    downgrade,
    init,
    migrate,
    revision,
    upgrade,
)

from profiler import app, db
from profiler.models.profile import Profile


class Usable(object):
    def __init__(self):
        self.time = datetime.utcfromtimestamp(time.time())
        self.directory = os.path.join(os.getcwd(), "migrations", "versions")

    def message(self):
        return self.time.strftime("%Y_%m_%d")

    def revision_id(self):
        path, dirs, files = next(os.walk(self.directory))
        return str(len([file_ for file_ in files if file_.endswith(".py")]) + 1).zfill(
            6
        )



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
            sleep(18)
    
    print("Seeding completed.")

@app.cli.command("db-init")
def dbi():
    """
    Calls the init()
    :return: None
    """
    init()


@app.cli.command("db-migrate")
def dbm():
    """
    Calls the migrate()
    :return: None
    """
    usable = Usable()
    migrate(message=usable.message(), rev_id=usable.revision_id())


@app.cli.command("db-revision")
def dbr():
    """
    Calls the revision()
    :return: None
    """
    usable = Usable()
    revision(message=usable.message(), rev_id=usable.revision_id())


@app.cli.command("db-upgrade-sql")
def dbu_sql():
    """
    Generate SQL statements but you will personally have to `run` it on your DB
    :return: None
    """
    upgrade(sql=True)


@app.cli.command("db-current")
def db_current():
    """
    Calls the current()
    :return: None
    """
    current()


@app.cli.command("db-upgrade")
def dbu_no_sql():
    """
    Bring the DB up to date with your data models.
    Calls the migrate()
    :return: None
    """
    upgrade()


@app.cli.command("db-downgrade-sql")
def downgrade_sql():
    """
    Generate SQL statements but you will personally have to `run` it on your DB
    :return: None
    """
    downgrade(sql=True)


@app.cli.command("db-downgrade")
def downgrade_no_sql():
    """
    Bring the DB up to date with your data models.
    Calls the downgrade()
    :return: None
    """
    downgrade()
