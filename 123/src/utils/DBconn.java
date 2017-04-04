package utils;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class DBconn {
	public static Connection conn;//定义连接 
	public static Statement stmt;//定义STMT     
	public ResultSet rs;//定义结果集    
	static{     
		String url = "jdbc:mysql://localhost:3306/class?"   + "user=root&password=51258868lin&useUnicode=true&characterEncoding=UTF8&useSSL=false";    
		try {  
			Class.forName("com.mysql.jdbc.Driver");// 动态加载mysql驱动  	  
	        conn = DriverManager.getConnection(url);  
	    } catch(ClassNotFoundException e) {
	    	
	    }
		catch(SQLException e) {  
	        e.printStackTrace();    
	    } catch (Exception e) {  
	        e.printStackTrace();  
	    }  
	}     
     public static Connection getConn(){     
         return conn;     
     }
     public void doInsert(String sql) {     
         try {
        	 //Connection conn = DBconn.getConn();
             stmt = conn.createStatement();     
             int i = stmt.executeUpdate(sql);
             if (stmt != null) {     
                 stmt.close();     
                 stmt = null;     
               }   
         } catch(SQLException sqlexception) {     
             System.err.println("db.executeInsert:" + sqlexception.getMessage());     
         }    
     }  
     public ResultSet doSelect(String sql) {
    	 try {
    		 stmt = conn.createStatement();
    		 rs = stmt.executeQuery(sql);
    	 } catch(SQLException sqlexception) {
    		 System.err.println("db.executeSelect:" + sqlexception.getMessage());  
    	 }
    	 return rs;
     }
     public void close(ResultSet rs) throws SQLException, Exception {       
         if (rs != null) {     
           rs.close();     
           rs = null;     
         }     
         if (stmt != null) {     
           stmt.close();     
           stmt = null;     
         }      
       }     
      
       /**   
        *关闭数据库操作对象，数据库连接对象   
        * Close all the statement and conn int this instance   
        * @throws SQLException   
        * @throws Exception   
        */    
       public void close() throws SQLException, Exception {     
         if (stmt != null) {     
           stmt.close();     
           stmt = null;     
         }     
      
         if (conn != null) {     
           conn.close();     
           conn = null;     
         }     
       }
}
