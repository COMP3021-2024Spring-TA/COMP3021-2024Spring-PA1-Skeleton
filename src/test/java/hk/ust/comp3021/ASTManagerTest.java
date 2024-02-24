package hk.ust.comp3021;

import hk.ust.comp3021.utils.TestExtension;
import hk.ust.comp3021.utils.TestKind;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import java.util.Date;

@ExtendWith(TestExtension.class)
class ASTManagerTest {
    @Tag(TestKind.PUBLIC)
    @Test
    void testPaperParser() {
    	ASTManagerEngine engine = new ASTManagerEngine();
    }

    @Tag(TestKind.PUBLIC)
    @Test
    void testUserRegister() {
        ASTManagerEngine engine = new ASTManagerEngine();
    }
}