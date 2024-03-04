package hk.ust.comp3021.misc;

import hk.ust.comp3021.utils.*;
import java.util.*;

public abstract class ASTElement {
    private int lineno;
    private int colOffset;
    private int endLineno;
    private int endColOffset;

    public ASTElement() {
        this.lineno = -1;
        this.colOffset = -1;
        this.endLineno = -1;
        this.endColOffset = -1;
    }


    public ASTElement(int lineno, int colOffset, int endLineno, int endColOffset) {
        this.lineno = lineno;
        this.colOffset = colOffset;
        this.endLineno = endLineno;
        this.endColOffset = endColOffset;
    }
    public ASTElement(XMLNode node) {
        if (node.hasAttribute("lineno")) {
            this.lineno = Integer.parseInt(node.getAttribute("lineno"));
        }
        if (node.hasAttribute("col_offset")) {
            this.colOffset = Integer.parseInt(node.getAttribute("col_offset"));
        }
        if (node.hasAttribute("end_lineno")) {
            this.endLineno = Integer.parseInt(node.getAttribute("end_lineno"));
        }
        if (node.hasAttribute("end_col_offset")) {
            this.endColOffset = Integer.parseInt(node.getAttribute("end_col_offset"));
        }
    }

    public int getLineNo() {
        return this.lineno;
    }

    public int getColOffset() {
        return this.colOffset;
    }

    public int getEndLineNo() {
        return this.endLineno;
    }

    public int getEndColOffset() {
        return this.endColOffset;
    }

    public static int countNowLineNo(StringBuilder str) {
        int frequency = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '\n') {
                frequency++;
            }
        }
        return frequency;
    }

    public static int countNowColOffset(StringBuilder str) {
        String splitedStr = str.toString();
        String[] lines = splitedStr.split("\n");
        String lastLine = lines[lines.length - 1];
        return lastLine.length();
    }

    public void fillStartBlanks(StringBuilder str) {
        int curLineNo = countNowLineNo(str) + 1;
        int curColOffset = countNowColOffset(str);

        str.append("\n".repeat(this.getLineNo() - curLineNo));
        if (this.getLineNo() == curLineNo) {
            str.append(" ".repeat(this.getColOffset() - curColOffset));
        } else {
            str.append(" ".repeat(this.getColOffset()));
        }
    }

    public void fillEndBlanks(StringBuilder str) {
        int curLineNo = countNowLineNo(str) + 1;
        int curColOffset = countNowColOffset(str);

        str.append("\n".repeat(this.getEndLineNo() - curLineNo));
        str.append(" ".repeat(this.getEndColOffset() - curColOffset));
    }

    public abstract String getNodeType();

    /*
     * Three abstract methods in ASTElement. You need to implement them in subclasses.
     */

    /*
     * Print the corresponding Python Code from current AST Node (Bonus Task)
     * Please learn the mapping between AST node and their Python code from given resources
     * We have provided several functions for you to ease the implementation
     * (1) countNowLineNo: count how many lines so far in the given str, which is the current line number
     * (2) countNowColOffset: count how many characters in the last line, which is the current column offset
     * (3) fillStartBlanks: add essential blanks and new lines to make sure the lineNo and colOffset of str are equal to
     *     the required lineNo and colOffset of current node.
     * (4) fillEndBlanks: add essential blanks and new lines to make sure the lineNo and colOffset of str are equal to
     *     the required endLineNo and endColOffset of current node.
     */
    public abstract void printByPos(StringBuilder str);

    /*
     * Return direct children of current node, which are fields whose type is `ASTElement`.
     * Noticed that field whose class type is `ASTEnumOp` should not be regarded as children.
     */
    public abstract ArrayList<ASTElement> getChildren();

    /*
     * Count the number of descendants of current node.
     * Noticed that you need to count both the number of direct children and all descendants
     */
    public abstract int countChildren();
}
