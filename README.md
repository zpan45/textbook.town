
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
```
* Students: Mark Cook <mcook62@uwo.ca>, Jeremy Wong <jwong668@uwo.ca>, Nicole Barucha <nbarucha@uwo.ca>, Jingyi Cao <jcao93@uwo.ca>, Philip Kolman <pkolman@uwo.ca>, Abdulla Abdelkader Ouda <aouda6@uwo.ca>, Zhengyang Pan <zpan45@uwo.ca>, Pierce Saly <psaly@uwo.ca>
* Teacher: Ethan Jackson <ejacks42@uwo.ca>
* TA: Jennifer Emily Knull <jknull@uwo.ca>
```


###Install Guide
1. Clone Project to Local Machine

```bash
git clone https://github.com/nelder/elixir
```

2. Install XAMPP to serve Apache webserver. The /webroot folder needs to be served as static content. 
3. Move project into apache webroot or at least ensure webroot folder is served on localhost using apache. 
4. The frontend is now being served.

###Install Flask (Python Backend)
1. Ensure Python3 is installed. 
2. Ensure mySQL is installed. 
3. Create database in mySQL with any name, like textbook_town. 
4. Add pip dependencies (while in Flask-backend folder) `sudo pip3 install -r requirements.txt`
5. Modify api.py in the backend folder with the correct mySQL information (constant DATABASE_LOGIN_STRING)
6. Run database install commands:

```python
nick@Nicks-MacBook-Pro-2:/Applications/XAMPP/xamppfiles/htdocs/elixir/Flask-backend$ python3
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from api import db
>>> db.create_all()
```

7. Quit to exit python3 interactive shell `quit()`
8. Run backend file:

```bash
nick@Nicks-MacBook-Pro-2:/Applications/XAMPP/xamppfiles/htdocs/elixir/Flask-backend$ python3 api.py 
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

9. Load frontent using localhost and apache webserver; rejoice as the website is now functional. We recommend trying: (click login, click register, register, login, add book to sell).

##Project Structure
* /docs [Our Website](https://textbook.town): for required team github page about us and our project.
* /webroot frontend javascript and designs.
* /Flash-backend is the backend logic and API to the frontend. It runs on python and mySQL.
* [Our Team Website](https://textbook.town): for required team github page about us and our project.