package study;

public class FindDivisor_7_24 {

	public static void main(String[] args) {
		int num = 12;
		int count = 0;
		for(int i = 1; i <= num; i++) {
			if(num % i == 0) {
				count += 1;
			}
		}
		System.out.println(count);
	}

}
