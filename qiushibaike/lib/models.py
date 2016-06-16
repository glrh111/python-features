# -*- coding: utf-8 -*- 
from sqlalchemy import func, Column, DateTime, String, Integer\
	, UnicodeText, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker

import os

Base_alchemy = declarative_base()

class Hot(Base_alchemy):
	__tablename__ = 'hots'
	id = Column(Integer, primary_key=True)
	author = Column(UnicodeText)
	content = Column(UnicodeText)
	add_time = Column(DateTime, default=func.now())

basedir = os.path.abspath(os.path.dirname(__file__))

database_uri = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db_engine = create_engine(database_uri, echo=False, \
	convert_unicode=True, encoding='UTF-8')
db_session = sessionmaker(bind=db_engine)

# use session mainly
session = db_session()

Base_alchemy.metadata.create_all(db_engine)

