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
import dao.Check;
import dao.StudentDao;

/**
 * Servlet implementation class AdminUpdateStudent
 */
@WebServlet("/AdminUpdateStudent")
public class AdminUpdateStudent extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AdminUpdateStudent() {
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
		response.sendRedirect("adminaddstudent.jsp");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		StudentDao studentdao = new StudentDao();
		Check check = new Check();
		String update;
		String student_id = (String)request.getParameter("student_id");
		if(!check.checkRegister(student_id)) {
			update = "用户不存在";
			request.setAttribute("update", update);
			RequestDispatcher rd = request.getRequestDispatcher("/adminupdatestudent.jsp");
			rd.forward(request,response);
			return;
		}
		String academy= (String)request.getParameter("academy");
		String department = (String)request.getParameter("department");
		String major = (String)request.getParameter("major");
		String class_id = (String)request.getParameter("class_id");
		String grade = (String)request.getParameter("grade");
		String class_name = major + grade + class_id;
		StudentClass studentclass = new StudentClass(student_id, academy, department, major, class_name);
		AdminClass adminclass = new AdminClass(major, class_id, grade);
		studentdao.adminUpdateClass(studentclass, adminclass);
		update = "修改成功";
		request.setAttribute("update", update);
		RequestDispatcher rd = request.getRequestDispatcher("/adminaddstudent.jsp");
		rd.forward(request,response);
	}

}
