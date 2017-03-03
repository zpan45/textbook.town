# Project elixir internal API
Written in Python, this API enables us to use mysql for Users, Textbooks, Bids, and Auctions databases.

Also, by implementing [Flask](http://flask.pocoo.org), we now have methods to register, login, verify password, check login status, and upload file.

# Setup and test the API
Make sure you have python3, pip3, virtualenv, mysql installed and running correctly on your machine.

    Incomplete mysql installation will cause trouble.

    After you install mysql, you should have:
        changed the root password;
        got mysql server running on localhost:5000;
        created a new database called elixir;

    You need to change the database password to your own at api.py(22) for this to work.

    Use the following command to check the path for your python3. This will be used to create virtualenv later.
        $ which python3
        /Library/Frameworks/Python.framework/Versions/3.5/bin/python3


Download this project to your machine.

    $ cd ./elixir/Flask-backend/

We need to remake venv:

    $ rm -r venv/
    $ virtualenv -p /Library/Frameworks/Python.framework/Versions/3.5/bin/python3 venv
    (you may neeed to change the path for python3)

Next, we enter virtual environment:

    $ source venv/bin/activate

In venv, install the requirements:

    $ pip3 install -r requirements.txt

In venv, enter python:

    $ python
    Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 08:49:46)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.

In python, initialize our databases:

    >>> from api import db
    >>> db.create_all()

Press Command+D to terminate python. Under vnev,

    $ python api.py
    * Running on http://127.0.0.1:5000/
    * Restarting with reloader

Now we have our API running and we should be able to test it with [Postman](https://www.getpostman.com/).

# elixir

