package helloweb;
import java.io.IOException;
import java.sql.Connection;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import bean.Register;
import bean.StudentMessage;
import dao.Check;
/**
 * Servlet implementation class HelloServlet
 */
@WebServlet("/HelloServlet")
public class UserRegister extends HttpServlet {
	private static final long serialVersionUID = 1L;
	Connection conn = null;  
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.sendRedirect("Register.jsp");
	}
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		String username = request.getParameter("username");
		String password = request.getParameter("password");
		Register student = new Register(username, password);
		Check check = new Check();
		boolean checkStudent = check.checkRegister(username);
		if(!checkStudent) {
			check.addUser(student);
		} else {
			response.sendRedirect("Register.jsp");
		}
	}
}

