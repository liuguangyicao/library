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
 * Servlet implementation class AdminQueryMessage
 */
@WebServlet("/AdminQueryMessage")
public class AdminQueryMessage extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public AdminQueryMessage() {
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
		request.setCharacterEncoding("UTF-8");
		StudentDao studentdao = new StudentDao();
		String username = (String)request.getParameter("student_id");
		StudentMessage studentmessage = studentdao.queryStudentMessage(username);
		StudentClass studentclass = studentdao.queryStudentClass(username);
		request.setAttribute("studentmessage", studentmessage);
		request.setAttribute("studentclass", studentclass);
		RequestDispatcher rd = request.getRequestDispatcher("/admin.jsp");
		rd.forward(request,response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
