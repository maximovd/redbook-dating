## Red book dating backend application

Before you start working, you need to create a virtual environment. I use poetry because it's convenient.

All you need to do is install poetry on your computer. To do this, enter the following command:

You can learn more about poetry [here](https://python-poetry.org/docs/basic-usage/)

**Linux:**
> Before installing on linux, make sure that your default version is python version 3 +

```shell script
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
**Windows:**
> In Windows. You only need to install Poetry once. It will automatically pick up the current Python version and use it to create virtualenvs accordingly.

```
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

After installing poetry, all you need to do is go to the project directory and enter:

```shell script
$ poetry install
```
Use this command to create an environment and install all the dependencies required for the project

After installing the necessary dependencies, you need to apply the current migrations to the database. to do this, enter the command in the console:

```shell script
$ python manage.py migrate
```
After successfully applying migrations, you can start working on tasks, good luck to you 🙂
