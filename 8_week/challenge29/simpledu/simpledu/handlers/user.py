from flask import Blueprint, render_template
from ..models import User, Course


user = Blueprint('user', '__name__', url_prefix='/user')
@user.route("/admin")
def index():
	date = User.query.filter_by().all()


	return render_template('user.html', date = date)
