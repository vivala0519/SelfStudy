package test;

import java.util.ArrayList;

class CodeWars {
	  public static long overTheRoad(long address, long n) {
//		ArrayList<Long> odd = new ArrayList<Long>();
//		ArrayList<Long> even = new ArrayList<Long>();
//		long j = 1;
//		long k = 2*n;
//		long result = 0;
//		for (int i = 0; i < n; i++) {
//			odd.add(j);
//			even.add(k);
//			j += 2;
//			k -= 2;
//		}
//		if (address%2 == 0) {
//			for (int i = 0; i < n; i++) {
//				if(even.get(i) == address) {
//					result = odd.get(i);
//				}
//			}
//		}
//		else {
//			for (int i = 0; i < n; i++) {
//				if(odd.get(i) == address) {
//					result = even.get(i);
//				}
//			}
//		}
//		return result;
		  
		return (n * 2) - (address - 1);
	  }
	}