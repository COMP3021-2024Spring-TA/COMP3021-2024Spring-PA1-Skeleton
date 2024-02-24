package hk.ust.comp3021.misc;

import hk.ust.comp3021.utils.*;
import java.util.ArrayList;


public class ASTEnumOp extends ASTElement {

    /*
     * expr_context = Load | Store | Del
     *
     * boolop = And | Or
     *
     * operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift | RShift |
     * BitOr | BitXor | BitAnd | FloorDiv
     *
     * unaryop = Invert | Not | UAdd | USub
     *
     * cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn
     */

    public enum ASTOperator {
        Ctx_Load, Ctx_Store, Ctx_Del,
        OP_And, OP_Or,
        OP_Add, OP_Sub, OP_Mult, OP_MatMult, OP_Div, OP_Mod, OP_Pow, OP_LShift, OP_RShift, OP_BitOr, OP_BitXor,
        OP_BitAnd, OP_FloorDiv,
        OP_Invert, OP_Not, OP_UAdd, OP_USub,
        OP_Eq, OP_NotEq, OP_Lt, OP_LtE, OP_Gt, OP_GtE, OP_Is, OP_IsNot, OP_In, OP_NotIn
    }

    private ASTOperator op;

    public ASTEnumOp(XMLNode node) {
        switch (node.getTagName()) {
        case "Load":
            this.op = ASTOperator.Ctx_Load;
            break;
        case "Store":
            this.op = ASTOperator.Ctx_Store;
            break;
        case "Del":
            this.op = ASTOperator.Ctx_Del;
            break;
        case "And":
            this.op = ASTOperator.OP_And;
            break;
        case "Or":
            this.op = ASTOperator.OP_Or;
            break;
        case "Add":
            this.op = ASTOperator.OP_Add;
            break;
        case "Sub":
            this.op = ASTOperator.OP_Sub;
            break;
        case "Mult":
            this.op = ASTOperator.OP_Mult;
            break;
        case "MatMult":
            this.op = ASTOperator.OP_MatMult;
            break;
        case "Div":
            this.op = ASTOperator.OP_Div;
            break;
        case "Mod":
            this.op = ASTOperator.OP_Mod;
            break;
        case "Pow":
            this.op = ASTOperator.OP_Pow;
            break;
        case "LShift":
            this.op = ASTOperator.OP_LShift;
            break;
        case "RShift":
            this.op = ASTOperator.OP_RShift;
            break;
        case "BitOr":
            this.op = ASTOperator.OP_BitOr;
            break;
        case "BitXor":
            this.op = ASTOperator.OP_BitXor;
            break;
        case "BitAnd":
            this.op = ASTOperator.OP_BitAnd;
            break;
        case "FloorDiv":
            this.op = ASTOperator.OP_FloorDiv;
            break;
        case "Invert":
            this.op = ASTOperator.OP_Invert;
            break;
        case "Not":
            this.op = ASTOperator.OP_Not;
            break;
        case "UAdd":
            this.op = ASTOperator.OP_UAdd;
            break;
        case "USub":
            this.op = ASTOperator.OP_USub;
            break;
        case "Eq":
            this.op = ASTOperator.OP_Eq;
            break;
        case "NotEq":
            this.op = ASTOperator.OP_NotEq;
            break;
        case "Lt":
            this.op = ASTOperator.OP_Lt;
            break;
        case "LtE":
            this.op = ASTOperator.OP_LtE;
            break;
        case "Gt":
            this.op = ASTOperator.OP_Gt;
            break;
        case "GtE":
            this.op = ASTOperator.OP_GtE;
            break;
        case "Is":
            this.op = ASTOperator.OP_Is;
            break;
        case "IsNot":
            this.op = ASTOperator.OP_IsNot;
            break;
        case "In":
            this.op = ASTOperator.OP_In;
            break;
        case "NotIn":
            this.op = ASTOperator.OP_NotIn;
            break;
        default:
            throw new IllegalArgumentException("Unsupported tag name: " + node.getTagName());
        }
    }

    public String getOperatorName() {
        String name = this.op.name();
        if (name.startsWith("OP_")) {
            return name.substring(3);
        }
        return "";
    }

    @Override
    public ArrayList<ASTElement> getChildren() {
        ArrayList<ASTElement> children = new ArrayList<>();
        return children;
    }

    @Override
    public int countChildren() {
        return 0;
    }

    @Override
    public String getNodeType() {
        return this.op.name();
    }

    @Override
    public void printByPos(StringBuilder str) {
        switch (this.op) {
            case OP_And:
                str.append("and");
                break;
            case OP_Or:
                str.append("or");
                break;
            case OP_Add:
                str.append("+");
                break;
            case OP_Sub:
                str.append("-");
                break;
            case OP_Mult:
                str.append("*");
                break;
            case OP_MatMult:
                str.append("@");
                break;
            case OP_Div:
                str.append("/");
                break;
            case OP_Mod:
                str.append("%");
                break;
            case OP_Pow:
                str.append("**");
                break;
            case OP_LShift:
                str.append("<<");
                break;
            case OP_RShift:
                str.append(">>");
                break;
            case OP_BitOr:
                str.append("|");
                break;
            case OP_BitXor:
                str.append("^");
                break;
            case OP_BitAnd:
                str.append("&");
                break;
            case OP_FloorDiv:
                str.append("//");
                break;
            case OP_Invert:
                str.append("~");
                break;
            case OP_Not:
                str.append("not");
                break;
            case OP_UAdd:
                str.append("+");
                break;
            case OP_USub:
                str.append("-");
                break;
            case OP_Eq:
                str.append("==");
                break;
            case OP_NotEq:
                str.append("!=");
                break;
            case OP_Lt:
                str.append("<");
                break;
            case OP_LtE:
                str.append("<=");
                break;
            case OP_Gt:
                str.append(">");
                break;
            case OP_GtE:
                str.append(">=");
                break;
            case OP_Is:
                str.append("is");
                break;
            case OP_IsNot:
                str.append("is not");
                break;
            case OP_In:
                str.append("in");
                break;
            case OP_NotIn:
                str.append("not in");
                break;
            default:
                str.append("unknown operator");
                break;
        }
    }

}
