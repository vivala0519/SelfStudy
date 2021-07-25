package test;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class DividerTests_7_24 {
	FindDivisor_7_24 fd = new FindDivisor_7_24();

	@Test
	public void fourTest() {
		assertEquals("Sould return 3 if the parameter equals 4", 3, fd.numberOfDivisors(4));
	}
  
	@Test
	public void fiveTest() {
		assertEquals("Sould return 2 if the parameter equals 5", 2, fd.numberOfDivisors(5));
	}
  
	@Test
	public void twelveTest() {
		assertEquals("Sould return 6 if the parameter equals 12", 6, fd.numberOfDivisors(12));
	}
  
	@Test
	public void thirtyTest() {
		assertEquals("Sould return 8 if the parameter equals 30", 8, fd.numberOfDivisors(30));
	}
}
