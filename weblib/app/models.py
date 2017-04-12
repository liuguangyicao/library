from app import db
from datetime import datetime
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(md5(db.String(64)), index = True)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)  # python 2
    def __repr__(self):
        return '<User %r>' %(self.username)
    ##repr used to debug


   

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    post_time = db.Column(db.DateTime)
    post_article = db.Column(db.UnicodeText(50))
    post_body = db.Column(db.UnicodeText(280))
    post_type = db.Column(db.Integer, index = True)
    post_num = db.Column(db.Integer, default = 0)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('posts', lazy='dynamic'))

class Post_view(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_username = db.Column(db.String(64),db.ForeignKey('user.username'))
    user = db.relationship('User', backref=db.backref('post_view', lazy='dynamic'))
    post_id = db.Column(db.Integer)
    
class Sent(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    sent_body = db.Column(db.UnicodeText(280))
    sent_time = db.Column(db.DateTime)
    sent_from_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('sent_from', lazy='dynamic'))
    sent_to_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    post = db.relationship('Post', backref=db.backref('sent_to', lazy='dynamic'))
    post_type = db.Column(db.Integer, index=True)
   
class Userinfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.UnicodeText(16),default = u'')
    sexy = db.Column(db.UnicodeText(4),default = u'')
    code = db.Column(db.String(15),default = '')
    qq = db.Column(db.String(15),default = '')
    tele = db.Column(db.String(15),default = '')
    email = db.Column(db.String(40),default = '')
    introduce = db.Column(db.UnicodeText(120),default = u'')
    image = db.Column(db.Boolean, default = False)
    image_name = db.Column(db.String(20))
    user_username = db.Column(db.String(64),db.ForeignKey('user.username'))
    user = db.relationship('User', backref=db.backref('userinfo', lazy='dynamic', uselist = 'False'))

class Recommend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    article = db.Column(db.UnicodeText(20), default = u'')
    writer = db.Column(db.UnicodeText(20), default = u'')
    body = db.Column(db.UnicodeText(120), default = u'')
    image = db.Column(db.String(30), default = '')
    recommend_name = db.Column(db.String(30), index = True, default = '')
    click = db.Column(db.Integer, index = True)
    
class Trade(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    trade_type = db.Column(db.String(5), index = True)
    body = db.Column(db.UnicodeText(120), default = u'')
    time = db.Column(db.DateTime)
    view = db.Column(db.Integer, index = True)
    image_name = db.Column(db.String(30))
    user_username = db.Column(db.String(64),db.ForeignKey('user.username'))
    user = db.relationship('User', backref=db.backref('trade', lazy='dynamic'))
    old_pay = db.Column(db.String(10), index = True)
    new_pay = db.Column(db.String(10), index = True)

class Trade_view(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_username = db.Column(db.String(64),db.ForeignKey('user.username'),index=True)
    user = db.relationship('User',primaryjoin='User.username==Trade_view.user_username' ,backref=db.backref('trade_view_user', lazy='dynamic'))
    trade_id = db.Column(db.Integer)

    
class Talk(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    talk_from = db.Column(db.Integer,db.ForeignKey('user.id'),index=True)
    user = db.relationship('User',primaryjoin='User.id==Talk.talk_from', backref=db.backref('talk', lazy='dynamic'))
    talk_to = db.Column(db.String(64),db.ForeignKey('user.username'),index=True)
    user_2 = db.relationship('User',primaryjoin='User.username==Talk.talk_to',backref=db.backref('to', lazy='dynamic'))
    view = db.Column(db.Boolean, default = False)
    datetime = db.Column(db.DateTime)
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    datetime = db.Column(db.DateTime)
    talk_id = db.Column(db.Integer,db.ForeignKey('talk.id'),index=True)
    talk = db.relationship('Talk', backref=db.backref('talk', lazy='dynamic'))
    body = db.Column(db.UnicodeText(80), default = u'')

class Seat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    num = db.Column(db.Integer, index = True)
    floor= db.Column(db.Integer, index = True)
    elec = db.Column(db.Integer, index = True)
    water= db.Column(db.Integer, index = True)
    sun = db.Column(db.Integer, index = True)
    lift= db.Column(db.Integer, index = True)

