package test;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

// TODO: Replace examples and use TDD by writing your own tests

public class SolutionTest {

    @Test
    public void exampleTestCases() {
        assertEquals(-1, Solution.closeCompare(4, 5));
        assertEquals(0, Solution.closeCompare(5, 5));
        assertEquals(1, Solution.closeCompare(6, 5));
        assertEquals(-1, Solution.closeCompare(-6, -5));

        assertEquals(0, Solution.closeCompare(2, 5, 3));
        assertEquals(1, Solution.closeCompare(8.1, 5, 3));
        assertEquals(-1, Solution.closeCompare(1.99, 5, 3));
    }

}
