package hk.ust.comp3021.expr;

import hk.ust.comp3021.misc.*;
import hk.ust.comp3021.utils.*;
import java.util.*;

public class CallExpr extends ASTExpr {
    // Call(expr func, expr* args, keyword* keywords)
    private ASTExpr func;
    private ArrayList<ASTExpr> args = new ArrayList<>();
    private ArrayList<ASTKeyWord> keywords = new ArrayList<>();

    public CallExpr(XMLNode node) {
        // TODO: complete the definition of the constructor. Define the class as the subclass of ASTExpr.
        super(node);
    }

    /*
     * Find all paths from func node to node with class type Name, which contain several cases
     * (1) if the path is func -> Attribute (attr: b) -> Name (id: self), then the name is self.b
     * (2) if the path is func -> Attribute (attr: b) -> Attribute (attr: a) -> Name (id: self), then the name is self.a.b
     * (3) if the path is func -> Name (id: bubbleSort), then the name is bubbleSort
     * @return: name of called function
     */
    public String getCalledFuncName() {
        // TODO: complete the definitaion of the method `getCalledFuncName`
        return "";
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
     * Attention: You may need to define more methods to update or access the field of the class `User`
     * Feel free to define more method but remember not
     * (1) removing the fields or methods in our skeleton.
     * (2) changing the type signature of `public` methods
     * (3) changing the modifiers of the fields and methods, e.g., changing a modifier from "private" to "public"
     */
    public void yourMethod() {

    }

}
