package study;

public class SmallestIntegerFinder {

	public static void main(String[] args) {
		 int args1[] = {34, 15, 88, 2, 23, 1, 454, -15};
		 int min = 0;
	     System.out.println("배열 수 : " + args1.length); 
	     min = args1[0];
     	 for(int i = 1; i < args1.length; i++){
    	    if(min > args1[i]) {
    	    	min = args1[i];
    	    }
        }

 	    System.out.println("최소값 : " + min);
	}

}
