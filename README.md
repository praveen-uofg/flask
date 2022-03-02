
### What is this repository for? ###
This is the base python base repo for any project to kickstart.
There are 2 major components to this:
* Flask App: REST APIs
* Worker: Celery Workers for Async Tasks

### How do I get set up? ###

#### Local 
Create & Activate a Virtual Environment
```commandline
sudo pip install virtualenv
virtualenv ~/Projects/venv/events-env -p python3.8.3
source ~/Projects/venv/events-env/bin/activate
```
Installing Requirements
```commandline
pip install -r requirements.txt
```
Setup Redis (Broker)
```commandline
brew install redis
brew services start redis
```

Start the Flask Application
```commandline
python app/flask_app.py
```

Start Workers
```commandline
celery -A app.worker worker --loglevel=debug
```

#### Local Docker
```commandline
docker-compose -f build
docker-compose up
```

### How to run tests
Install The App as a python package
```commandline
pip install -e .
```

Run the Tests
```commandline
pytest
```

Get the coverage Report
```commandline
coverage run -m pytest
coverage report
```


### Contribution guidelines ###

* Writing tests
    * Ensure that the code coverage is > 90% 
* Code review
    * Create a Feature / Hotfix Branch
    * Start your commit messages with the JIRA Ticket ID
        * [ZOHO-111]: Setting up the unit tests
    * Add 2 Reviewers
* Other guidelines
