package hk.ust.comp3021.stmt;

import hk.ust.comp3021.misc.*;
import hk.ust.comp3021.utils.*;
import java.util.*;

public class BreakStmt extends ASTStmt {
    public BreakStmt(XMLNode node) {
        super(node);
    }
    @Override
    public ArrayList<ASTElement> getChildren() {
        ArrayList<ASTElement> children = new ArrayList<>();
        return children;
    }
    @Override
    public int countChildren() {
        int numChild = 1;
        return numChild;
    }
    @Override
    public void printByPos(StringBuilder str) {
        this.fillStartBlanks(str);
        str.append("break");
        this.fillEndBlanks(str);
    }
}
