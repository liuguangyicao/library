<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="en">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
<link href="bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css"/>
<link rel="stylesheet" href="bootstrap/font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="boostrap/css-index/form-elements.css">
<link rel="stylesheet" href="bootstrap/css-index/style.css">
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
<!-- Top content -->
        <div class="top-content">
        	
            <div class="inner-bg">
                <div class="container">
                    <div class="row">
                        <div class="col-sm-8 col-sm-offset-2 text">
                            <h1>学生信息管理系统</h1>
                            <div class="description">
                            	<p>
	                            	welcometo学生信息管理系统
                            	</p>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-sm-6 col-sm-offset-3 form-box">
                        	<div class="form-top">
                        		<div class="form-top-left">
                        			<h3>登录</h3>
                            		<p>输入学号和密码登录（初始密码是学号）。</p>
                        		</div>
                        		<div class="form-top-right">
                        			<i class="fa fa-lock"></i>
                        		</div>
                            </div>
                            <div class="form-bottom">
			                    <form role="form" action="UserLogin" method="post" class="login-form">
			                    	<div class="form-group">
			                    		<label class="sr-only" for="form-username">学号</label>
										<input class="form-username form-control" id="form-username" name="username" placeholder="Enter username" type="text" value="">
			                        </div>
			                        <div class="form-group">
			                        	<label class="sr-only" for="form-password">密码</label>
			                        	<input class="form-password form-control" id="form-password" name="password" placeholder="Enter password" type="password" value="">
						
			                        </div>
			                        <button type="submit" class="btn btn-primary">登录</button>
			                    </form>
		                    </div>
                        </div>
                    </div>
			
                </div>
            </div>
            
        </div>
<script src="bootstrap/js-index/jquery-1.11.1.min.js"></script>
        <script src="bootstrap/js/bootstrap.min.js"></script>
        <script src="bootstrap/js-index/jquery.backstretch.min.js"></script>
        <script src="bootstrap/js-index/scripts.js"></script>
</body>
</html>