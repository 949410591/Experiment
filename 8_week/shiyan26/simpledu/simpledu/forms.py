from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms.validators import Length, Email, EqualTo, Required


class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3,24)])#第一个是映射的表单字段名字，后面是验证器
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6,24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码',validators=[Required(), Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
