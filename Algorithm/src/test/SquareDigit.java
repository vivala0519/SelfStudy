package test;
public class SquareDigit {

	public int squareDigits(int n) {
		String trans = String.valueOf(n);
		// trans = n ��Ʈ��ȭ
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
		return result;
	}

}