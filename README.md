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
As a User, I should be able to enter my basic contact details, academic information and team information.

* Feature 002: Create a SQL server
As a Developer, I need to be able to store the user data into a database for easier manipulation.

* Feature 003: Import contact data to a database.
As a Developer, details about any new entry through the forms should automatically populate the database.

* Feature 004: Identify records as part of one team if mentioned in the Google forms.
As a Developer, a unique ID is required to link already formed teams.

EPIC: Algorithm

* Feature 001: Distribute participants into teams in terms of major
As a Developer, I need to form teams comprised on individual sign-ups.

* Feature 002: Distribute participants into teams with mixed team status in terms of major
As a Developer, I need to accommodate if teams have already been formed with individual sign-ups.

* Feature 003: Distribute participants into teams based in terms of year standing
As a Developer, I need to form teams comprised on individual sign-ups.

* Feature 004: Distribute participants into teams with mixed team status in terms of year standing
As a Developer, I need to accommodate if teams have already been formed with individual sign-ups.

* Feature 005: Distribution with two criteria: major and standing
As a Developer, I need to form teams with mixed team and individual standings based on both major and year standing.

* Feature 006: Connect algorithm to SQL database
As a Developer, I need to read participant data from the database.

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
