package dao;
import java.sql.ResultSet;
import java.sql.SQLException;
import bean.Register;
import bean.StudentClass;
import bean.StudentMessage;
import bean.StudentLesson;
import bean.AdminClass;
import utils.DBconn;
import java.util.*;
public class StudentDao {
	public StudentMessage queryStudentMessage(String username)  {
		String sql = "SELECT * FROM student_message WHERE student_id = '" + username + "';";
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		StudentMessage studentmessage = new StudentMessage();
		rst = dbconn.doSelect(sql);
		try {
			if(rst.next()) {
				studentmessage.setAge(rst.getString("age"));
				studentmessage.setName(rst.getString("name"));
				studentmessage.setStudentId(rst.getString("student_id"));
				studentmessage.setSexy(rst.getString("sexy"));
			} else {
				String sqlcreate = "INSERT INTO student_message(student_id) VALUES ('"+username+"');";
				dbconn.doInsert(sqlcreate);
				studentmessage.setAge("");
				studentmessage.setName("");
				studentmessage.setStudentId(username);
				studentmessage.setSexy("0");
			}
		} catch(SQLException ex) {	
		}
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
		return studentmessage;
	}
	public void updateStudentMessage(StudentMessage studentmessage)  {
		String sql = "UPDATE student_message SET name = '" + studentmessage.getName() + "',age = "
	+ studentmessage.getAge()+",sexy =" + studentmessage.getSexy() + " WHERE student_id = '"+studentmessage.getStudentId()+"';";
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		dbconn.doInsert(sql);
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
	}
	public void updatePassword(Register student)  {
		String sql = "UPDATE student_username_password SET password = '" + student.getPassword() + "' WHERE student_id = '" 
	+ student.getUsername()+"';";
		//System.out.println(sql);
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		dbconn.doInsert(sql);
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
	}
	public StudentClass queryStudentClass(String username)  {
		String sql = "SELECT * FROM student_class WHERE student_id = '" + username + "';";
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		StudentClass studentclass = new StudentClass();
		rst = dbconn.doSelect(sql);
		try {
			if(rst.next()) {
				studentclass.setStudent_id(rst.getString("student_id"));
				studentclass.setAcademy(rst.getString("academy"));
				studentclass.setDepartment(rst.getString("department"));
				studentclass.setMajor(rst.getString("major"));
				studentclass.setClass_name(rst.getString("major")+rst.getString("grade")+rst.getString("class_id"));
			}
		} catch(SQLException ex) {	
		}
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
		return studentclass;
	}
	public String queryStudentScore(StudentLesson studentlesson)  {
		String sql = "SELECT class_score FROM class_score join class_name on class_score.student_class_id = class_name.id WHERE class_score.student_id = '" + studentlesson.getStudent_id() 
		+ "' and class_name.class_term = "+studentlesson.getClass_term() + " and class_name.class_name = '"+studentlesson.getClass_name()+"';";
		System.out.println(sql);
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		String score = "";
		rst = dbconn.doSelect(sql);
		try {
			if(rst.next()) {
				score = rst.getString("class_score");
			}
		} catch(SQLException ex) {	
		}
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
		return score;
	}
	public List<StudentClass> adminQueryClass(AdminClass adminclass)  {
		String sql = "SELECT * FROM student_class WHERE major= '" + adminclass.getMajor() + "'and class_id='"+adminclass.getClass_id()+"'and grade='"
	+adminclass.getGrade()+"';";
		System.out.println(sql);
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		List<StudentClass> studentclass = new ArrayList<StudentClass>( );
		rst = dbconn.doSelect(sql);
		try {
			while(rst.next()) {
				StudentClass tmp = new StudentClass();
				tmp.setStudent_id(rst.getString("student_id"));
				tmp.setAcademy(rst.getString("academy"));
				tmp.setDepartment(rst.getString("department"));
				tmp.setMajor(rst.getString("major"));
				tmp.setClass_name(rst.getString("major")+rst.getString("grade")+rst.getString("class_id"));
				studentclass.add(tmp);
			}
		} catch(SQLException ex) {	
		}
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
	return studentclass;
}
	public void adminAddClass(StudentClass studentclass, AdminClass adminclass)  {
		String sql = "INSERT INTO student_class(student_id, academy, department, major, class_id, grade) values('" + studentclass.getStudent_id() + "','"
	+ studentclass.getAcademy()+"','" + studentclass.getDepartment() + "','"+studentclass.getMajor()+"',"+ adminclass.getClass_id()+","+adminclass.getGrade()+");";
		String sql2= "INSERT INTO student_username_password(student_id, password) values('"+ studentclass.getStudent_id() + "','"+ studentclass.getStudent_id()+"');";
		//System.out.println(sql2);
		//System.out.println(sql);
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		dbconn.doInsert(sql);
		dbconn.doInsert(sql2);
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
	}
	public void adminUpdateClass(StudentClass studentclass, AdminClass adminclass)  {
		String sql = "UPDATE student_class SET academy = '" + studentclass.getAcademy() + "',department= '"
				+ studentclass.getDepartment()+"',major ='" + studentclass.getMajor() + "',class_id="+adminclass.getClass_id()+",grade="+
				adminclass.getGrade()+" WHERE student_id = '"+studentclass.getStudent_id()+"';";
		//System.out.println(sql2);
		//System.out.println(sql);
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		dbconn.doInsert(sql);
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
	}
}
