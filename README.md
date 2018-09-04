# Template Flask App with 
- User Login (Using Flask Login Manager) with hashed passwords
- Local sqlite db (Using Flask SQLAlchemy)
- Database migrations (Using Flask Migrate)

Before Starting:
1. Install Homebrew
2. Install python3
3. Install pip3

To start: 
1. Clone repo
2. Change git remote URL
$git remote set-url origin git://new.url.here
3. Change root folder name from <flask_app_template> to your project name
2. Create venv in root folder
	in root folder: $ python3 -m venv ./venv
3. Activate venv:
	$ source ./venv/bin/activate
3. Install dependencies 
	$ pip install -r requirements.txt
4. Rename "project_name.py" to <project_name>.py
$ mv project_name.py <project_name>.py
5. Create a local database
$ flask db init
$ flask db migrate
$ flask db upgrade
6. (Optional) set flask environment to Development:
$ export FLASK_ENV=development

6. Run development server 
$ flask run

To Activate/Deactivate venv:
Activate: 
$ source ./bin/activate
Deactivate: 
$ deactivate

Apps made using template:
https://championsleague18-19.herokuapp.com/

Resources used to create this:
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
