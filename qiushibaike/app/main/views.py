# -*- coding: utf-8 -*-
from datetime import datetime
from flask import request, render_template, session, redirect, url_for, jsonify
import json
from . import main
from .forms import NameForm
from .. import db
from ..models import Hot

@main.route('/ajax', methods=['GET', 'POST'])
def ajax():
    page = request.args.get('page', 0, type=int) + 1

    # 20 pices a time
    content = Hot.query.filter((page*20)<Hot.id).all()[:20]
    if content != None:
        result = {i.author:i.content for i in content}
    else:
        result = {'No More': u'木有更多了，哭哭哭~~~', 'hengheg': u'还要看！！！', }

    return jsonify(result=json.dumps(result, encoding='utf-8'))

@main.route('/', methods=['GET', 'POST'])
def index():
	content = Hot.query.filter(Hot.content!=None).all()[:20]
	return render_template('index.html', content=content)







	
