package hk.ust.comp3021.utils;

public class ASTParser {
    private final String xmlFileID;
    private boolean isErr;
    private XMLNode rootXMLNode;
    private ASTModule rootASTModule;

    public ASTParser(String xmlFileID) {
        this.xmlFileID = xmlFileID;

        this.isErr = false;
        this.rootXMLNode = null;
        this.rootASTModule = null;
    }

    public boolean isErr() {
        return isErr;
    }

    public ASTModule getASTModule() {
        return rootASTModule;
    }

    public void parse() {
        // parse the XML Tree into rootXMLNode
        parse2XMLNode();
        // obtain the module node as the first child of ast node
        rootXMLNode = rootXMLNode.getChildByIdx(0);
        // create AST Tree and return the root node ASTModule
        rootASTModule = new ASTModule(rootXMLNode, xmlFileID);
    }

    /**
     * 1. Parse the XML Tree inside given XML File whose path is `xmlFilePath`
     * 2. Initialize the rootXMLNode as the root node of XML Tree, the tag Name of rootXMLNode should be ast
     * 3. If any exception throws, please set the field `isErr` to true. Otherwise, `isErr` is false.
     *
     * Hints:
     * For the following XML snippet:
     * <Assign type_comment="None" lineno="4" col_offset="8" end_lineno="4" end_col_offset="19">
     *     <targets>
     *         <Name id="tail" lineno="4" col_offset="8" end_lineno="4" end_col_offset="12">
     *             <Store/>
     *         </Name>
     *     </targets>
     *     <Constant value="None" kind="None" lineno="4" col_offset="15" end_lineno="4" end_col_offset="19"/>
     * </Assign>
     *
     * There are five XML nodes in total. Each XMLNode has two fields, i.e., attributes and children.
     * Attributes are key-value pairs. For instance, for xml node whose tag is Assign, the key-value pairs contains
     * `id: tail`. Children are a list of XMLNode, for instance, for Assign node, it has two children (targets, Constant).
     *
     * Noticed that in each line, there could be a self-closing tag, e.g., <Store/>, or a closing tag, e.g., </Name>, or
     * an opening tag <Name>. Please carefully organize the parent-children relation and initialize the attributes.
     *
     */
    public void parse2XMLNode() {
        // TODO: complete the definition of the method `parse2XMLNode`
    }

    /**
     * Attention: You may need to define more methods to parse XML file
     * Feel free to define more method but remember not
     * (1) removing the fields or methods in our skeleton.
     * (2) changing the type signature of `public` methods
     * (3) changing the modifiers of the fields and methods, e.g., changing a modifier from "private" to "public"
     */
    public void yourMethod() {

    }
}
