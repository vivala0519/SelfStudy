package test;
public class School {
	public static int getAverage(int[] marks){
		int length = marks.length;
		int sum = 0;
		for(int i = 0; i<length; i++) {
			sum = sum + marks[i];
		}
		int avg = sum/length;
		return avg;
	}
}
