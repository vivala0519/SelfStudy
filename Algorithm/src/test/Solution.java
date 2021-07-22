package test;
public class Solution {

  public static int closeCompare(double a, double b) {
	  return closeCompare(a,b,0);
  }
  
  public static int closeCompare(double a, double b, double margin) {
	  if(Math.abs(a-b) <= margin) {
			return 0;
		}
		else {
			if(a < b) {
				return -1;
			}
			else {
				return 1;
			}
		}
  }
}