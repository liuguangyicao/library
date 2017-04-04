package helloweb;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import bean.AdminClass;
import bean.StudentClass;
import dao.StudentDao;
import java.util.*;
/**
 * Servlet implementation class AdminQueryClass
 */
@WebServlet("/AdminQueryClass")
public class AdminQueryClass extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AdminQueryClass() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		HttpSession session = request.getSession();
		if(session == null || !((String)session.getAttribute("username")).equals("admin")) {
			response.sendRedirect("login.jsp");
			return;
		} 
		response.sendRedirect("adminclass.jsp");
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		StudentDao studentdao = new StudentDao();
//		StudentMessage studentmessage = studentdao.queryStudentMessage(username);
		String major = (String)request.getParameter("major");
		String class_id = (String)request.getParameter("class_id");
		String grade = (String)request.getParameter("grade");
		AdminClass adminclass = new AdminClass(major, class_id, grade);
		List<StudentClass> studentclass = studentdao.adminQueryClass(adminclass);
		request.setAttribute("studentclass", studentclass);
		//StudentClass s = studentclass.get(0);
		//System.out.println(s.getMajor());
//		request.setAttribute("studentmessage", studentmessage);
//		request.setAttribute("studentclass", studentclass);
		RequestDispatcher rd = request.getRequestDispatcher("/adminclass.jsp");
		rd.forward(request,response);
	}

}
