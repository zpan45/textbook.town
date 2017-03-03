#Project Elixir
CS2212 Software Engineering Team 4

##Meet the Team:
* Nicole Barucha
* Luna Cao  
* Mark Cook 
* Nicholas Elder (nelder)
* Philip Kolman
* Abdulla Abdelkader Ouda
* Zhengyang Pan
* Pierce Saly
* Jeremy Wong
* TA: Jennie
* Professor: Ethan

##Useful Links:
* [Google Drive](https://drive.google.com/drive/u/0/folders/0B33lPR-1w35LU0pGaEViNVBPNnM): For meeting minutes, some static design assets, planning, etc.
* [Discord](https://discord.gg/sty82bT): Drop in to voice chat room while you are working on the project. Text chat channels also avalible.
* [Facebook Messenger](https://www.messenger.com/t/1520017064690069): For non development specific discussion of things like logistics.
* [Github Repository](https://github.com/nelder/elixir): Project collaboration and storage tool.
* [Trello](https://trello.com/b/3cZF8Gg7/elixir-cs2212-project): Project feature progress tracking. *Note we could change to github projects if we test it and deem it just as good.*

##Email List:
* Students: Mark Cook <mcook62@uwo.ca>, Jeremy Wong <jwong668@uwo.ca>, Nicole Barucha <nbarucha@uwo.ca>, Jingyi Cao <jcao93@uwo.ca>, Philip Kolman <pkolman@uwo.ca>, Abdulla Abdelkader Ouda <aouda6@uwo.ca>, Zhengyang Pan <zpan45@uwo.ca>, Pierce Saly <psaly@uwo.ca>
* Teacher: Ethan Jackson <ejacks42@uwo.ca>
* TA: Jennifer Emily Knull <jknull@uwo.ca>

##Working on Project
###Getting Started
*Will be expanded when we learn GRAILS*
1. Clone Project to Local Machine
```bash
git clone https://github.com/nelder/elixir
```
2. Install GRAILS 
3. Start Webserver

###Working on a New Feature
1. Something about branching to come. 

###Merging New Tested Feature into Main 
1. Something about merge requests to come.

##Project Structure
* [Our Website](https://nelder.github.io/elixir/): for required team github page about us and our project.

##Stage 2
### Project elixir internal API
Written in Python, this API enables us to use mysql for Users, Textbooks, Bids, and Auctions databases.

Also, by implementing [Flask](http://flask.pocoo.org), we now have methods to register, login, verify password, check login status, and upload file.

### Setup and test the API
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

### elixir
