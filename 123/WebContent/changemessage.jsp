<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="bootstrap/css/style.css" rel="stylesheet" type="text/css"/>
<script src="http://code.jquery.com/jquery-latest.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<!--[if lt IE 9]>
   <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
   <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
<![endif]-->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<div class="container">
			<div class="row clearfix">
				<div class="col-md-12 column">
					<nav class="navbar navbar-default navbar-static-top">
						<div class="navbar-header">
							<a class="navbar-brand" href="StudentQuery">学生管理系统</a>
						</div>
						<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1" >
							<ul class="nav navbar-nav navbar-right">
								<li>
								<a href="StudentQuery"><span class="glyphicon glyphicon-user"></span>欢迎您！${username}</a>
									
								</li>
								<li>
									 <a href="Logout"><span class="glyphicon glyphicon-log-out"></span>登出</a>
								</li>
							</ul>
						</div>	
					</nav>
					<ul class="nav nav-tabs nav-justified" >
						<li class="active"><a href="StudentQuery">个人信息</a></li>
						<li><a href="/trade">查询成绩</a></li>
					</ul>
					<div class="panel panel-success">
						<div class="recommended-info panel-title">
							<h3 style="margin:10px;">个人信息</h3>
						</div>
						<div class="panel-body ">
						<hr/>
						<div class="row clearfix">
							<div class="col-md-3 column">
								<ul class="nav nav-stacked nav-pills">
									<li class="active">
										 <a href="StudentQuery">个人资料</a>
									</li>
									<li>
										<a href="ChangePassword">修改密码</a>
									</li>	
								</ul>
							</div>
							<div class="col-md-9 column">
							<form action="ChangeStudentMessage" method="POST">
								<dl class="dl-horizontal">
								<dt>学号:</dt>
								<dd>${studentmessage.studentId}<br/><br/></dd>	
								<dt>学院:</dt>
								<dd>${studentclass.academy}<br/><br/></dd>
								<dt>系:</dt>
								<dd>${studentclass.department}<br/><br/></dd>
								<dt>专业:</dt>
								<dd>${studentclass.major}<br/><br/></dd>
								<dt>班级:</dt>
								<dd>${studentclass.class_name}<br/><br/></dd>
								<dt>姓名:</dt>
								<dd><input class="form-control"  name="name" type="text" value="${studentmessage.name}"><br/><br/></dd>
								<dt>性别:</dt>
								<dd><select class="form-control" name="sexy"><option value="男">男</option><option value="女">女</option></select><br/><br/></dd>
								<dt>年龄:</dt>
								<dd><input class="form-control"  name="age" type="text" value="${studentmessage.age}"><br/><br/></dd>
								</dl>
								<button type="submit" class="btn btn-primary ">确认修改</button>
							</form>	
							</div>
						</div>
						</div>
						</div>
				</div>
			</div>
		</div>
</body>
</html>