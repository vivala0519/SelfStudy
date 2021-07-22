package test;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;

public class BasicTests {
    @Test
    public void basicTestCases() {
      assertEquals(6, CodeWars.overTheRoad(1, 3));
      assertEquals(4, CodeWars.overTheRoad(3, 3));
      assertEquals(5, CodeWars.overTheRoad(2, 3));
      assertEquals(8, CodeWars.overTheRoad(3, 5));
      assertEquals(16, CodeWars.overTheRoad(7, 11));
      assertEquals(1999981L, CodeWars.overTheRoad(20, 1000000));
      assertEquals(596421736780L, CodeWars.overTheRoad(23633656673L, 310027696726L)); 
    }
}