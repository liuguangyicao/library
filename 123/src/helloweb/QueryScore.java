package helloweb;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import bean.StudentLesson;
import dao.StudentDao;

/**
 * Servlet implementation class QueryScore
 */
@WebServlet("/QueryScore")
public class QueryScore extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public QueryScore() {
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
		response.sendRedirect("queryscore.jsp");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		request.setCharacterEncoding("UTF-8");
		HttpSession session = request.getSession();
		String username = (String)session.getAttribute("username");
		String class_term = request.getParameter("class_term");
		String class_name = request.getParameter("class_name");
		StudentLesson studentlesson = new StudentLesson(username, class_term, class_name);
		StudentDao studentdao = new StudentDao();
		request.setAttribute("score",studentdao.queryStudentScore(studentlesson));
		request.setAttribute("studentlesson",studentlesson);
		RequestDispatcher rd = request.getRequestDispatcher("/queryscore.jsp");
		rd.forward(request,response);
	}

}
