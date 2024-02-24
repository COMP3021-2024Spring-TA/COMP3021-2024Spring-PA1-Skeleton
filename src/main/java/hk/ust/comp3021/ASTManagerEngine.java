package hk.ust.comp3021;

import hk.ust.comp3021.stmt.*;
import hk.ust.comp3021.utils.*;
import java.io.*;
import java.util.*;

public class ASTManagerEngine {
    private final String defaultXMLFileDir;
    private final HashMap<String, ASTModule> id2ASTModules;

    public ASTManagerEngine() {
        defaultXMLFileDir = "resources/pythonxml/";
        id2ASTModules = new HashMap<>();
    }

    public void userInterface() {
        System.out.println("----------------------------------------------------------------------");
        System.out.println("ASTManager is running...");

        while (true) {
            System.out.println("----------------------------------------------------------------------");
            System.out.println("Please select the following operations with the corresponding numbers:");
            System.out.println("  0: Given AST ID, parse AST from XML files");
            System.out.println("  1: Print all functions with # arguments greater than user specified N");
            System.out.println("  2: Find the most commonly used operators in all ASTs");
            System.out.println("  3: Print all functions names and the functions invoked by each function");
            System.out.println("  4: Given AST ID, count the number of all node types");
            System.out.println("  5: Sort all functions based on # children nodes");
            System.out.println("  6: Given AST ID, recover Python Code (Bonus Task)");
            System.out.println("  7: Exit");
            System.out.println("----------------------------------------------------------------------");
            Scanner scan1 = new Scanner(System.in);
            if (scan1.hasNextInt()) {
                int i = scan1.nextInt();
                if (i < 0 || i > 7) {
                    System.out.println("You should enter 0~7.");
                    continue;
                }

                switch (i) {
                case 0: {
                    userInterfaceParseXML();
                    break;
                }
                case 1: {
                    userInterfaceParamNum();
                    break;
                }
                case 2: {
                    userInterfaceCommonOp();
                    break;
                }
                case 3: {
                    userInterfaceCallFuncs();
                    break;
                }
                case 4: {
                    userInterfaceCountNum();
                    break;
                }
                case 5: {
                    userInterfaceSortByChild();
                    break;
                }
                case 6: {
                    userInterfaceRecoverCode();
                    break;
                }
                default: {

                }
                }
                if (i == 7) {
                    break;
                }
            } else {
                System.out.println("You should enter integer 0~6.");
            }
        }
    }

    public int countXMLFiles(String dirPath) {
        int count = 0;
        File directory = new File(dirPath);
        if (directory.isDirectory()) {
            File[] files = directory.listFiles();
            if (files != null) {
                for (File file : files) {
                    if (file.isDirectory()) {
                        count += countXMLFiles(file.getAbsolutePath());
                    } else if (file.isFile() && file.getName().toLowerCase().endsWith(".xml")) {
                        count++;
                    }
                }
            }
        }

        return count;
    }


    /*
    * Task 0: Given AST ID, parse AST from XML files
    */

    public void processXMLParsing(String xmlID) {
        ASTParser parser = new ASTParser(xmlID);
        parser.parse();
        if (!parser.isErr()) {
            this.id2ASTModules.put(xmlID, parser.getASTModule());
            System.out.println("AST " + xmlID + " Succeed! The XML file is loaded!");
        } else {
            System.out.println("AST " + xmlID + " Failed! Please check your implementation!");
        }
    }

    public void userInterfaceParseXML() {
        int xmlCount = countXMLFiles(this.defaultXMLFileDir);
        System.out.println("Please specify the XML file ID to parse (0~" + xmlCount + ") or -1 for all:");
        Scanner scan1 = new Scanner(System.in);
        if (scan1.hasNextLine()) {
            String xmlID = scan1.nextLine();
            if (!xmlID.equals("-1")) {
                processXMLParsing(xmlID);
            } else {
                File directory = new File(this.defaultXMLFileDir);
                if (directory.isDirectory()) {
                    File[] files = directory.listFiles();
                    if (files != null) {
                        for (File file : files) {
                            if (file.isFile() && file.getName().toLowerCase().endsWith(".xml")) {
                                String str = file.getName().toLowerCase();
                                int startIndex = str.indexOf('_') + 1;
                                int endIndex = str.indexOf(".xml");

                                if (endIndex > startIndex) {
                                    processXMLParsing(str.substring(startIndex, endIndex));
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    /*
     * Task 1: Print all functions with # arguments greater than user specified N
     */

    public void findFuncWithArgGtN(int paramN) {
        for (String key : id2ASTModules.keySet()) {
            ASTModule module = id2ASTModules.get(key);
            for (FunctionDefStmt func : module.getAllFunctions()) {
                if (func.getParamNum() >= paramN) {
                    System.out.println(module.getASTID() + "_" + func.getName());
                }
            }
        }
    }

    public void userInterfaceParamNum() {
        System.out.println("Please indicate the value of N (recommended range 0~5):");
        Scanner scan2 = new Scanner(System.in);
        if (scan2.hasNextLine()) {
            String paramN = scan2.nextLine();
            try {
                int number = Integer.parseInt(paramN);
                System.out.println("Parsed number: " + number);
                findFuncWithArgGtN(number);
            } catch (NumberFormatException e) {
                System.out.println("Error! Invalid number format");
            }

        }
    }

    /*
     * Task 2: Find the most commonly used operators in all ASTs
     */


    /*
     * Calculate the frequency of each node in the AST
     * @return: HashMap that records the mapping from operator name to the
     *          frequency of this operator
     */
    public HashMap<String, Integer> calculateOp2Nums() {
        // TODO: complete the definition of the method `calculateOp2Nums`
        return null;
    }

    /*
     * Find the operator whose has the largest frequency
     * @return: return the operator name with largest frequency
     */
    public String mostCommonUsedOp(HashMap<String, Integer> op2Num) {
        // TODO: complete the definition of the method `mostCommonUsedOp`
        return "";
    }


    public void userInterfaceCommonOp() {
        HashMap<String, Integer> op2Num = calculateOp2Nums();
        String maxOp = mostCommonUsedOp(op2Num);
        if (maxOp != null) {
            System.out.println("Most common operator is " + maxOp + " with frequency " + op2Num.get(maxOp));
        } else {
            System.out.println("Failed to find most common operator!");
        }
    }

    /*
     * Task 3: Print all functions names and the functions invoked by each function")
     */

    /*
     * First, you need to find all declarative functions, whose node is FunctionDefStmt.
     * Then, starting from the node, find all CallExpr nodes,
     * Finally, obtain the called function name.
     *
     * Hints: we have prepared some methods for you, e.g., getCalledFuncName.
     *
     * @return: Hashmap that stores the mapping from function name
     *          to the set of functions that invokes
     */
    public HashMap<String, Set<String>> calculateCalledFunc() {
        // TODO: complete the definition of the method `calculateCalledFunc`
        return null;
    }

    public void userInterfaceCallFuncs() {
        HashMap<String, Set<String>> func2CalledFuncs = calculateCalledFunc();

        for (Map.Entry<String, Set<String>> entry : func2CalledFuncs.entrySet()) {
            String curFunc = entry.getKey();
            for (String calledFunc : entry.getValue()) {
                System.out.println("Func " + curFunc + " invokes func " + calledFunc);
            }
        }
    }

    /*
     * Task 4: Given AST ID, count the number of all node types
     */

    /*
     * First, you need to obtain all nodes into an arraylist.
     * Then, count the frequency of each node type.
     *
     * Hints: we have prepared some methods for you, e.g., getNodeName.
     *
     * @return: Hashmap that stores the mapping from node name to its frequency.
     */
    public HashMap<String, Integer> calculateNode2Nums(String astID) {
        // TODO: complete the definition of the method `calculateNode2Nums`
        return null;
    }

    public void userInterfaceCountNum() {
        System.out.println("Please specify the AST ID to count Node (" + id2ASTModules.keySet() + ") or -1 for all:");
        Scanner scan1 = new Scanner(System.in);
        if (scan1.hasNextLine()) {
            String astID = scan1.nextLine();
            if (!astID.equals("-1")) {
                if (id2ASTModules.containsKey(astID)) {
                    HashMap<String, Integer> node2Num = calculateNode2Nums(astID);
                    for (Map.Entry<String, Integer> entry : node2Num.entrySet()) {
                        System.out.print(astID + entry.getKey() + " node with frequency " + entry.getValue());
                    }
                }
            } else {
                HashMap<String, Integer> totNode2Num = new HashMap<>();
                for (String key : id2ASTModules.keySet()) {
                    HashMap<String, Integer> node2Num = calculateNode2Nums(key);
                    for (Map.Entry<String, Integer> entry : node2Num.entrySet()) {
                        if (totNode2Num.containsKey(entry.getKey())) {
                            int currentValue = totNode2Num.get(entry.getKey());
                            totNode2Num.put(entry.getKey(), currentValue + entry.getValue());
                        } else {
                            totNode2Num.put(entry.getKey(), entry.getValue());
                        }
                    }
                }
                for (Map.Entry<String, Integer> entry : totNode2Num.entrySet()) {
                    System.out.print("All " + entry.getKey() + " node with frequency " + entry.getValue() + "\n");
                }
            }
        }
    }

    /*
     * Task 5: Sort all functions based on # children nodes
     */

    /*
     * First, you need to find all declarative functions, whose node is FunctionDefStmt.
     * Then, starting from the node, find all children nodes and get the number of children
     * nodes as the complexity of the function.
     *
     * @return: Hashmap that stores the mapping from function name
     *          to the number of children nodes
     */
    public HashMap<String, Integer> processNodeFreq() {
        // TODO: complete the definition of the method `processNodeFreq`
        return null;
    }

    /*
     * Sort the hashmap based on the complexity
     * @return: list of entry whose complexity is sorted in ascending order
     */
    public List<Map.Entry<String, Integer>> sortHashMapByValue(HashMap<String, Integer> map) {
        // TODO: complete the definition of the method `sortHashMapByValue`
        return null;
    }

    public void userInterfaceSortByChild() {
        HashMap<String, Integer> funcName2NodeNum = processNodeFreq();
        List<Map.Entry<String, Integer>> sortedEntries = sortHashMapByValue(funcName2NodeNum);

        for (Map.Entry<String, Integer> entry : sortedEntries) {
            System.out.println("Func " + entry.getKey() + " has complexity " + entry.getValue());
        }
    }

    /*
     * Task 6: Recover the Python code from its AST
     */
    public void userInterfaceRecoverCode() {
        System.out.println("Please specify the AST ID to recover code (" + id2ASTModules.keySet() + ")");
        Scanner scan1 = new Scanner(System.in);
        if (scan1.hasNextLine()) {
            String astID = scan1.nextLine();
            if (id2ASTModules.containsKey(astID)) {
                ASTModule module = id2ASTModules.get(astID);
                System.out.println("Python Code " + astID);
                StringBuilder stringBuilder = new StringBuilder("");
                module.printByPos(stringBuilder);
                System.out.println(stringBuilder);
            } else {
                System.out.println("Invalid AST ID " + astID + "!");
            }
        }
    }
}
