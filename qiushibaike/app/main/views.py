# -*- coding: utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import Hot


@main.route('/', methods=['GET', 'POST'])
def index():
	wcontent = Hot.query.filter(Hot.content!=None).all()
	return render_template('index.html', content=wcontent)







	