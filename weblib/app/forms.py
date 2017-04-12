# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,SelectField,BooleanField,IntegerField,SubmitField,TextAreaField,DecimalField
from wtforms.validators import DataRequired
from flask_uploads import UploadSet, IMAGES,configure_uploads
from app import app
import os 
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

class LoginForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    
class IndexForm(FlaskForm):
    article = StringField('article', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    inputname = StringField('inputname',validators=[DataRequired()])
    inputpassword = StringField('inputpassword',validators=[DataRequired()])
    inputemail = StringField('inputemail',validators=[DataRequired()])
    inputcode = StringField('inputcode',validators=[DataRequired()])
class UserinfoForm(FlaskForm):
    name = StringField('name')
    sexy = SelectField('sexy',validators=[DataRequired()],choices=[(u'男',u'男'),(u'女',u'女')])
    code = StringField('code')
    qq = StringField('qq')
    tele = StringField('tele')
    email = StringField('email')
    introduce =StringField('introduce')
        
class SentForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])

class ImageForm(FlaskForm):
    photo = FileField('image', validators=[
        FileAllowed(images,'Images only!'),FileRequired('file not chosen')])


class RecommendForm(FlaskForm):
    photo = FileField('image', validators=[
        FileAllowed(images,'Images only!'),FileRequired('file not chosen')])
    article = StringField('article', validators=[DataRequired()])
    writer = StringField('writer', validators=[DataRequired()])
    body = TextAreaField('content', validators=[DataRequired()])
    
class ChangepasswordForm(FlaskForm):
    oldpassword = StringField('oldpassword', validators=[DataRequired()])
    newpassword = StringField('newpassword', validators=[DataRequired()])

class TradeForm(FlaskForm):
    trade_type = SelectField('trade_type',validators=[DataRequired()],choices=[('0',u'教科书'),('1',u'图书'),('2',u'程序书'),('3',u'其他')])
    body = TextAreaField('content', validators=[DataRequired()])
    old_pay = DecimalField('old_pay',validators=[DataRequired()])
    new_pay = DecimalField('new_pay',validators=[DataRequired()])
    photo = FileField('image', validators=[
        FileAllowed(images,'Images only!'),FileRequired('file not chosen')])

class MessageForm(FlaskForm):
    body = TextAreaField('body', validators=[DataRequired()])
   
class LocationForm(FlaskForm):
    floor = SelectField('floor',validators=[DataRequired()],choices=[('1',u'1楼'),('2',u'2楼'),('3',u'3楼'),('4',u'4楼'),('5',u'5楼'),('6',u'6楼')])
    elec  = SelectField('elec',validators=[DataRequired()],choices=[('2',u'全部'),('0',u'是'),('1',u'否')])
    water = SelectField('water',validators=[DataRequired()],choices=[('2',u'全部'),('0',u'是'),('1',u'否')])
    sun = SelectField('sun',validators=[DataRequired()],choices=[('2',u'全部'),('0',u'是'),('1',u'否')])
    lift = SelectField('lift',validators=[DataRequired()],choices=[('2',u'全部'),('0',u'是'),('1',u'否')])
class QueryForm(FlaskForm):
    query = StringField('query', validators=[DataRequired()]);

class SortForm(FlaskForm):
    article = StringField('article', validators=[DataRequired()]);
    sort_type = SelectField('floor',validators=[DataRequired()],choices=[('1',u'程序设计类'),('2',u'哲学类'),
                                                                         ('3',u'社会科学类'),('4',u'自然科学类'),('5',u'历史类'),('6',u'综合性图书')])
    sort = SelectField('floor',validators=[DataRequired()],choices=[('1',u'1'),('2',u'2'),('3',u'3'),('4',u'4'),('5',u'5'),
                                                                     ('6',u'6'),('7',u'7'),('8',u'8'),('9',u'9'),('10',u'10')])
class TestForm(FlaskForm):
    test1 = DecimalField('test1',validators=[DataRequired()])
