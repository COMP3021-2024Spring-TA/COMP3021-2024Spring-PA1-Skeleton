package hk.ust.comp3021;

import hk.ust.comp3021.utils.ASTParser;

import hk.ust.comp3021.utils.TestKind;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.*;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;


import static org.junit.jupiter.api.Assertions.*;

public class ASTManagerEngineTest {

    @Tag(TestKind.PUBLIC)
    @Test
    void testParse2XMLNode() {
        ASTParser parser = new ASTParser("1");
        parser.parse2XMLNode();
        assertNotNull(parser.getRootXMLNode());
        assertEquals(parser.getRootXMLNode().getTagName(), "ast");
        assertFalse(parser.isErr());
    }

    @Tag(TestKind.PUBLIC)
    @Test
    public void testPrintedInformation() {
        ASTManagerEngine engine = new ASTManagerEngine();
        engine.processXMLParsing(String.valueOf(227));

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PrintStream printStream = new PrintStream(outputStream);
        PrintStream originalPrintStream = System.out;
        System.setOut(printStream);

        engine.findFuncWithArgGtN(4);
        System.setOut(originalPrintStream);
        String printedOutput = outputStream.toString();

        // the function name should be astID_FuncName_UniqueID
        Set<String> expectedOutput = Set.of(
                "227_diagonalBinarySearch_2",
                "227_rowBinarySearch_13",
                "227_colBinarySearch_27");
        assertEquals(expectedOutput, Set.of(printedOutput.trim().split("\\r?\\n")));
    }

    @Tag(TestKind.PUBLIC)
    @Test
    void testCalculateOp2Nums() {
        ASTManagerEngine engine = new ASTManagerEngine();
        int xmlFileTot = engine.countXMLFiles(engine.getDefaultXMLFileDir());
        for (int i = 0; i < xmlFileTot; i++) {
            engine.processXMLParsing(String.valueOf(i));
        }
        HashMap<String, Integer> op2Num = engine.calculateOp2Nums();
        HashMap<String, Integer> expectedOp2Num = new HashMap<>();

        expectedOp2Num.put("And", 253);
        expectedOp2Num.put("Or", 101);

        expectedOp2Num.put("Add", 1257);
        expectedOp2Num.put("Sub", 862);
        expectedOp2Num.put("Mult", 171);
        expectedOp2Num.put("Div", 18);
        expectedOp2Num.put("Mod", 86);
        expectedOp2Num.put("Pow", 11);
        expectedOp2Num.put("LShift", 16);
        expectedOp2Num.put("RShift", 22);
        expectedOp2Num.put("BitOr", 6);
        expectedOp2Num.put("BitXor", 24);
        expectedOp2Num.put("BitAnd", 43);
        expectedOp2Num.put("FloorDiv", 153);

        expectedOp2Num.put("Invert", 2);
        expectedOp2Num.put("Not", 222);
        expectedOp2Num.put("USub", 265);
        expectedOp2Num.put("Eq", 671);
        expectedOp2Num.put("NotEq", 119);

        expectedOp2Num.put("Lt", 375);
        expectedOp2Num.put("LtE", 156);
        expectedOp2Num.put("Gt", 238);
        expectedOp2Num.put("GtE", 92);
        expectedOp2Num.put("Is", 2);
        expectedOp2Num.put("IsNot", 17);
        expectedOp2Num.put("In", 95);
        expectedOp2Num.put("NotIn", 76);
        assertEquals(expectedOp2Num, op2Num);
    }

    @Tag(TestKind.PUBLIC)
    @Test
    void testMostCommonUsedOp() {
        ASTManagerEngine engine = new ASTManagerEngine();
        int xmlFileTot = engine.countXMLFiles(engine.getDefaultXMLFileDir());
        for (int i = 0; i < xmlFileTot; i++) {
            engine.processXMLParsing(String.valueOf(i));
        }
        HashMap<String, Integer> op2Num = engine.calculateOp2Nums();
        String maxOp = engine.mostCommonUsedOp(op2Num);
        assertEquals(maxOp, "Add");
    }


    @Tag(TestKind.PUBLIC)
    @Test
    void testCalculateNode2Num() {
        ASTManagerEngine engine = new ASTManagerEngine();
        int xmlFileTot = engine.countXMLFiles(engine.getDefaultXMLFileDir());
        for (int i = 0; i < xmlFileTot; i++) {
            engine.processXMLParsing(String.valueOf(i));
        }
        HashMap<String, Integer> node2Num = engine.calculateNode2Nums("0");
        HashMap<String, Integer> expectedNode2Num = new HashMap<>();
        expectedNode2Num.put("Module", 1);
        expectedNode2Num.put("ClassDef", 1);
        expectedNode2Num.put("FunctionDef", 2);
        expectedNode2Num.put("arguments", 2);

        expectedNode2Num.put("arg", 4);
        expectedNode2Num.put("Name", 29);
        expectedNode2Num.put("Assign", 7);
        expectedNode2Num.put("Constant", 1);

        expectedNode2Num.put("While", 2);

        expectedNode2Num.put("BoolOp", 1);
        expectedNode2Num.put("Compare", 2);
        expectedNode2Num.put("Attribute", 13);

        expectedNode2Num.put("Tuple", 2);
        expectedNode2Num.put("Return", 2);

        expectedNode2Num.put("Subscript", 2);

        expectedNode2Num.put("Call", 1);
        expectedNode2Num.put("If", 1);
        assertEquals(expectedNode2Num, node2Num);
    }


    @Tag(TestKind.PUBLIC)
    @Test
    void testCalledFuncOnXML1() {
        ASTManagerEngine engine = new ASTManagerEngine();
        engine.processXMLParsing("0");

        HashMap<String, Set<String>> func2CalledFuncs = engine.calculateCalledFunc();
        HashMap<String, Set<String>> expectedMap = new HashMap<>();

        expectedMap.put("0_sortList_19", Set.of("0_self.bubbleSort_20"));
        expectedMap.put("0_bubbleSort_2", new HashSet<>());
        assertEquals(func2CalledFuncs, expectedMap);
    }


    @Tag(TestKind.PUBLIC)
    @Test
    public void testProcessNodeFreq() {
        ASTManagerEngine engine = new ASTManagerEngine();
        int xmlFileTot = engine.countXMLFiles(engine.getDefaultXMLFileDir());
        for (int i = 0; i < xmlFileTot; i++) {
            engine.processXMLParsing(String.valueOf(i));
        }

        assertEquals(engine.getId2ASTModules().size(), 837);
        HashMap<String, Integer> funcName2NodeNum = engine.processNodeFreq();
        assertEquals(funcName2NodeNum.size(), 1126);
        assertEquals(Collections.max(funcName2NodeNum.values()), 221);
        assertEquals(Collections.min(funcName2NodeNum.values()), 6);
    }

    @Tag(TestKind.PUBLIC)
    @Test
    public void testSortHashMapByValue() {
        ASTManagerEngine engine = new ASTManagerEngine();
        HashMap<String, Integer> map = new HashMap<>();
        map.put("A", 5);
        map.put("B", 2);
        map.put("C", 7);
        map.put("D", 1);

        // Call the sortHashMapByValue method
        List<Map.Entry<String, Integer>> result = engine.sortHashMapByValue(map);

        // Create an expected sorted list based on values
        List<Map.Entry<String, Integer>> expected = new ArrayList<>(map.entrySet());
        expected.sort(Map.Entry.comparingByValue());

        // Assert that the result matches the expected sorted list
        assertEquals(expected, result);
    }

    @Tag(TestKind.PUBLIC)
    @Test
    public void testBonusPrintByPos() {
        ASTManagerEngine engine = new ASTManagerEngine();
        engine.processXMLParsing("0");
        StringBuilder stringBuilder = new StringBuilder("");
        engine.getId2ASTModules().get("0").printByPos(stringBuilder);
        String expectedOutput = "class Solution:\n" +
                "    def bubbleSort(self, head: ListNode):\n" +
                "        node_i = head\n" +
                "        tail = None\n" +
                "\n" +
                "        while node_i:\n" +
                "            node_j = head\n" +
                "            while node_j and node_j.next != tail:\n" +
                "                if node_j.val > node_j.next.val:\n" +
                "\n" +
                "                    node_j.val, node_j.next.val = node_j.next.val, node_j.val\n" +
                "                node_j = node_j.next\n" +
                "\n" +
                "            tail = node_j\n" +
                "            node_i = node_i.next\n" +
                "\n" +
                "        return head\n" +
                "\n" +
                "    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:\n" +
                "        return self.bubbleSort(head)";
        assertEquals(expectedOutput, stringBuilder.toString());
    }
}
