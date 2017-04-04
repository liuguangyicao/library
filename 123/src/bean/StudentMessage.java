package bean;

public class StudentMessage {
	private String age;
	private String name;
	private String studentId;
	private String sexy;
	
	public  StudentMessage(){}
	public  StudentMessage(String age, String name, String studentId, String sexy) {
		this.age = age;
		this.name = name;
		this.studentId = studentId;
		this.sexy = sexy;
	}
	public String getAge() {
		return age;
	}
	public void setAge(String age) {
		this.age = age;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getStudentId() {
		return studentId;
	}
	public void setStudentId(String studentId) {
		this.studentId = studentId;
	}
	public String getSexy() {
		return sexy;
	}
	public void setSexy(String sexy) {
		this.sexy = sexy;
	}
}

