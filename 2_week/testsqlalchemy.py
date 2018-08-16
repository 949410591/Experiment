from sqlalchemy import create_engine
engine = create_engine('mysql://root:@localhost/hanhan')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String ,Text, table
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker


class User(Base): 
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	name = Column(String(10))
	email = Column(String(30))
	def __repr__(self):
		return "<User(name=%s)>" % self.name

class Course(Base): 
	__tablename__ = 'course' 
	id = Column(Integer, primary_key=True) 
	name = Column(String(10)) 
	teacher_id = Column(Integer, ForeignKey('user.id')) 
	teacher = relationship('User',backref = "course") 
	def __repr__(self):
		return '<Course(name=%s)>' % self.name

class Lab(Base):

 	__tablename__ = 'lab'
 	id = Column(Integer, primary_key=True)  
 	name = Column(String(64)) 
 	course_id = Column(Integer, ForeignKey('course.id')) 
 	course = relationship('Course', backref='labs') 
 	def __repr__(self): 
 		return '<Lab(name=%s)>' % self.name

class UserInfo(Base):
 	__tablename__ = 'userinfo'
 	user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
 	addr = Column(String(512))
 	use = relationship("User", backref= "info")
 	def __repr__(self):
 		return '<UserInfo (name=%s)>' % self.addr
course_tag = Table('course_tag', Base.metadata, 
		Column('course_id', ForeignKey('course.id'), Primary_key=True),
		Column('Tag_id', ForeignKey('tag.id'),primary_key=True)
	)

class Tag(Base):

 	__tablename__ = 'Tag'
 	id = Column(Integer, primary_key=True)  
 	name = Column(String(64)) 
 	course = relationship('course',)
 	def __repr__(self): 
 		return '<Tag (name=%s)>' % self.name



Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)()


def add_use():
	u1 = User(name='hanhan',email = '949410591@qq.com')
	u2 = User(name='pipi',email = '1051695067@qq.com')
	session.add(u1)
	session.add(u2)
	session.commit()
def add_userinfo():
	u1 = UserInfo(addr = "hanhanjie" ,user_id = user.id)

	session.add(u1)

	session.commit()


def add_course():
	c1 = Course(name='python3',teacher = user)
	c2 = Course(name='java2',teacher_id = user.id)
	session.add(c1)
	session.add(c2)
	session.commit()


def add_lab():

	c1 = Lab(name='1',course_id = course.id)
	c2 = Lab(name='2',course = course)
	session.add(c1)
	session.add(c2)
	session.commit()



user = session.query(User).first()

course = session.query(Course).first()

lab= session.query(Lab).first()
u2 = session.query(User).filter(User.id== 2).all()[0]
info = session.query(UserInfo).all()







	

