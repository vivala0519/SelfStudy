package study;

public class CloseCompare {

	public static void main(String[] args) {
		double a = 3;
		double b = 5;
		double margin = 0;
		int return_value = 0;
		if(Math.abs(a-b) <= margin) {
			return_value =  0;
		}
		else {
			if(a < b) {
				return_value = -1;
			}
			else {
				return_value = 1;
			}
		}
		System.out.println(return_value);
	}

}
