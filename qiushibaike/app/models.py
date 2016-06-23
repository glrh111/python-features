# -*- coding: utf-8 -*-
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin, AnonymousUserMixin
# from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime


class Hot(db.Model):
	__tablename__ = 'hots'
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.UnicodeText)
	content = db.Column(db.UnicodeText)
	add_time = db.Column(db.DateTime, default=db.func.now())

