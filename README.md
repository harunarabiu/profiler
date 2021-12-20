## Profiler
An API endpoint to get list of users


### Problem Challenge
To read more about the problem challenge visit https://gist.github.com/scabbiaza/82e9069cfa71c4d7aa9d9539a794a1db

# Before you begin
1. *source bootstraps.sh* then alter to taste, if need be.
2. `Make download` and `Make install` to download & install the necessary libraries.
3. If you encounter errors during the build of uwsgi, blinker, uwsgitop, pyperclip and wrapt, just overlook it.

# Note
1. Ports are quoted here, e.g. 9030. Please note that if you have changed such quoted ports in your `.env` file,
remember to change it to taste where appropriate.

# How to use
1. Type `make` and choose any command that shows afterwards
2. To reload the application run by nginx: type `make livereload`


# To run the application for development
1. type `make bash` to enter the container
2. run `flask run --host 0.0.0.0`

# Bootstrap the application
1. `make routes` displays all the routes so that you can know which one to work with
2. `docker-compose ps` helps you see the running apps and the ports they are serving on
