PROJECT_NAME ?= redbook-dating

all:
		@echo "make run - Run dev server"
		@echo "make test - Run all tests"

run:
		python redbook_dating/manage.py runserver

test:
		python redbook_dating/manage.py test