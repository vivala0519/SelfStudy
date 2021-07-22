package study;


public class SquareDigit {
	public static void main(String[] args) {
	int num = 9119;
	String trans = String.valueOf(num);
	// trans = num 스트링화
	int length = trans.length();
	// trans 문자열 길이 구하기
	int arr[] = new int[length];
	// 배열 선언
	for(int i = 0; i < length; i++) {
		arr[i] = (int) Math.pow(trans.charAt(i)-48, 2);
		//첫글자부터 인트화+제곱 배열에 넣기
	}
	String res = "";
	//결과 문자열 선언
	for(int i = 0; i < length; i++) {
		res += String.valueOf(arr[i]);
		//배열에 있는 값들 합쳐서 문자열화
	}
	int result = 0;
	//최종결과물 인트화를 위한 선언
	result = Integer.parseInt(res);
	//문자열 -> 정수
	System.out.println(result);
	}
}
