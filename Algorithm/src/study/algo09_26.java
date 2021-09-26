package study;

public class algo09_26 {

	public static void main(String[] args) {
		double principal = 1000;
		double interst = 0.01625;
		double tax = 0.18;
		double desired = 1000;
		int i = 0;
		while(principal < desired) {
			double cal = principal * (1 + interst) - (principal * interst) * tax;
			principal = cal;
			i ++;
			System.out.println(cal);
		}
		System.out.println(i);
//		principal = 1041.00;
//		System.out.println(principal * (1 + interst));
//		System.out.println(principal * (1 + interst) - principal);
//		System.out.println(principal * (1 + interst) - (principal * interst) * tax);
		
		
		
//		for(int i = 1; principal > desired; i++) {
//			double cal = principal * (1 + interst) - (principal * (1 + interst) - principal) * tax;
//			System.out.println(cal);
//			principal = cal;
//			System.out.println(i);
//		}
		
	}

}
