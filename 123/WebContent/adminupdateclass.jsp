<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link href="bootstrap/css/style_admin.css" rel="stylesheet" type="text/css"/>
<script src="http://code.jquery.com/jquery-latest.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<!--[if lt IE 9]>
   <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
   <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
<![endif]-->
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>admin</title>
</head>
<body>
<div class="container">
	<div class="row clearfix">
		<div class="col-md-12 column">
			<div class="row clearfix">
				<div class="col-md-2 column">
					<ul class="nav nav-stacked nav-pills">
						<li>
						<h3>Administrator</h3>
						</li>
						<li>
							 <a href="AdminQueryMessage">查询详细信息</a>
						</li>
						<li>
							 <a href="AdminQueryClass">查询班级信息</a>
						</li>
						<li>
							 <a href="AdminAddStudent">添加学生资料</a>
						</li>
						<li class = "active">
							 <a href="AdminUpdateClass">课程管理</a>
						</li>
								</ul>
				</div>
				<div class="col-md-8 column">
					 <ul class="breadcrumb">
						<li class = "pull-right">
						 <a href="Logout"><span class="glyphicon glyphicon-log-out"></span>登出</a>
						</li>
					</ul>
					<form action="" method="POST">
						<table>
							<tbody>
								<tr>
									<td>
									课程管理
									<dl class="dl-horizontal">
									<dt>输入学期：</dt>
									<dd><input class="form-control" name="class_term" type="text" ><br/></dd>
									<dt>输入课程名：</dt>
									<dd><input class="form-control" name="class_name" type="text" ><br/></dd>
									<dt>输入专业名：</dt>
									<dd><input class="form-control" name="major" type="text"><br/></dd>
									<dt></dt>
									<dd> <input type="button" value="修改课程" type="submit" class="btn btn-info" onclick="form.action='AdminUpdateClass';form.submit();"/>
									<input type="button" value="添加课程" type="submit" class="btn btn-info" onclick="form.action='AdminAddClass';form.submit();"/>
									<input type="button" value="删除课程" type="submit" class="btn btn-info" onclick="form.action='AdminDeleteClass';form.submit();"/>
									</dd>
									
									</dl>
									</td>
									</tr>
							</tbody>
						</table>
					</form>
					<hr/>
					
				</div>
			</div>
		</div>
	</div>
</div>
			
</body>
</html>