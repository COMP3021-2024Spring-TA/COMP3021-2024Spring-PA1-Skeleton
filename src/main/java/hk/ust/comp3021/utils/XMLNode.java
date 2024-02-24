package hk.ust.comp3021.utils;

import java.util.*;

public class XMLNode {
    private String tagName;
    private Map<String, String> attributes;
    private List<XMLNode> children;
    private XMLNode parent;

    public XMLNode(String tagName) {
        this.tagName = tagName;
        this.attributes = new HashMap<>();
        this.children = new ArrayList<>();
    }

    public String getTagName() {
        return tagName;
    }

    public Map<String, String> getAttributes() {
        return attributes;
    }

    public boolean hasAttribute(String attributeName) {
        return attributes.containsKey(attributeName);
    }

    public String getAttribute(String attributeName) {
        return attributes.get(attributeName);
    }

    public List<XMLNode> getChildren() {
        return children;
    }

    public XMLNode getChildByIdx(int idx) {
        return children.get(idx);
    }

    public int getNumChildren() {
        return children.size();
    }

    public void addChild(XMLNode child) {
        children.add(child);
        child.setParent(this);
    }

    public XMLNode getParent() {
        return parent;
    }

    public void setParent(XMLNode parent) {
        this.parent = parent;
    }
}
