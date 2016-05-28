# -*- coding: utf-8 -*-
# tutorial from: http://stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/
'''Entry point to all things to avoid circular imports.'''
from app import app, freezer
from views import *
