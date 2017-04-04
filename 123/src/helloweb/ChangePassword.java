package helloweb;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import bean.Register;
import bean.StudentClass;
import bean.StudentMessage;
import dao.Check;
import dao.StudentDao;

/**
 * Servlet implementation class ChangePassword
 */
@WebServlet("/ChangePassword")
public class ChangePassword extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ChangePassword() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		HttpSession session = request.getSession();
		if(session == null || ((String)session.getAttribute("username")).equals("admin")) {
			response.sendRedirect("login.jsp");
			return;
		} 
		response.sendRedirect("changepassword.jsp");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		HttpSession session = request.getSession();
		StudentDao studentdao = new StudentDao();
		String username = (String)session.getAttribute("username");
		String oldpassword = request.getParameter("oldpassword");
		String newpassword = request.getParameter("newpassword");
		Register student = new Register(username, oldpassword);
		Check check = new Check();
		boolean checkStudent = check.checkLogin(student);
		String update;
		if(!checkStudent) {
			update = "ÃÜÂë´íÎó";
		} else {
			Register newstudent = new Register(username, newpassword);
			studentdao.updatePassword(newstudent);
			update = "ÐÞ¸Ä³É¹¦";
		}
		request.setAttribute("update", update);
		RequestDispatcher rd = request.getRequestDispatcher("/changepassword.jsp");
		rd.forward(request,response);
	}

}
