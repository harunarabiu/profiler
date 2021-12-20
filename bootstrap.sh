#!/bin/sh

test -d libraries || mkdir -p libraries

printf "This action OVERWRITES any existing .env file\n\nDo you wish to create them (y/n) as ? "

if [ -z "$1" ]; then
  read answer
else
  answer = $1
fi

create_files(){
cat > .env<< EOF

# Redis Details
REDIS_HOST=redis
REDIS_HOST_PORT=6080
REDIS_DB=profileredis


# PostgreSQL details

POSTGRES_DB=profilerdb
POSTGRES_USER=profiler
POSTGRES_PASSWORD=Pass0123
POSTGRES_HOST_PORT=9010
POSTGRES_HOST=profilerpg


# Flask app details
FLASK_ENV=development
FLASK_SKIP_DOTENV=1
FLASK_APP=wsgi.py
FLASK_DEBUG=1
FLASK_RUN_HOST=0.0.0.0

SITE_NAME=profiler
SECRET_KEY=f717a91ba64b29be9ea32ec7580210fabea72e90
PROFILER_STATUS=profiler.config.LiveConfig



SERVER_HOST_PORT=9030
DEV_SERVER_HOST_PORT=9040
SUPERVISOR_HOST_PORT=9050




EOF

printf "\n===\n'.env' has been successfully created\n===\n\n"
}

if [ "$answer" != "${answer#[Yy]}" ] ;then
    create_files
fi