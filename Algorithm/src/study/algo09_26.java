package study;

public class algo09_26 {

	public static void main(String[] args) {
		double principal = 1000;
		double interst = 0.05;
		double tax = 0.18;
		double desired = 1100;
		int i = 1;
		while(principal < desired) {
			System.out.println(i);
			double cal = principal * (1 + interst) - (principal * (1 + interst) - principal) * tax;
			System.out.println(cal);
			principal = cal;
			i ++;
			System.out.println(cal);
		}
//		for(int i = 1; principal > desired; i++) {
//			double cal = principal * (1 + interst) - (principal * (1 + interst) - principal) * tax;
//			System.out.println(cal);
//			principal = cal;
//			System.out.println(i);
//		}
		
	}

}
