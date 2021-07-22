package study;

public class multi {

	public static void main(String[] args) {
		String multiple = "";
		int num = 5;
		for(int i=1; i<=10; i++) {
			multiple += i;
			multiple += " * ";
			multiple += num;
			multiple += " = ";
			multiple += i * num;
			multiple += "\n";
		}
		System.out.println(multiple.toString().trim());
	}

}
