package study;


public class SquareDigit {
	public static void main(String[] args) {
	int num = 9119;
	String trans = String.valueOf(num);
	// trans = num ��Ʈ��ȭ
	int length = trans.length();
	// trans ���ڿ� ���� ���ϱ�
	int arr[] = new int[length];
	// �迭 ����
	for(int i = 0; i < length; i++) {
		arr[i] = (int) Math.pow(trans.charAt(i)-48, 2);
		//ù���ں��� ��Ʈȭ+���� �迭�� �ֱ�
	}
	String res = "";
	//��� ���ڿ� ����
	for(int i = 0; i < length; i++) {
		res += String.valueOf(arr[i]);
		//�迭�� �ִ� ���� ���ļ� ���ڿ�ȭ
	}
	int result = 0;
	//��������� ��Ʈȭ�� ���� ����
	result = Integer.parseInt(res);
	//���ڿ� -> ����
	System.out.println(result);
	}
}
