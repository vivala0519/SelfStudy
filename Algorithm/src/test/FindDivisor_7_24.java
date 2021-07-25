package test;

public class FindDivisor_7_24 {
	public long numberOfDivisors(int n) {
		long count = 0;
		for(int i = 1; i <= n; i++) {
			if(n % i == 0) {
				count += 1;
			}
		}
		return count;
	  }
}
