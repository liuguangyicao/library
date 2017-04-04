package dao;
import bean.Register;
import java.sql.ResultSet;
import utils.DBconn;
import java.sql.SQLException;

public class Check {
	public boolean checkRegister(String username)  {
		String sql = "SELECT COUNT(*) FROM student_username_password WHERE student_id = '" + username + "';";
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		boolean checkregister = true;
		rst = dbconn.doSelect(sql);
		try {
			if(rst.next()) {
			    if(rst.getInt(1) == 0) {
			    	checkregister = false;
			    	}
			}
		} catch(SQLException ex) {	
		}
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
		return checkregister;  
	}
	public boolean checkLogin(Register student)  {
		String sql = "SELECT * FROM student_username_password WHERE student_id = '" + student.getUsername() + "';";
		//System.out.println(sql);
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		boolean checklogin = false;
		rst = dbconn.doSelect(sql);
		try {
			if(rst.next()) {
				checklogin =  rst.getString("password").equals(student.getPassword());
			} else {
				checklogin =  false;
			}
		} catch(SQLException ex) {	
		}
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
		return checklogin;  
	}

	public void addUser(Register student) {
		String sql = "INSERT INTO student_username_password(student_id, password) VALUES ('" +student.getUsername()+"','"+student.getPassword()+"');";
		DBconn dbconn = new DBconn();
		ResultSet rst = null;
		dbconn.doInsert(sql);
		try {
			dbconn.close(rst);
		} catch(Exception ex) {	
		}
	}
}
