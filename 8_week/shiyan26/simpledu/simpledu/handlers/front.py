from flask import Blueprint, render_template
from ..models import Course
from simpledu.forms import LoginForm, RegisterForm
front = Blueprint('front', __name__ )

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@front.route('/login')
def login():
	return render_template('login.html', form = LoginForm())

@front.route('/register')
def register():
	return render_template('register.html', form = RegisterForm())
