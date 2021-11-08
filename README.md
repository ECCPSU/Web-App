# Web-App
Web App for handling case competition registration

# Environment setup

Create environment
* cd Web-App
* python3 -m venv venv

Activate environment
* venv/bin/activate

Install flask
* pip install Flask

# Project Plan
The project is divided into three EPICS

EPIC: Input data

* Feature 001: Create a google sheets form

* Feature 002: Import contact data to a SQL server

EPIC: Algorithm

* Feature 001: Distribute participants into teams in terms of major

* Feature 002: Distribute participants into teams based on year standing

* Feature 003: Distribution with two criteria: major and standing

* Feature 004: Connect algorithm to SQL database

EPIC: Deployment

* Research about potential options to host the application.


# Git Commands

Push  a branch to github (send updates to github)
* git push origin [branch]

Pull from origin ( get updates from github)
* git pull origin master

Start a git project
* git init

See your commits
* git log

Make a branch
* make a branch but not move to the branch
    * git branch [branch]
* Make a branch and move to it
    * git checkout -b [branch]

Move to a branch
* git checkout [branch]

Delete a branch
* git branch -d [branch]

Add changes to staging area (the staging area store the files who's changes you want to commit)
* Add all files that have been change
    * git add .
* Add a specific file
    * git add [file]

Commit a branch (only after peer-review)
* git commit -m [message on commit surrounded by quotes]
