package bean;

public class Lesson {
	private String class_term;
	private String class_name;
	private String class_major;
	public Lesson(){}
	public Lesson(String class_term, String class_name, String class_major) {
		this.class_term = class_term;
		this.class_name = class_name;
		this.class_major = class_major;
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
	public String getClass_major() {
		return class_major;
	}
	public void setClass_major(String class_major) {
		this.class_major = class_major;
	}
	
}
