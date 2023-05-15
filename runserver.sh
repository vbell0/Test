#!/bin/bash
source /home/ubuntu/repos/template-django/venv/bin/activate
pip install -r requirements.txt
nohup python /home/ubuntu/repos/template-django/manage.py runserver 0:8000 
deactivate
