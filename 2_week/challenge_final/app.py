 #!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template,url_for,redirect,abort
from flask.ext.sqlalchemy import SQLAlchemy
import os.path,os
import json
from datetime import datetime
from pymongo import MongoClient

mdb = MongoClient("127.0.0.1",27017).hanhan

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/hanhan'
db = SQLAlchemy(app)
#json
#tiao zhan 6 
class Files:
	def __init__(self):
		self.filename = []
		self.articles = self.find()
		
	def find(self):
		file_path = {}
		articles = {}
		for i in os.listdir("../files"):
			file_path[i.split(".")[0] ] = os.path.join("../files",i)
		
			self.filename = file_path.keys()

	
		for i in self.filename:
			with open(file_path[i]) as f:
				articles[i]= dict(json.load(f))

		return articles


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	def __init__(self,name):
	
		self.name = name
	
	def __repr__(self):
		return '<Category %r>' %self.name

class File(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id  = db.Column(db.Integer, db.ForeignKey("category.id"))
	category = db.relationship("Category",
		backref = db.backref('files',lazy="dynamic"))
	content = db.Column(db.Text)

	def __init__(self,title,created_time,category,content):

		self.title = title
		self.created_time = created_time
		self.content = content
		self.category = category

	def __repr__(self):
		return '<File %r>' %self.title

	def add_tag(self,tag_name):
		a = mdb.hanhan.find_one({'id': self.category_id})

		if not a:
			mdb.hanhan.insert_one({'id': self.category_id , "tag": [tag_name] })
		else:
			a = a["tag"]
			a.append(tag_name)
			
			mdb.hanhan.update_one({'id': self.category_id },
				{"$set":{'tag':a}})
			
	def remove_tag(self, tag_name):
		mdb.hanhan.delete_one({'tag': tag_name})

	@property
	def tags(self):
		return mdb.hanhan.find_one({'id': self.category_id})['tag']


def a():

	db.create_all() 
	java = Category('Java') 
	python = Category('Python') 
	file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!') 
	file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!') 
	db.session.add(java) 
	db.session.add(python) 

	db.session.add(file1) 
	db.session.add(file2)

	db.session.commit()
	file1.add_tag('tech') 
	file1.add_tag('java') 
	file1.add_tag('linux') 
	file2.add_tag('tech') 
	file2.add_tag('python')


	





db.create_all() 
t = Category.query.all()
f = File.query.all()


@app.route('/')
def index():

	return render_template("index.html",t = t)
@app.errorhandler(404)
def not_found(error):
	return render_template("404.html"),404


@app.route('/files/<file_id>')
def file(file_id):
	c = Category.query.filter_by(name=file_id).first()
	if not c:
		abort(404)
	return render_template("file.html",files = c.files[0])
        
