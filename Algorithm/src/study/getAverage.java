package study;

public class getAverage {

	public static void main(String[] args) {
		int score[] = {1,1,1,1,1,1,1,2};
		int length = score.length;
		int sum = 0;
		for(int i = 0; i<length; i++) {
			sum = sum + score[i];
		}
		int avg = sum/length;
		System.out.println(avg);
	}
}
