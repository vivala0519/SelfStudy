package study;

import java.util.ArrayList;

public class overTheRoad {

	public static void main(String[] args) {
		long addr = 23633656673L;
		long n = 310027696726L;
		ArrayList<Long> odd = new ArrayList<Long>();
		ArrayList<Long> even = new ArrayList<Long>();
		long j = 1;
		long k = 2*n;
		for (int i = 0; i < n; i++) {
			odd.add(j);
			even.add(k);
			j += 2;
			k -= 2;
		}
		if (addr%2 == 0) {
			for (int i = 0; i < n; i++) {
				if(even.get(i) == addr) {
					System.out.println(odd.get(i));
				}
			}
		}
		else {
			for (int i = 0; i < n; i++) {
				if(odd.get(i) == addr) {
					System.out.println(even.get(i));
				}
			}
		}
		
	}

}
