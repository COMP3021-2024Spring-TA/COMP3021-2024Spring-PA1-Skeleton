package hk.ust.comp3021.stmt;

import hk.ust.comp3021.expr.*;
import hk.ust.comp3021.misc.*;
import hk.ust.comp3021.utils.*;
import java.util.*;

public class FunctionDefStmt extends ASTStmt {
    /*
     * FunctionDef(identifier name, arguments args, stmt* body, expr*
     * decorator_list, expr? returns, ..)
     */
    private String name;
    private ASTArguments args;
    private ArrayList<ASTStmt> body = new ArrayList<>();
    private ArrayList<ASTExpr> decoratorList = new ArrayList<>();
    private ASTExpr returns = null;

    public FunctionDefStmt(XMLNode node) {
        // TODO: complete the definition of the constructor. Define the class as the subclass of ASTExpr.
        super(node);
    }

    /*
     * Find all AST node whose class type is `CallExpr` shown in the AST
     * Hints: you need to traverse all the nodes in AST and check its class type.
     * We have prepared the method `getChildren` for you to ease the traversal.
     * You may need to remove the `return null` in the skeleton.
     * */
    public ArrayList<CallExpr> getAllCalledFunc() {
        // TODO: complete the definition of the method `getAllCalledFunc`
        return null;
    }

    public int getParamNum() {
        return args.getParamNum();
    }

    public String getName() {
        return name;
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
