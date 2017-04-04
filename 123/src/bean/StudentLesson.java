package bean;

public class StudentLesson {
	private String student_id;
	private String class_term;
	private String class_name;
	public StudentLesson(){}
	public StudentLesson(String student_id, String class_term, String class_name) {
		this.student_id = student_id;
		this.class_term = class_term;
		this.class_name = class_name;
	}
	public String getStudent_id() {
		return student_id;
	}
	public void setStudent_id(String student_id) {
		this.student_id = student_id;
	}
	public String getClass_term() {
		return class_term;
	}
	public void setClass_term(String class_term) {
		this.class_term = class_term;
	}
	public String getClass_name() {
		return class_name;
	}
	public void setClass_name(String class_name) {
		this.class_name = class_name;
	}
	
}
