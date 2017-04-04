package bean;

public class AdminClass {
	private String major;
	private String class_id;
	private String grade;
	public AdminClass(String major, String class_id, String grade) {
		this.major = major;
		this.class_id = class_id;
		this.grade = grade;
	}
	
	public String getMajor() {
		return major;
	}
	public void setMajor(String major) {
		this.major = major;
	}
	public String getClass_id() {
		return class_id;
	}
	public void setClass_id(String class_id) {
		this.class_id = class_id;
	}
	public String getGrade() {
		return grade;
	}
	public void setGrade(String grade) {
		this.grade = grade;
	}
}