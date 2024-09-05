# study-mate
for the portfolio project for alx foundations

## installation
this setup procedure is for a linux machine primarily
the first thing is to clone the github repository:

`git clone https://github.com/triggerAustin/study-mate.git`

then:

`cd study-mate`

since the project requires a databse you will first run:
if you don't have mysql installed, [follow this installation guide](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/). You can skip this step if you have mysql installed already.
After installation run this command to set up the mysql server

`cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p` put your mysql password at the prompt.

then you start a virtual env. Download it using:

`python -m venv venv`

activate it using:

`source venv/bin/activate`

Once you have activated it, your bash prompt should have a preceeding (venv) at the beginning. Now it is time to install the requirements for this project. Use:

`pip install -r requirements.txt`

after the installation is successful, run `cd app` and then run `flask run` to start the application.
