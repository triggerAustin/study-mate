# study-mate
for the portfolio project for alx foundations

## installation
this setup procedure is gor a linux machine primarily
the first thing is to clone the github repository:

`git clone https://github.com/triggerAustin/study-mate.git`

then:
`cd study-mate`
then you start a virtual env.
download it using `python -m venv venv`
activate it using `source venv/bin/activate`
once you have activated it, your bash prompt should have a preceeding (venv) at the beginning
now it is time to install the requirements for this project

`pip install -r requirements.txt`

after the installation is successful, run `cd api/v1/` and then run `flask run` to start the application
