## Profiler
An API endpoint to get list of users


### Problem Challenge
To read more about the problem challenge visit https://gist.github.com/scabbiaza/82e9069cfa71c4d7aa9d9539a794a1db

# Setup

1. Clone this repository
```bash
git clone this repo
```

2. Generate .env file from `bootstraps.sh` to hold environment variales.
```bash
source bootstraps.sh
```
3. Deploy docker containers using the `docker-compose.yml` and `Dockerfile`.
```bash
docker-compose up --build
```

4. Make database migrations
```bash
make db_upgrade
```
5. Seed demo user profiles to the database
```bash
make seed_profiles
```
6. access the app through
```bash
http://<host_machine_ip>:80
```


# To run the application for development
1. type `make bash` to access the bash terminal of the app container
2. run `flask run --host 0.0.0.0`
3. access the app through `http://127.0.01:9040/api/v1/profiles`



# Bootstrap the application
`make routes` displays all the routes so that you can know which one to work with
`make shell` to access flask shell

`docker-compose ps` helps you see the running apps and the ports they are serving on

`make db_init` initialise database migration.
`make db_migrate` migrate database migrations.


`make bash`  to access the bash terminal of the app container 
`make pgsql_bash`  to access the bash terminal of the database container

`make updates` to make git updates and show branch
`make build` to make git updates and show branch

`make help` display help and other commands.