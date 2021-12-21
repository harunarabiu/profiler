FORMAT="\nID\t{{.ID}}\nIMAGE\t{{.Image}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.RunningFor}}\nSTATUS\t\
{{.Status}}\nPORTS\t{{.Ports}}\nNAMES\t{{.Names}}\n"

ID_NAME="ID\t{{.ID}}\nNAMES\t{{.Names}}\n"
PROFILER_APP = docker exec -it profiler_app


# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: profiler Makefile help
# help:


.PHONY: help
# help: help				- Please use "make <target>" where <target> is one of
help:
	@grep "^# help\:" Makefile | sed 's/\# help\: //' | sed 's/\# help\://'


.PHONY: clean
# help: clean 				- to make the work directories clean of unwanted files
clean:
	@find . -iname '*.pyc' -delete; find . -iname '.DS_Store' -delete
	@find . -name '__pycache__' -type d -print0 | xargs -0 /bin/rm -rf '{}'


.PHONY: freeze
# help: freeze				- freeze listed Python libraries
freeze:
	@pip freeze | egrep -i "requests|cryptography|wtforms|whoosh|flask-migrate|\
	psycopg2-binary|uwsgitop|flask-login|flask-wtf|blinker|passlib|webtest|\
	python-dotenv|coverage|ua-parser" > requirements.txt


.PHONY: livereload
# help: livereload			- live reload uwsgi
livereload:
	@$(PROFILER_APP) touch wsgi.py


.PHONY: bash
# help: bash				- to make bash for the docker environment
bash:
	@$(PROFILER_APP) bash


.PHONY: stats
# help: stats				- show live uwsgi statistics
stats:
	@uwsgitop http://127.0.0.1:9030/stats


.PHONY: logs
# help: logs				- Run individual log of a container (see inside Makefile for sample)
logs:
	@# make log c=monitaur-core_api-redis_1
	@# docker-compose logs  --timestamps --follow
	@$(if $(c),docker logs --timestamps --follow $(c),$(value LIST_CONTAINERS))


.PHONY: stop
# help: stop				- stops docker
stop:
	@docker-compose stop


.PHONY: cls
# help: cls				- to clear the screen
cls:
	@printf "\033c"  # clear the screen


.PHONY: rmi
# help: rmi				- to remove the image with a specified id or id(s. See Makefile for example(s)
rmi:
	@# make rmi id=4152a9608752; make rmi id="1ea5b921a459 07ee12a5eb2a"
	@docker rmi $(id); make cls
	@docker images


.PHONY: tail
# help: tail				- to tail the profiler_app container
tail:
	@docker logs profiler_app --timestamps --follow


.PHONY: dpa
# help: dpa				- to run docker ps -a
dpa:
	@docker-compose ps
	@docker ps -a --format $(FORMAT)

.PHONY: listids
# help: listids				- list all container ids. You can substitute any of them to `make ipdoc id=CONTAINER_ID`
listids:
	@docker ps -a --format $(ID_NAME)


.PHONY: ipdoc
# help: ipdoc				- get the ip of a container. See Makefile for example(s)
ipdoc:
	@# make ipdoc id=4152a9608752
	@docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(id)


.PHONY: routes
# help: routes				- displays the application's routes
routes:
	@$(PROFILER_APP) flask routes


.PHONY: shell
# help: shell				- displays the application's shell
shell:
	@$(PROFILER_APP) flask shell


.PHONY: db_init
# help: db_init				- to make a development migration init
db_init:
	@$(PROFILER_APP) flask db-init


.PHONY: db_migrate
# help: db_migrate			- to make a development migration migrate
db_migrate:
	@$(PROFILER_APP) flask db-migrate


.PHONY: db_revision
# help: db_revision				- to make a development migration revision
db_revision:
	@$(PROFILER_APP) flask db-revision


.PHONY: db_upgrade_sql
# help: dbu_sql				- to make a development migration upgrade, showing the sql
db_upgrade_sql:
	@$(PROFILER_APP) flask db-upgrade-sql


.PHONY: db_upgrade
# help: db_upgrade			- to make a development migration upgrade, not showing the sql
db_upgrade:
	@$(PROFILER_APP) flask db-upgrade


.PHONY: db_downgrade_sql
# help: db_downgrade				- to make a development migration downgrade, showing the sql
db_downgrade_sql:
	@$(PROFILER_APP) flask db-downgrade-sql


.PHONY: db_downgrade
# help: db_downgrade			- to make a development migration downgrade, not showing the sql
db_downgrade:
	@$(PROFILER_APP) flask db-downgrade


.PHONY: db_current
# help: db_current				- shows the current migration
db_current:
	@$(PROFILER_APP) flask db-current
	@#docker-compose run --rm serve flask db-current


.PHONY: seed_profiles
# help: seed_profiles	        - seed database with 100,000 random profiles fetch from  https://randomuser.me/
seed_profiles:
	@$(PROFILER_APP) flask seedprofiles 100000


.PHONY: updates
# help: updates				- to make git updates and show branch
updates:
	@git fetch && git merge origin/master; echo; git branch; echo
	@echo "git branch -D "


.PHONY: config
# help: config				- displays the docker configuration
config:
	@docker-compose config


.PHONY: ps
# help: ps				- runs the docker ps command
ps:
	@docker-compose ps


.PHONY: test
# help: test				- run tests
test:
	@docker-compose run --rm serve python -m unittest discover -s tests


.PHONY: pgsql_bash
# help: pgsql_bash			- PostgreSQL bash
pgsql_bash:
	@echo 'psql "postgresql://postgres:Pass0123@profilerpg:5432" -c "SHOW data_directory;"'
	@echo 'psql "postgresql://profiler:Pass0123@profilerpg:5432/profilerdb" -c "SHOW data_directory;"'
	@docker exec -it profiler_psql bash

.PHONY: download
# help: download			- Download libraries
download:
	@$(value DOWNLOAD_LIBS)


.PHONY: install
# help: install				- Install libraries
install:
	@$(value INSTALL_LIBS)


.PHONY: build
# help: build				- to make build and then detach from the docker environment
build:
	@# docker pull python postgres redis

	@# clean up libraries
	@rm -rf libraries

	@# copy over libraries
	@cp -r ~/buildapps/profiler-libraries/ libraries/

	@# build the library
	@docker-compose up --build -d; docker-compose ps

	@# clean up libraries
	@rm -rf libraries


define LIST_CONTAINERS =
docker ps | grep profiler | awk '{ print $NF }'
endef




define DOWNLOAD_LIBS =
# create missing directories and virtual env
test -d ~/buildapps/profiler-libraries || mkdir -p ~/buildapps/profiler-libraries
test -d ~/buildapps/profiler-libraries/.venv/profiler || python3 -m venv ~/buildapps/profiler-libraries/.venv/profiler

. ~/buildapps/profiler-libraries/.venv/profiler/bin/activate && find . -type f -name 'requiremen*.txt' \
	-exec bash -c 'FILE="$1"; echo -e "\n\n${FILE}"; pip download --dest=~/buildapps/profiler-libraries\
	--disable-pip-version-check --no-cache-dir -r "${FILE}" ' _ '{}' \;
endef


define INSTALL_LIBS =
# activate the environment and download the library
eval ". ~/buildapps/profiler-libraries/.venv/profiler/bin/activate" \
	&& find . -type f -name 'requirement*.txt' \
	-exec bash -c 'FILE="$1"; echo -e "\n\n${FILE}"; pip install --no-build-isolation --no-index --no-cache-dir \
	--disable-pip-version-check --find-links=~/buildapps/profiler-libraries -r "${FILE}"' _ '{}' \;
endef