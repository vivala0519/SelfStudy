package study;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class algo10_03 {

	/**
	 * @param args
	 * @throws IOException
	 */
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		String input = br.readLine();
//		System.out.println("hi : " + input);
		String input = "5 5 3\n1 5\n1 5\n2 3\n2 5\n1 3";
		String first = input.split("\n")[0];
		System.out.println(first);
		//엘리베이터 이용하고자 하는 사람의 수
		int n = Integer.parseInt(first.split(" ")[0]);
		//최대 층 수
		int k = Integer.parseInt(first.split(" ")[1]);
		//엘리베이터 정원
		int m = Integer.parseInt(first.split(" ")[2]);
		
		
		String[] people = new String[n];
		for(int i = 0; i < n; i++) {
			people[i] = input.split("\n")[i+1];
		}
		System.out.println(Arrays.toString(people));
		List<Integer> elevator = new ArrayList<Integer>();
		int full = 0;
		int now_floor = 1;
		int second = 0;
		while(full != 1) {
			for(int i = now_floor; i < k + 1; i++) {
				for(int j = 0; j < people.length; j++) {
					if(Integer.parseInt(people[j].split(" ")[0]) == i) {
						if(elevator.size() == m) {
							full = 1;
							now_floor = i;
							System.out.println(i);
							break;
						}
						else {
							elevator.add(Integer.parseInt(people[j].split(" ")[1]));
							people[j] = "0";
						}	
					}	
				}	
			}
		}
		System.out.println("now" + now_floor);
		System.out.println(elevator);
		System.out.println(Arrays.toString(people));
		move(elevator, now_floor, k);
		now_floor = elevator.get(0);
		elevator.remove(0);
		System.out.println(now_floor);
		second = now_floor - 1;
	}
	
	public static List<Integer> move(List<Integer> elevator, int now_floor, int k) {
		System.out.println(elevator);
		for(int i = now_floor; i < k+1; i++) {
			for(int j = 0; j < elevator.size(); j++) {
				if(elevator.get(j) == i) {
					elevator.remove(j--);
					now_floor = i;
				}
			}
		}
		elevator.add(now_floor);
		System.out.println(elevator);
		System.out.println(now_floor);
		return elevator;
	}

}
