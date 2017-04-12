# -*- coding:utf-8 -*-  
from app import app
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import login_user, login_required,logout_user
from .forms import LoginForm, ImageForm, IndexForm, UserinfoForm, LocationForm, SortForm
from .forms import RegisterForm, SentForm, images,TestForm, RecommendForm, ChangepasswordForm, TradeForm,MessageForm,QueryForm
from werkzeug import secure_filename
from app import db, models, lm
from datetime import datetime
from sqlalchemy import desc,or_
import os
import math
@lm.user_loader
def load_user(id):
    return models.User.query.get(int(id))
@app.errorhandler(404)
def internal_error(error):
    return '404'
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return '500'

#login
@app.route('/login', methods = ['GET', 'POST'])
@app.route('/', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = form.name.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user, False)
            session['name'] = user.username
            session['user_id'] = user.id
            if user.username != 'admin':
                return redirect(url_for('index'))
            else:
                return redirect(url_for('admin_index'))
        form.name.data = ''
        form.password.data = ''
        flash('name or password is false')
        return redirect(url_for('login'))
    return render_template('log-in.html',form1 = form)

#logout
@app.route('/logout',methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#register
@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = form.inputname.data).first()
        if user is not None:
            flash('user has existed')
            form.inputpassword.data = ''
            return redirect(url_for('register'))
        else:
            i = models.User(username = form.inputname.data,password = form.inputpassword.data)
            db.session.add(i)
            db.session.commit()
            userinfo = models.Userinfo(user_username=form.inputname.data,email=form.inputemail.data,
                                       code=form.inputcode.data)
            db.session.add(userinfo)
            db.session.commit()
            user = models.User.query.filter_by(username=form.inputname.data).first()
            login_user(user, False)
            session['name'] = user.username
            session['user_id'] = user.id
            form.inputname.data = ''
            form.inputpassword.data=''
            form.inputemail.data=''
            form.inputcode.data=''
            return redirect(url_for('index'))
    return render_template('register.html',form=form)
#index
@app.route('/index',methods =['GET','POST'])
@login_required
def index():
    post_num = []
    sent_num = []
    for i in range(5):
        tmp1 = models.Post.query.filter_by(post_type=i).count()
        post_num.append(tmp1)
        tmp2 = models.Sent.query.filter_by(post_type=i).count()
        sent_num.append(tmp2)
    name = session.get('name')
    user = models.User.query.filter_by(username = name).first()
    talk_cnt = user.to.filter_by(view=False).count()
    first_talk = None
    now_talk_to = user.talk.first()
    now_talk_from = user.to.first()
    if now_talk_to != None:
        first_talk = now_talk_to.talk_to
    if now_talk_from != None:
        tmp = models.User.query.get(now_talk_from.talk_from)
        first_talk = tmp.username
    return render_template('index.html',post_num=post_num,sent_num=sent_num,talk_cnt=talk_cnt,first_talk=first_talk)

#index_1
@app.route('/index_1/<int:index_type>',methods =['GET','POST'])
@app.route('/index_1/<int:index_type>/<int:page>',methods = ['GET', 'POST'])
@app.route('/index_1/<int:index_type>/<int:page>/<int:search_type>',methods = ['GET', 'POST'])
@login_required
def index_1(page=1,index_type=0,search_type=1):
    form = IndexForm()
    if search_type == 1:
        content = models.Post.query.filter_by(post_type=index_type).order_by(desc(models.Post.id)).limit(10).offset((page-1)*10)
        content_cnt = models.Post.query.filter_by(post_type = index_type).count()
    elif search_type == 2:
        content = models.Post.query.filter_by(post_type=index_type).order_by(desc(models.Post.post_num)).limit(10).offset((page-1)*10)
        content_cnt = models.Post.query.filter_by(post_type = index_type).count()
    else:
        name = session.get('name')
        view_user = models.User.query.filter_by(username=name).first()
        view_post_id = view_user.post_view.all()
        content = []
        for i in view_post_id:
            tmp_post = models.Post.query.get(i.post_id)
            content.append(tmp_post)
        content_cnt = view_user.post_view.count()        
    post_user_name = []
    for i in content:
        user = models.User.query.filter_by(id = i.user_id).first()
        post_user_name.append(user.username)
    post_time = []
    for i in content:
        tmp_time = str(i.post_time).split('.')
        post_time.append(tmp_time[0].split('-',1)[1])
    
    
    page_cnt = int(math.ceil(content_cnt*1.0/10))
    name = session.get('name')
    user = models.User.query.filter_by(username = name).first()
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = name).first()
        i = models.Post(post_time=datetime.now(),post_article=form.article.data,
                        post_body=form.content.data,user_id=user.id,post_type=index_type)
        db.session.add(i)
        db.session.commit()
        form.article.data=''
        form.content.data=''
        return redirect(url_for('index_1',index_type=index_type, page=page,search_type=search_type))
    return render_template('index_1.html',form = form, page = page,name = name,post_content = content,
                           page_cnt = page_cnt,post_user_name = post_user_name,post_time = post_time,index_type=index_type,search_type=search_type)

#sent
@app.route('/sent/<int:post_id>/<int:post_type>',methods = ['GET','POST'])
@app.route('/sent/<int:post_id>/<int:post_type>/<int:page>',methods = ['GET', 'POST'])
@login_required
def sent(post_id=1,page=1,post_type=0):
    form = SentForm()
    post = models.Post.query.get(post_id)
    name = session.get('name')
    judge_post = models.Post_view.query.filter_by(user_username=name,post_id=post_id).first()
    if judge_post == None:
        view = False
    else:
        view = True
    sent = post.sent_to.limit(10).offset((page-1)*10)
    content_cnt = post.sent_to.count()
    page_cnt = int(math.ceil(content_cnt*1.0/10))
    ###get sent name and image 
    sent_user_name = []
    sent_image_name = []
    for i in sent:
        user = models.User.query.filter_by(id = i.sent_from_id).first()
        sent_user_name.append(user.username)
        sent_userinfo = user.userinfo.first()
        if sent_userinfo.image == False:
            sent_image_name.append('face.gif')
        else:
            sent_image_name.append(sent_userinfo.image_name)
    ###get post user name and image
    if page == 1:
        post_user = models.User.query.filter_by(id = post.user_id).first()
        post_user_name = post_user.username
        post_userinfo = post_user.userinfo.first()
        if post_userinfo.image == False:
            post_image_name = 'face.gif'
        else:
            post_image_name = post_userinfo.image_name
    tmp_1 = str(post.post_time).split('.')
    post_time = tmp_1[0]
    sent_time = []
    for i in sent:
        tmp_2 = str(i.sent_time).split('.')
        sent_time.append(tmp_2[0])
    name = session.get('name')
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = name).first()
        i = models.Sent(sent_body=form.content.data,sent_time=datetime.now(),sent_from_id=user.id,sent_to_id=post.id,post_type=post_type)
        models.Post.query.filter_by(id = post.id).update({models.Post.post_num:post.post_num+1})
        db.session.add(i)
        db.session.commit()
        form.content.data=''
        return redirect(url_for('sent',post_id=post_id,page=page,post_type=post_type))
    return render_template('sent.html',form=form,post=post,sent=sent,page=page,sent_time=sent_time,
                           post_time=post_time,post_user_name=post_user_name,sent_user_name=sent_user_name,
                           post_image_name=post_image_name,sent_image_name=sent_image_name,post_type=post_type,view = view,page_cnt=page_cnt)


#post_view
@app.route('/post_view/<int:post_id>/<int:post_type>/<int:page>',methods = ['GET', 'POST'])
@login_required
def post_view(post_id,post_type,page):
    name = session.get('name')
    post_view = models.Post_view(user_username = name, post_id=post_id)
    db.session.add(post_view)
    db.session.commit()
    return redirect(url_for('sent',post_id=post_id,post_type=post_type,page=page))

#trade
@app.route('/trade', methods=['GET', 'POST'])
@app.route('/trade/<int:page>',methods = ['GET', 'POST'])
@app.route('/trade/<int:page>/<int:trade_type>',methods = ['GET', 'POST'])
@login_required
def trade(page=1,trade_type=1):
    #content
    form = TradeForm()
    name = session.get('name')
    user = models.User.query.filter_by(username=name).first()
    if trade_type == 1:
        all_trade = models.Trade.query.order_by(desc(models.Trade.id)).limit(6).offset((page-1)*6)
    elif trade_type == 2:
        all_trade = models.Trade.query.order_by(desc(models.Trade.view)).limit(6).offset((page-1)*6)
    else:
        all_trade = []
        view_trade = user.trade_view_user.all()
        for i in view_trade:
            tmp = models.Trade.query.get(i.trade_id)
            all_trade.append(tmp)
    trade_time = []
    view = []
    for i in all_trade:
        tmp = str(i.time).split('.')
        trade_time.append(tmp[0])
        tmp = user.trade_view_user.filter_by(trade_id=i.id).first()
        if tmp == None:
            view.append(0)
        else:
            view.append(1)
    #page
    content_cnt = models.Trade.query.count()
    if trade_type == 3:
        content_cnt = user.trade_view_user.count()
    page_cnt = int(math.ceil(content_cnt*1.0/6))
    if form.validate_on_submit():
        time = str(datetime.now())
        image_tmp_name = time[:10]+time[11:13]+time[14:16]+time[17:19]+time[20:-1]+'trade'
        tmp = form.photo.data.filename.split('.')
        image_name = image_tmp_name + '.' + str(tmp[-1])
        filename = images.save(form.photo.data,name=image_tmp_name + '.')
    	trade = models.Trade(trade_type=form.trade_type.data,body=form.body.data,time=datetime.now(),view = 0,user_username = name,
                             old_pay=str(form.old_pay.data),new_pay=str(form.new_pay.data),image_name=image_name)
    	db.session.add(trade)
    	db.session.commit()
    	form.body.data = ''
    	return redirect(url_for('trade'))
    return render_template('trade.html',form = form,all_trade=all_trade,trade_time=trade_time,page=page,trade_type=trade_type,page_cnt=page_cnt,name=name,view=view)

#trade_view
@app.route('/trade_view/<int:trade_id>/<int:page>/<int:trade_type>',methods = ['GET', 'POST'])
@login_required
def trade_view(trade_id = 1,page = 1,trade_type=1):
    name = session.get('name')
    this_trade = models.Trade_view(user_username=name,trade_id=trade_id)
    db.session.add(this_trade)
    trade = models.Trade.query.get(trade_id)
    models.Trade.query.filter_by(id=trade_id).update({models.Trade.view:trade.view+1})
    db.session.commit()
    return redirect(url_for('trade', page=page, trade_type=trade_type))

#delete_trade_view
@app.route('/delete_trade_view/<int:trade_id>/<int:page>/<int:trade_type>',methods = ['GET', 'POST'])
@login_required
def delete_trade_view(trade_id = 1,page = 1,trade_type=1):
    name = session.get('name')
    this_trade = models.Trade_view.query.filter_by(trade_id=trade_id).first()
    db.session.delete(this_trade)
    trade = models.Trade.query.get(trade_id)
    models.Trade.query.filter_by(id=trade_id).update({models.Trade.view:trade.view-1})
    db.session.commit()
    return redirect(url_for('trade', page=page, trade_type=trade_type))

#search
@app.route('/search',methods =['GET','POST'])
@login_required
def search():
    return render_template('search.html')

#location
@app.route('/location',methods =['GET','POST'])
@login_required
def location():
    form = LocationForm()
    form2 = QueryForm()
    if form.validate_on_submit():
        choice = []
        if form.elec.data == '2':
            choice.append([0,1])
        else:
            tmp = int(form.elec.data)
            choice.append([tmp,tmp])
        if form.water.data == '2':
            choice.append([0,1])
        else:
            tmp = int(form.water.data)
            choice.append([tmp,tmp])
        if form.sun.data == '2':
            choice.append([0,1])
        else:
            tmp = int(form.sun.data)
            choice.append([tmp,tmp])
        if form.lift.data == '2':
            choice.append([0,1])
        else:
            tmp = int(form.lift.data)
            choice.append([tmp,tmp])
        location = models.Seat.query.filter(models.Seat.floor==int(form.floor.data),
                                            or_(models.Seat.elec==choice[0][0],models.Seat.elec==choice[0][1]),
                                            or_(models.Seat.water==choice[1][0],models.Seat.water==choice[1][1]),
                                            or_(models.Seat.sun==choice[2][0],models.Seat.sun==choice[2][1]),
                                            or_(models.Seat.lift==choice[3][0],models.Seat.lift==choice[3][1])).all()
        form.floor.data=''
        form.elec.data=''
        form.water.data=''
        form.sun.data=''
        form.lift.data=''
        form2.query.data=''
        return render_template('location.html', form = form, location = location,form2=form2)
    if form2.validate_on_submit():
        num = int(form2.query.data)
        result = models.Seat.query.filter(models.Seat.num==num).first()
        form.floor.data=''
        form.elec.data=''
        form.water.data=''
        form.sun.data=''
        form.lift.data=''
        form2.query.data=''
        return render_template('location.html', form = form, result=result,form2=form2)
    return render_template('location.html', form = form,form2=form2)

#recommend
@app.route('/recommend',methods =['GET','POST'])
@login_required
def recommend():
    recommend = models.Recommend.query.all()
    return render_template('recommend.html', recommend = recommend)

#recommend_add
@app.route('/recommend_add/<int:recommend_id>',methods =['GET','POST'])
@login_required
def recommend_add(recommend_id):
    name = session.get('name') 
    models.Recommend.query.filter_by(id=recommend_id).update({models.Recommend.click:models.Recommend.click+1})
    db.session.commit()
    return redirect(url_for('recommend'))

#otherinfo
@app.route('/otherinfo/<int:user_id>',methods = ['GET','POST'])
@login_required
def otherinfo(user_id):
    name = session.get('name')
    user = models.User.query.filter_by(id = user_id).first()
    u = user.userinfo.first()
    post_cnt = user.posts.count()
    sent_cnt = user.sent_from.count()
    trade_cnt = user.trade.count()
    post_view_cnt = user.post_view.count()
    trade_view_cnt = user.trade_view_user.count()
    u = user.userinfo.first()
    userinfo = [user.username,u.name,u.sexy,u.code,u.qq,u.tele,u.email,u.introduce]
    head = [u'用户名:',u'姓名:',u'性别:',u'学号:',u'QQ:',u'电话:',u'邮箱:',u'个人简介:']
    return render_template('otherinfo.html',userinfo = userinfo, head = head,
                           post_cnt=post_cnt,sent_cnt=sent_cnt,trade_cnt=trade_cnt,post_view_cnt=post_view_cnt,
                           trade_view_cnt=trade_view_cnt,image=u.image,image_name=u.image_name,name=name)
#userinfo
@app.route('/userinfo',methods = ['GET','POST'])
@login_required
def userinfo():
    name = session.get('name')
    user = models.User.query.filter_by(username = name).first()
    u = user.userinfo.first()
    post_cnt = user.posts.count()
    sent_cnt = user.sent_from.count()
    trade_cnt = user.trade.count()
    post_view_cnt = user.post_view.count()
    trade_view_cnt = user.trade_view_user.count()
    u = user.userinfo.first()
    userinfo = [name,u.name,u.sexy,u.code,u.qq,u.tele,u.email,u.introduce]
    head = [u'用户名:',u'姓名:',u'性别:',u'学号:',u'QQ:',u'电话:',u'邮箱:',u'个人简介:']
    return render_template('userinfo.html',userinfo = userinfo, head = head,
                           post_cnt=post_cnt,sent_cnt=sent_cnt,trade_cnt=trade_cnt,post_view_cnt=post_view_cnt,
                           trade_view_cnt=trade_view_cnt,image=u.image,image_name=u.image_name)

#changeinfo 
@app.route('/changeinfo',methods = ['GET', 'POST'])
@login_required
def changeinfo():
    form = UserinfoForm()
    name = session.get('name')
    user = models.User.query.filter_by(username = name).first()
    userinfo = user.userinfo.first()
    if form.validate_on_submit():
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.name:form.name.data})
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.code:form.code.data})
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.qq:form.qq.data})
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.tele:form.tele.data})
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.email:form.email.data})
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.introduce:form.introduce.data})
        models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.sexy:form.sexy.data})
        db.session.commit()
        return redirect(url_for('userinfo'))
    return render_template('changeinfo.html',form = form, userinfo = userinfo)

#changeimage
@app.route('/changeimage', methods=('GET', 'POST'))
@login_required
def changeimage():
    form = ImageForm()
    if form.validate_on_submit():
        name = session.get('name')
        user = models.User.query.filter_by(username = name).first()
        userinfo = user.userinfo.first()
        if userinfo.image == False:
            models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.image:True})
            tmp = form.photo.data.filename.split('.')
            tmp_name = name + '.' + str(tmp[-1])
            models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.image_name:tmp_name})
            db.session.commit()
            filename = images.save(form.photo.data,name=name + '.')
        else:
            #### this can be promoted
            if str(os.getcwd()) == 'c:\weblib':
                os.chdir('app')
                os.chdir('static')
            file_path = userinfo.image_name
            if os.path.exists(file_path) == True:
                os.remove(file_path)
            tmp = form.photo.data.filename.split('.')
            tmp_name = name + '.' + str(tmp[-1])
            models.Userinfo.query.filter_by(user_username = name).update({models.Userinfo.image_name:tmp_name})
            db.session.commit()
            images.save(form.photo.data,None,name= name+'.')
        flash(u'修改成功')
        return redirect(url_for('changeimage'))
    return render_template('changeimage.html', form=form)


#changepassword
@app.route('/changepassword',methods = ['GET', 'POST'])
@login_required
def changepassword():
    form = ChangepasswordForm()
    name = session.get('name')
    if form.validate_on_submit():
        user = models.User.query.filter_by(username = name).first()
        if form.oldpassword.data != user.password:
            flash('old password is wrong')
            return redirect(url_for('changepassword'))
        else:
            models.User.query.filter_by(username = name).update({models.User.password:form.newpassword.data})
            db.session.commit()
            flash('change has done')
            form.oldpassword.data=''
            form.newpassword.data=''
            return redirect(url_for('changepassword'))
    return render_template('changepassword.html',form = form)

#myindex
@app.route('/myindex',methods =['GET','POST'])
@app.route('/myindex/<int:page>',methods = ['GET', 'POST'])
@login_required
def myindex(page=1):
    user_id = session.get('user_id')
    user = models.User.query.get(user_id)
    post = user.posts.limit(10).offset((page-1)*10)
    return render_template('myindex.html',post = post, page = page)


#delete_post
@app.route('/deletepost/<int:post_id>/<int:page>',methods = ['GET', 'POST'])
@login_required
def deletepost(post_id = 1, page = 1):
    post = models.Post.query.filter_by(id = post_id).first()
    sent = post.sent_to.all()
    for i in sent:
        db.session.delete(i)
        db.session.commit()
    post_view = models.Post_view.query.filter_by(post_id=post_id).all()
    for i in post_view:
        db.session.delete(i)
        db.session.commit()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('myindex', page = page))

#mysent
@app.route('/mysent',methods =['GET','POST'])
@app.route('/mysent/<int:page>',methods = ['GET', 'POST'])
@login_required
def mysent(page=1):
    user_id = session.get('user_id')
    user = models.User.query.get(user_id)
    sent = user.sent_from.limit(10).offset((page-1)*10)
    return render_template('mysent.html',sent=sent,page=page)

#delete_sent
@app.route('/deletesent/<int:sent_id>/<int:page>',methods = ['GET', 'POST'])
@login_required
def deletesent(sent_id = 1, page = 1):
    sent = models.Sent.query.filter_by(id = sent_id).first()
    db.session.delete(sent)
    db.session.commit()
    return redirect(url_for('mysent', page = page))

#mytrade
@app.route('/mytrade',methods =['GET','POST'])
@app.route('/mytrade/<int:page>',methods = ['GET', 'POST'])
@login_required
def mytrade(page=1):
    user_id = session.get('user_id')
    user = models.User.query.get(user_id)
    trade = user.trade.limit(10).offset((page-1)*10)
    return render_template('mytrade.html',trade=trade,page=page)

#delete_trade
@app.route('/deletetrade/<int:trade_id>/<int:page>',methods = ['GET', 'POST'])
@login_required
def deletetrade(trade_id = 1, page = 1):
    trade = models.Trade.query.filter_by(id = trade_id).first()
    trade_view = models.Trade_view.query.filter_by(trade_id=trade_id).all()
    for i in trade_view:
        db.session.delete(i)
        db,session.commit()
    db.session.delete(trade)
    db.session.commit()
    return redirect(url_for('mytrade', page = page))

#myview
@app.route('/myview',methods =['GET','POST'])
@login_required
def myview():
    user_id = session.get('user_id')
    user = models.User.query.get(user_id)
    trade_view = user.trade_view_user.all()
    post_view = user.post_view.all()
    post = []
    trade = []
    for i in trade_view:
        tmp_view = models.Trade.query.filter_by(id=i.trade_id).first()
        trade.append(tmp_view)
    for i in post_view:
        tmp_view = models.Post.query.filter_by(id=i.post_id).first()
        post.append(tmp_view)
    return render_template('myview.html',post=post,trade=trade)

#delete_view_post
@app.route('/delete_view_post/<int:post_id>',methods = ['GET', 'POST'])
@login_required
def delete_view_post(post_id):
    name = session.get('name')
    delete_post_view = models.Post_view.query.filter_by(user_username=name,post_id=post_id).first()
    db.session.delete(delete_post_view)
    db.session.commit()
    return redirect(url_for('myview'))

#delete_view_trade
@app.route('/delete_view_trade/<int:trade_id>',methods = ['GET', 'POST'])
@login_required
def delete_view_trade(trade_id):
    name = session.get('name')
    delete_trade_view = models.Trade_view.query.filter_by(user_username=name,trade_id=trade_id).first()
    db.session.delete(delete_trade_view)
    db.session.commit()
    return redirect(url_for('myview'))

#message
@app.route('/message/<string:sent_to>', methods = ['GET', 'POST'])
@login_required
def message(sent_to=''):
    name = session.get('name')
    #find self and sent_to
    talk_from = models.User.query.filter_by(username = name).first()
    talk_to = models.User.query.filter_by(username = sent_to).first()
    #find now talk to and from 
    now_talk_to = talk_from.talk.filter_by(talk_to = sent_to).first()
    now_talk_from = talk_from.to.filter_by(talk_from = talk_to.id).first()
    #find messages
    message_to = []
    message_from = []
    if now_talk_to != None:
        message_to = now_talk_to.talk.all()
    if now_talk_from != None:
        message_from = now_talk_from.talk.all()
        models.Talk.query.filter_by(id = now_talk_from.id).update({models.Talk.view:True})
        db.session.commit()
    message_tmp = []
    if message_to != []:
        for i in message_to:
            tmp = []
            tmp_time = str(i.datetime).split('.')
            tmp.append(tmp_time[0])
            tmp.append(i.body)
            tmp.append(1)
            message_tmp.append(tmp)
    if message_from != []:
        for i in message_from:
            tmp = []
            tmp_time = str(i.datetime).split('.')
            tmp.append(tmp_time[0])
            tmp.append(i.body)
            tmp.append(0)
            message_tmp.append(tmp)
    if message_tmp != []:
        message_tmp.sort(key=lambda message_tmp_tuple:message_tmp_tuple[0])
    other = {}
    other_to = talk_from.talk.filter(models.Talk.talk_to != sent_to).all()
    other_from = talk_from.to.filter(models.Talk.talk_from != talk_to.id).all()
    if other_to != []:
        for i in other_to:
            other[i.talk_to]=True
    if other_from != []:
        for i in other_from:
            tmp = models.User.query.filter_by(id=i.talk_from).first()
            other[tmp.username]=i.view
    form = MessageForm()
    if form.validate_on_submit():
        if message_to == []:
            new_talk = models.Talk(talk_from=talk_from.id,talk_to=sent_to,view=False,datetime=datetime.now())
            db.session.add(new_talk)
            db.session.commit()
        now_talk_to = talk_from.talk.filter_by(talk_to=sent_to).first()
        new_message = models.Message(datetime=datetime.now(),talk_id=now_talk_to.id,body=form.body.data)
        db.session.add(new_message)
        models.Talk.query.filter_by(id = now_talk_to.id).update({models.Talk.view:False})
        models.Talk.query.filter_by(id = now_talk_to.id).update({models.Talk.datetime:datetime.now()})
        db.session.commit()
        return redirect(url_for('message',sent_to=sent_to))
    return render_template('message.html',message=message_tmp,sent_to=sent_to,form=form,name=name,other=other)




#admin_recommend
@app.route('/admin_index', methods = ['GET', 'POST'])
@login_required
def admin_index(reco_name = ""):
    form = RecommendForm()
    recommend = models.Recommend.query.all()
    recommend_cnt = models.Recommend.query.count()
    if form.validate_on_submit():
        #create a file name 
        time = str(datetime.now())
        image_tmp_name = time[:10]+time[11:13]+time[14:16]+time[17:19]+time[20:-1]
        tmp = form.photo.data.filename.split('.')
        image_name = image_tmp_name + '.' + str(tmp[-1])
        recommend = models.Recommend(article=form.article.data,writer=form.writer.data,body=form.body.data,image=image_name,recommend_name=image_name,click=0)
        db.session.add(recommend)
        db.session.commit()
        filename = images.save(form.photo.data,name=image_tmp_name + '.')
        form.article.data =''
        form.writer.data = ''
        form.body.data = ''
        return redirect(url_for('admin_index')) 
    return render_template('admin_recommend.html', form = form,recommend = recommend, recommend_cnt = recommend_cnt)

#admin_index delete recommend
@app.route('/admin_index_delete/<int:recommend_id>', methods = ['GET', 'POST'])
@login_required
def admin_index_delete(recommend_id):
    i = models.Recommend.query.get(recommend_id)
    db.session.delete(i)
    db.session.commit()
    if str(os.getcwd()) == 'c:\weblib':
        os.chdir('app')
        os.chdir('static')     
        file_path = i.image
        if os.path.exists(file_path) == True:
            os.remove(file_path)
    return redirect(url_for('admin_index'))

#admin_index change recommend
@app.route('/admin_index/changerecommend/<string:reco_name>', methods = ['GET', 'POST'])
@login_required
def admin_index_changerecommend(reco_name = ''):
    form = RecommendForm()
    recommend = models.Recommend.query.filter_by(recommend_name = reco_name).first()
    if form.validate_on_submit():
        models.Recommend.query.filter_by(id=recommend.id).update({models.Recommend.article:form.article.data,
                                                                  models.Recommend.writer:form.writer.data,
                                                                  models.Recommend.body:form.body.data})
        form.article.data =''
        form.writer.data =''
        form.body.data=''
        return redirect(url_for('admin_index'))
    return render_template('admin_index_changerecommend.html',form = form,recommend = recommend)

#admin_name_password
@app.route('/admin_name_password', methods = ['GET', 'POST'])
@app.route('/admin_name_password/<int:page>', methods = ['GET', 'POST'])
@login_required
def admin_name_password(page=1):
    content = models.User.query.limit(10).offset((page-1)*10)
    content_cnt = models.User.query.count()
    page_cnt = int(math.ceil(content_cnt*1.0/10))
    post = []
    sent = []
    trade = []
    view = []
    for i in content:
        post.append(i.posts.count())
        sent.append(i.sent_from.count())
        trade.append(i.trade.count())
        view.append(i.trade_view_user.count())
    return render_template('admin_name_password.html',content=content,page=page,page_cnt=page_cnt,post=post,sent=sent,trade=trade,view=view)

#admin_post
@app.route('/admin_post', methods = ['GET', 'POST'])
@app.route('/admin_post/<int:page>', methods = ['GET', 'POST'])
@login_required
def admin_post(page=1):
    content = models.Post.query.limit(10).offset((page-1)*10)
    content_cnt = models.Post.query.count()
    page_cnt = int(math.ceil(content_cnt*1.0/10))
    user = []
    view = []
    for i in content:
        tmp = models.User.query.filter_by(id = i.user_id).first()
        user.append(tmp.username)
        tmp2 = models.Post_view.query.filter_by(post_id=i.id).count()
        view.append(tmp2)
    return render_template('admin_post.html',content=content,page=page,page_cnt=page_cnt,user=user,view=view)


#admin_delete_post
@app.route('/admin_deletepost/<int:post_id>/<int:page>',methods = ['GET', 'POST'])
@login_required
def admin_deletepost(post_id = 1, page = 1):
    post = models.Post.query.filter_by(id = post_id).first()
    sent = post.sent_to.all()
    for i in sent:
        db.session.delete(i)
        db.session.commit()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin_post', page = page))
   

#admin_sent
@app.route('/admin_sent', methods = ['GET', 'POST'])
@app.route('/admin_sent/<int:page>', methods = ['GET', 'POST'])
@login_required
def admin_sent(page=1):
    content = models.Sent.query.limit(10).offset((page-1)*10)
    content_cnt = models.Sent.query.count()
    page_cnt = int(math.ceil(content_cnt*1.0/10))
    post = []
    user = []
    for i in content:
        tmp = models.User.query.filter_by(id = i.sent_from_id).first()
        user.append(tmp.username)
        tmp2 = models.Post.query.filter_by(id = i.sent_to_id).first()
        post.append(tmp2.post_article)
    return render_template('admin_sent.html',content=content,page=page,page_cnt=page_cnt,user=user,post=post)

#admin_sort
@app.route('/admin_sort', methods = ['GET', 'POST'])
@login_required
def admin_sort():
    form = SortForm()
    return render_template('admin_sort.html',form=form)


#admin_trade
@app.route('/admin_trade', methods = ['GET', 'POST'])
@app.route('/admin_trade/<int:page>', methods = ['GET', 'POST'])
@login_required
def admin_trade(page=1):
    content = models.Trade.query.limit(10).offset((page-1)*10)
    content_cnt = models.Trade.query.count()
    page_cnt = int(math.ceil(content_cnt*1.0/10))
    return render_template('admin_trade.html',content=content,page_cnt=page_cnt,page=page)
    

#admin_location
@app.route('/admin_location', methods = ['GET', 'POST'])
@app.route('/admin_location/<int:page>', methods = ['GET', 'POST'])
@login_required
def admin_location(page=1):
    content = models.Seat.query.limit(15).offset((page-1)*10)
    content_cnt = models.Seat.query.count()
    page_cnt = int(math.ceil(content_cnt*1.0/15))
    return render_template('admin_location.html',content=content,page_cnt=page_cnt,page=page)
   
