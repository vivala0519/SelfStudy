package test;
import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class SmallestIntegerFinder {

	public static int findSmallestInt(int[] args) {
		 System.out.println("d");
		 int args1[] = {34, 15, 88, 2};
		 int min = 0;
	     System.out.println("배열 수 : " + args1.length); 
	       for(int i = 1; i < args1.length; i++){
	         if(min > args1[i]) min = args1[i];
		     System.out.println("배열 수 : " + args1.length); 
	       }
	       
	      return min;
	}

	@Test
    public void example1(){
        int expected = 11;
        int actual = SmallestIntegerFinder.findSmallestInt(new int[]{78,56,232,12,11,43});
        assertEquals(expected, actual);
    }


    @Test
    public void example2(){
        int expected = -33;
        int actual = SmallestIntegerFinder.findSmallestInt(new int[]{78,56,-2,12,8,-33});
        assertEquals(expected, actual);
    }
    
    @Test
    public void example3(){
        int expected = Integer.MIN_VALUE;
        int actual = SmallestIntegerFinder.findSmallestInt(new int[]{0,Integer.MIN_VALUE,Integer.MAX_VALUE});
        assertEquals(expected, actual);
    }
}
