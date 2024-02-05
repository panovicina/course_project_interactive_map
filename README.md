# course_project_interactive_map
Course Project, 3rd year

## Quick start

Create database using dump.sql file.

Create virtual enviroment (optionally):

```
python3 -m venv .venv
source .venv/bin/activate
```

Install requirements:

```
pip3 install -r requirements.txt
```

Make migrations:

```
alembic  upgrade head
```

Run the app:

```
python3 main.py
