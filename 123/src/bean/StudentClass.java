package bean;

public class StudentClass {
	private String student_id;
	private String academy;
	private String department;
	private String major;
	private String class_name;
	public StudentClass() {	}
	public StudentClass(String student_id, String academy,
			String department, String major, String class_name) {
		this.student_id = student_id;
		this.academy = academy;
		this.department = department;
		this.major= major;
		this.class_name = class_name;
	}
	public String getStudent_id() {
		return student_id;
	}
	public void setStudent_id(String student_id) {
		this.student_id = student_id;
	}
	public String getAcademy() {
		return academy;
	}
	public void setAcademy(String academy) {
		this.academy = academy;
	}
	public String getDepartment() {
		return department;
	}
	public void setDepartment(String department) {
		this.department = department;
	}
	public String getMajor() {
		return major;
	}
	public void setMajor(String major) {
		this.major = major;
	}
	public String getClass_name() {
		return class_name;
	}
	public void setClass_name(String class_name) {
		this.class_name = class_name;
	}
	
}
