package hk.ust.comp3021.stmt;

import hk.ust.comp3021.expr.*;
import hk.ust.comp3021.misc.*;
import hk.ust.comp3021.utils.*;
import java.util.ArrayList;

public class WhileStmt extends ASTStmt {
    // While(expr test, stmt* body, stmt* orelse)
    private ASTExpr test;
    private ArrayList<ASTStmt> body = new ArrayList<>();
    private ArrayList<ASTStmt> orelse = new ArrayList<>();

    public WhileStmt(XMLNode node) {
        // TODO: complete the definition of the constructor. Define the class as the subclass of ASTExpr.
        super(node);
    }

    @Override
    public ArrayList<ASTElement> getChildren() {
        // TODO: complete the definition of the method `getChildren`
        return null;
    }

    @Override
    public int countChildren() {
        // TODO: complete the definition of the method `countChildren`
        return 0;
    }

    @Override
    public void printByPos(StringBuilder str) {
        // TODO: (Bonus) complete the definition of the method `printByPos`
    }


    /**
     * Attention: You may need to define more methods to update or access the field
     * of the class ASTStmt, i.e., getters or setters Feel free to define more
     * method but remember not
     * (1) removing the fields or methods in our skeleton.
     * (2) changing the type signature of `public` methods
     * (3) changing the modifiers of the fields and methods, e.g., changing a modifier from "private"
     * to "public"
     */
    @Override
    public void yourMethod() {
    }

}
