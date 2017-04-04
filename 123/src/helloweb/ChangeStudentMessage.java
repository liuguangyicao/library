package helloweb;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import bean.StudentClass;
import bean.StudentMessage;
import dao.StudentDao;

/**
 * Servlet implementation class ChangeStudentMessage
 */
@WebServlet("/ChangeStudentMessage")
public class ChangeStudentMessage extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public ChangeStudentMessage() {
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
		StudentDao studentdao = new StudentDao();
		String username = (String)session.getAttribute("username");
		StudentMessage studentmessage = studentdao.queryStudentMessage(username);
		StudentClass studentclass = studentdao.queryStudentClass(username);
		request.setAttribute("studentmessage", studentmessage);
		request.setAttribute("studentclass", studentclass);
		RequestDispatcher rd = request.getRequestDispatcher("/changemessage.jsp");
		rd.forward(request,response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		HttpSession session = request.getSession();
		String username = (String)session.getAttribute("username");
		String name = request.getParameter("name");
		String age = request.getParameter("age");
		String sexy;
		if(request.getParameter("sexy").equals("ÄÐ")) {
			sexy = "0";
		} else {
			sexy = "1";
		}
		StudentMessage updatemessage = new StudentMessage(age, name, username, sexy);
		String sql = "UPDATE student_message SET name = '" + updatemessage.getName() + "',age = "
				+ updatemessage.getAge()+",sexy =" + updatemessage.getSexy() + "WHERE student_id = '"+updatemessage.getStudentId()+"';";
		StudentDao studentdao = new StudentDao();
		studentdao.updateStudentMessage(updatemessage);
		response.sendRedirect("StudentQuery");
	}

}
