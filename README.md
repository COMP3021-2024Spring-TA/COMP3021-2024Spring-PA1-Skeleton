# COMP3021 Spring 2024 Java Programming Assignment 1 (PA1)

:warning: Please make sure you always pull the **latest** version of the PA skeleton!

:heavy_exclamation_mark: **Updates** and **Skeleton Clarification**: 
1. `countChildren` abstract method also takes the current node into consideration. You'd better understand its functionality as counting the node of subtree with current node as root node. That is, if a node has no child, the numChild should return 1. Thus, for the sort query task, please also take the FunctionDefStmt root node into consideration as well.
2. Test cases and how to test your codes are updated.
3. To avoid ambiguity, when printing or getting the name of FunctionDefStmt node, we use the format **astID_FuncName_FuncLineNo** to name a function uniquely. For instance, the `horspool` function in #26 AST is started from line 2, so its name is `26_horspool_2`.
4. When printing or getting the name of func field of CallExpr node, we use the format `astID_FuncName_CallLineNo` to name the invoked function. For instance, `horspool` in #26 AST invokes `generateBadCharTable` in line 5, so the invoked function is named as `26_generateBadCharTable_5`.


## Python AST Management System

**[AST (Abstract Syntax Tree)](https://en.wikipedia.org/wiki/Abstract_syntax_tree)** is a tree representation that represents the syntactic structure of source code. It is widely used in compilers and interpreters to reason about relationships between program elements. In this project, you are required to implement your own management system, named **ASTManager**, for parsing and analyzing Python ASTs.

### Grading System

 In PA1, **ASTManager** should support the following functionalities:

- Task 1: Parse the XML files that organize the tree structure of Python ASTs (50%)
- Task 2: Simple query on basic information of given ASTs (5 * 10% = 50%)
- Bonus Task: Recover the Python code from its AST (10%)

Each test case is an XML file that represents a Python AST. We will provide public test cases for you to verify the correctness of your implementations. However, passing all the public test cases does not mean that you can obtain the full mark for the PA. We also have many additional test cases as the hidden ones, which are different from the ones we provided in the skeleton.

Before task specification, we first explain the grading policy as follows for your reference so that you will not miss it.

| Item                                             | Ratio | Notes                                                        |
| ------------------------------------------------ | ----- | ------------------------------------------------------------ |
| Keeping your GitHub repository private           | 5%    | You must keep your repository **priavte** at all times.      |
| Having at least three commits on different days  | 5%    | You should commit three times during different days in your repository |
| Code style                                       | 10%   | You get 10% by default, and every 5 warnings from CheckStyle deducts 1%. |
| Public test cases (Task 1 + Task 2 + Bonus Task) | 30%   | (# of passing tests / # of provided tests) * 30%             |
| Hidden test cases (Task 1 + Task 2 + Bonus Task) | 50%   | (# of passing tests / # of provided tests) * 50%             |

### Python ASTs 

We now provide essential background about Python AST for you. The AST captures the essential elements of programs' syntax. Specifically, each node in AST denotes a specific program element in source code, such as operators, functions, statements, and expressions. Taking the following simple Python code as an instance, the function `add` computes the sum of two arguments `a` and `b`. The results are stored in variable `c` and returned as the return value.

```python
def add(a, b):
    c = a + b
    return c
```

The AST of the Python code is shown below. Each AST node has a defined structure, consisting of **node type**, **attributes**, and **child nodes**. 

<img src="./AST_Example.png" alt="example" style="zoom:10%;" />

For instance, `FunctionDef` is the node type, and its attribute `name` is `add`. Such node has three child nodes, which are the arguments and body of function `add`, i.e., `arguments`, `Assign`, and `Return`. Note that the node attributes are optional and vary based on the node type. For instance, the attributes of node type `Name` are `id` and `ctx`, which represent the corresponding variable name and whether the variable is read or written. We can notice that the nodes in green essentially represent the addition operation of two variables `a` and `b` in the second line of Python code.

The above example only shows sampled program elements in Python. Please refer to the Abstract Grammar section of this [document](https://docs.python.org/3/library/ast.html) to access the complete ASDL (Abstract Syntax Description Language) for all node types in Python. Let's explain the following grammar of `BinOp` as an example. 

```python
expr = ...
       | BinOp(expr left, operator op, expr right)
       ...
       | Name(identifier id, expr_context ctx)
      
expr_context = Load | Store | Del
operator     = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
                   | RShift | BitOr | BitXor | BitAnd | FloorDiv
```

The above grammar for `BinOp` node indicates:

- `BinOp` is a binary expression with two operands and one operator.
- `BinOp` has two fields, `left` and `right`, which are the left and right operands of binary expression. These two fields are expressions as well, which could be binary expressions or other expression types. 
- If the operands of binary expression is a variable, the node type would be `Name`, whose field `id` represents the variable name and `ctx` marks whether the value of the variable is read or written. For instance, `Load` means the value of the variable is read here. 
- `BinOp` has a field, `op`, which is the operator of the binary expression. The operator could be `Add`, `Sub`, etc.

In PA1, you need to implement the classes of nodes defined in the grammar. In the following, we provide more concrete specifications for related classes, their fields, and methods in the provided skeleton.

### Classes

#### Element Superclass

The skeleton contains one base class `ASTElement`, which is almost the super class of all classes in PA1. `ASTElement` has four fields as follows:

- `lineno: int`: the first line number of elements in code
- `colOffset: int`: the UTF-8 byte offset of the first token of the element in the source code
- `endLineno: int`: the end line number of the element in the code
- `endColOffset: int`: the UTF-8 byte offset of the last token of the element in the source code

Except for fields, there are three abstract methods shown as follows. Please refer to the skeleton to understand their functionalities. For all subclass of `ASTElement`, you need to implement these three abstract methods.

- `public abstract ArrayList<ASTElement> getChildren();`
- `public abstract int countChildren();`
- `public abstract void printByPos(StringBuilder str);`

The ASTs being managed are obtained by parsing XML files. Therefore, the constructor of  `ASTElement` takes an XML node as input and initializes essential fields given the information provided by XML nodes. You should implement the constructor for all subclasses of `ASTElement` as well.  You may need to define more methods according to your needs during the development.

#### Stmt SubClasses

`ASTStmt` is the subclass of `ASTElement`, which represents statements.  `ASTStmt` has one more field `protected StmtType stmtType;`, which represents the specific statement type.

The class `ASTStmt` has 11 subclasses according to the following AST grammar. 

```
stmt = FunctionDef(identifier name, arguments args,
                       stmt* body, expr* decorator_list, expr? returns,
                       ...)
          ...
          | Assign(expr* targets, expr value, ...)
          ...

```

Note that we have simplified the input ASTs, thus not all stmt declared in AST grammar need to be implemented.  We outline the fields of two of them as examples.

- The class `FunctionDefStmt` has 5 fields.
  -  `name: String`: function name, e.g., `name` for function example shown above is `add`.
  -  `args: ASTArguments`: function arguments, which corresponds to the `arguments` node in AST example above.
  -  `body: ArrayList<ASTStmt>`: function body. `*` means `body` contains a list of statements. As shown in the above `add` function, its body is composed of two statements.
  -  `decoratorList: ArrayList<ASTExpr>`: a list of decorators. For `add` function, the ArrayList `decoratorList` has zero elements.
  -  `returns: ASTExpr`: return annotation. `?` means `returns` are optional. For instance, the `returns` field for function `add` is `null`. Please initialize it carefully when buidling AST.
- The class `AssignStmt` has 2 fields, i.e., `targets: ArrayList<ASTExpr>`, `value: ASTExpr`.

Similarly, all fields of these classes should be private. You need to implement essential methods of these 11 classes, including constructors. To convenience your implementation, we have provided the skeleton of these 11 classes. For a more detailed explanation of fields and methods, you can refer to the class files under the directory `src/main/java/hk.ust.comp3021/stmt`.

#### Expr SubClasses

`ASTExpr` is the subclass of `ASTElement`, which represents expressions.  `ASTExpr` has one more field `protected ExprType exprType`, which represents the specific expression type.

The class `ASTExpr` has 11 subclasses. We outline the fields of three of them as examples.

```
 expr = BoolOp(boolop op, expr* values)
         ...
         | BinOp(expr left, operator op, expr right)
         ...
         | Name(identifier id, expr_context ctx)
         ...
```

- The class `BoolOpExpr` has two fields, i.e., boolean operator `op: ASTEnumOp` and a list of expression `values: ArrayList<ASTExpr>`.
- The class `BinOpExpr` has three fields, i.e., binary operator `op: ASTEnumOp`, left operand expression `left: ASTExpr`, and right operand expression `right: ASTExpr`.
- The class `NameExpr` has two fields, i.e., variable name `id: String` and `crx: ASTEnumOp`.

You can refer to the class files under the directory `src/main/java/hk.ust.comp3021/expr` for more details. Similar to `Stmt` and its subclasses, you need to implement essential methods of these 11 subclasses to support the desired functionality.

#### Misc SubClasses

Several types haven't been introduced but are used when implementing the above subclasses. Please implement them according to the AST grammar. 

```
keyword = (identifier? arg, expr value)
          attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)
```

For instance, we use  `ASTKeyword` as the class describing `keyword` in AST grammar, which contains six fields, i.e., `arg: String`, `value: ASTExpr`, `lineno: int`, `col_offset: int`, `end_lineno: int` and `end_col_offset: int`.

You can refer to the class files under the directory `src/main/java/hk.ust.comp3021/misc` for more details.

### Utils

To support AST parsing, managing, and analyzing, we provide three classes as follows in the directory `src/main/java/hk.ust.comp3021/utils`.

#### ASTModule

`ASTModule` is one subclass of `ASTElement`, which represents the root nodes of ASTs. Its AST grammar is shown below.

```
mod = Module(stmt* body, type_ignore* type_ignores)
```

According to the AST grammar of Module, the class `ASTModule` has two fields, i.e., lists of body statements `body: ArrayList<Stmt>` and unique ID of current AST `astID: int`.

Each AST corresponds to a Python source file. The `astID` is also used to find the path to the XML file and corresponding Python code. For instance, given `astID` as 1, the XML file and Python file are `resources/pythonxml/python_1.xml` and `resources/pythonxml/python_1.py`, respectively.

All fields of `ASTModule` should be private. You should implement all methods we marked as `TODO`. Besides, you may need to define more methods according to your needs during the development, such as `getter` or `setter` to access private fields from other classes.

#### ASTParser

We provide Python ASTs in XML files under the directory `resources/pythonxml/`. Each XML file corresponds to an object in `ASTModule` class. 

`ASTParser` parses a given XML file that organizes the AST tree structure and extracts corresponding objects. If the parsing succeeds, you should set `isErr` to `false`. Otherwise, it should be set to `true`. An example of the XML file is `resources/pythonxml/python_0.xml`. 

We use the following XML snippet for the green nodes in the aforementioned AST example to explain the XML format.

```xml
<BinOp lineno="2" col_offset="8" end_lineno="2" end_col_offset="13">
  <Name id="a" lineno="2" col_offset="8" end_lineno="2" end_col_offset="9">
    <Load/>
  </Name>
  <Add/>
  <Name id="b" lineno="2" col_offset="12" end_lineno="2" end_col_offset="13">
    <Load/>
  </Name>
</BinOp>
```

- **Elements:** The basic building blocks of the XML document are elements, which consist of start tags, contents, and end tags. For instance, `Name` element starts with the tag `<Name>` and ends with `<\Name>`. Alternatively, the tag can be self-closing, such as `<Load/>`, indicating the element does not contain any content and child elements. 
- **Attributes:** Elements can have attributes, which provide additional information about elements. Attributes are defined within the start tag. For instance, `<Name id="c" lineno="2" col_offset="4" end_lineno="2" end_col_offset="5">` indicates the `id` field of the `Name` element is `c`. 
- **Hierarchy**: Elements in XML documents are nested within each other to form a tree structure. The tree structures of the above XML snippet are shown below, which is consistent with the green nodes in the aforementioned AST.

```
BinOp (attributes: lineno="2", col_offset="8", end_lineno="2", end_col_offset="13")
├── Name (attributes: id="a", lineno="2", col_offset="8", end_lineno="2", end_col_offset="9")
│   └── Load
├── Add
└── Name (attributes: id="b", lineno="2", col_offset="12", end_lineno="2", end_col_offset="13")
    └── Load
```

When you parse the file, you can assume that all the XML files in our test cases are legal. Note that you are not allowed to invoke library functions to parse XML files directly.

#### XMLNode

Considering that creating the AST during XML file parsing is too complicated, we choose to first parse the XML tree structure into `XMLNode` and later construct the AST from XML tree.

`XMLNode` is a general class for all XML elements, and it contains four fields:

- `tagName: String`: the tag name of the current XML node, e.g., BinOp, Name, Add, etc.
- `attributes: Map<String, String>`: attributes of current XML node in key-value pairs format
- `children: List<XMLNode>`: children XML nodes
- `parent: XMLNode`: the parent XML node

When handling XML file, we explain how to get these four fields by taking the above `BinOp` node as an example:

- The tagName is `BinOp`
- The attributes are four key-value pairs 
  - lineno: 2
  - col_offset: 8
  - end_lineno: 2
  - end_col_offset: 13
- The `BinOp` node has three children whose tag name is Name, Add and Name, respectively.
- The parent of `BinOp` is not shown in the XML snippet. But the `parent` of `Add` node is `BinOp`.

If an XML element is self-closing, such as `<Add/>`, it indicates the node has no attribute and children. We have implemented the `XMLNode` class for you. Please carefully consider the mapping between XMLNode and the corresponding AST node when creating AST from the XML tree. You can search for tagName among given XML files to learn the mapping.


### Bouns Task

The bonus task unparses a tree structure of AST back to its original Python code. For instance, after you parsing the XML file that represents the AST shown in the above example, the bonus task takes charge of generating the original Python code as follows.

```python
def add(a, b):
    c = a + b
    return c
```

**Hints.** Essentially, you can regard the process as a customized preorder tree traversal. During tree traversal, starting from the root node, you can examine each node in the AST and generate corresponding Python code based on its type and attributes. For instance, if you encounter a `FunctionDef` node with an attribute `name` to be `add`, the generated Python code is `def add(...)`.

Let's go through the preorder traversal of the aforementioned AST example to help you understand the unparsing process. The traversal sequence and code generation process are shown as follows.

```
Module -> FunctionDef (name: add)                           =>  def add(...):
       -> arguments -> arg (arg: a) 
                    -> arg (arg: b)                         =>  def add(a, b):
       -> Assign -> Name (id: c, ctx: Store)                =>      c = ...
                 -> BinOp -> Name (id: a, ctx: Load)    
                          -> Add
                          -> Name (id: b, ctx: Load)        =>      c = a + b
       -> Return -> Name (id: c, ctx: Load)                 =>      return c
       
```

The code generating process involves handling different node types and their attributes. Each node type has specific attributes that need to be considered. Noticed that Python code is sensitive to indentation, which determines the scope of statements within a block. Please carefully handle the indentation and follow the rules to ensure the reconstructed code is legal and readable.  

**Hints.** You can use the four fields `lineno`, `colOffset`, `endLineNo` and `endColOffset` to help you find the position of each AST element.

### ASTManager and ASTManagerEngine

The class `ASTManager` is the main class of our system, which wraps an `ASTManagerEngine` inside. The method `userInterface` of `ASTManagerEngine` processes the following analysis commands from the console and invokes corresponding handlers.
   - Given AST ID, parse AST from XML files
   - Print all functions with # arguments greater than user-specified N
   - Find the most commonly used operators in all ASTs
   - Print all function names and the functions invoked by each function
   - Given AST ID, count the number of all node types.
   - Sort all functions based on # children nodes
   - Bonus Task: Given AST ID, recover Python Code

### What YOU need to do

We have marked the methods you need to implement using `TODO` in the skeleton. Specifically, please

- Fully define the `ASTStmt` and its subclasses, including their constructors and other necessary methods.
- Fully define the class `ASTExpr` and its subclasses, including their constructors and other necessary methods.
- Fully implement `ASTParser` and `ASTModule`.
- Fully implement the methods in the class `ASTManageEngine`.
  - calculateOp2Nums
  - mostCommonUsedOp
  - calculateCalledFunc
  - calculateNode2Nums
  - processNodeFreq
  - sortHashMapByValue

You need to follow the comments on the methods to be implemented in the provided skeleton. We have provided detailed descriptions and even several hints for these methods. To convenience the testing and debugging, you can just run the `main` method of `ASTManager` to interact with the system.

We use the JUnit test to verify the functionalities of all methods you implement. Please do not modify the type signatures of these functions.

### How to TEST

Public test cases are released in `src/test/java/hk.ust.comp3021/ASTManagerEngineTest.java`. Please try to test your code with `./gradlew test` before submission to ensure your implementation can pass all public test cases.

We use JUnit test to validate the correctness of individual methods that you need to implement. The mapping between public test cases and methods to be tested are shown below.

| Test Case      | Target Method |
| ----------- | ----------- |
| `testParse2XMLNode`        | `parser.parse2XMLNode`    |
| `testPrintedInformation`   | `engine.findFuncWithArgGtN`  |
| `testCalculateOp2Nums` | `engine.calculateOp2Nums` |
| `testMostCommonUsedOp` | `engine.mostCommonUsedOp` |
| `testCalculateNode2Num` | `engine.calculateNode2Nums` |
| `testCalledFuncOnXML1` | `engine.calculateCalledFunc` |
| `testProcessNodeFreq` | `engine.processNodeFreq` |
| `testSortHashMapByValue` | `engine.sortHashMapByValue` |
| `testBonusPrintByPos` | `module.printByPos` (For Bonus Task Only) |

You can fix the problem of your implementation based on the failed test cases. We would not provide test cases for 


### Submission Policy

Please submit your code on Canvas before the deadline **March 23, 2024, 23:59:59.** You should submit a single text file specified as follows:

- A file named `<itsc-id>.txt` containing the URL of your private repository at the first line. We will ask you to add the TA's account `COMP3021-2024Spring-TA` as a collaborator near the deadline.

For example, a student CHAN, Tai Man with ITSC ID `tmchanaa` having a repository at `https://github.com/tai-man-chan/COMP3021-PA1` should submit a file named `tmchanaa.txt` with the following content:

```txt
https://github.com/tai-man-chan/COMP3021-PA1
```

Note that we are using automatic scripts to process your submission on test cases rather than testing via the console manually. **DO NOT add extra explanation** to the file; otherwise, they will prevent our scripts from correctly processing your submission. 

**We will grade your submission based on the latest committed version before the deadline.** Please make sure all the amendments are made before the deadline and do not make changes after the deadline.

We have pre-configured a gradle task to check style for you. You can run `./gradlew checkstyleMain` to check style. Before submission, please make sure that: 

1. Your code can be complied with successfully. Please try to compile your code with `./gradlew build` before submission. You will not get any marks for public/hidden test cases if your code cannot be successfully compiled.
2. Your implementation can pass the public test cases we provided in `src/test`.
3. Your implementation should not yield too many errors when running `./gradlew checkstyleMain`.

### Academic Integrity

We trust that you are familiar with the Honor Code of HKUST. If not, refer to [this page](https://course.cse.ust.hk/comp3021/#policy).

### Contact US

If you have any questions on the PA1, please email TA Wei Chen via wei.chen@connect.ust.hk

---

Last Update: Feb 24, 2024
