package study;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class algo09_29 {

	public static void main(String[] args) {
		int[] a = {1, 2, 2, 2, 3};
		int[] b = {2};
		
		for(int i = 0; i < b.length; i++) {
			for(int j = 0; j < a.length; j++) {
				if(a[j] == b[i]) {
					a[j] = -1;
				}
			}
		}
		System.out.println(Arrays.toString(a));
		List<Integer> list = new ArrayList<Integer>();
		for(int i = 0; i < a.length; i++) {
			if(a[i] != -1) {
				list.add(a[i]);
			}
		}
		System.out.println(list);
		int[] result = list.stream().mapToInt(i->i).toArray();
		System.out.println(Arrays.toString(result));
	}
}
