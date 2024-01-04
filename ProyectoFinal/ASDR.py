#Entrega lunes en la noche
import sys

class ExprAssign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"ExprAssign({self.name}{self.value})"

class ExprBinary:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"ExprBinary({self.left}{self.operator}{self.right})"

class ExprCallFunction:
    def __init__(self, callee, arguments):
        self.callee = callee
        self.arguments = arguments

    def __str__(self):
        return f"ExprCallFunction({self.callee}{self.arguments})"

#class Expression:  (abstract class (?))
#    def __init__(self):
#        pass

class ExprGet:
    def __init__(self, object, name):
        self.object = object
        self.name = name

    def __str__(self):
        return f"ExprGet({self.object}{self.name})"
class ExprGrouping:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"ExprGrouping({self.expression})"

class ExprLiteral:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"ExprLiteral({self.value})"

class ExprLogical:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"ExprLogical({self.left}{self.operator}{self.right})"
class ExprSet:
    def __init__(self, object, name, value):
        self.object = object
        self.name = name
        self.value = value

    def __str__(self):
        return f"ExprSet({self.object}{self.name}{self.value})"
class ExprSuper:
    def __init__(self, method):
        self.method = method

    def __str__(self):
        return f"ExprSuper({self.method})"
class ExprThis:
    def __init__(self):
        pass

class ExprUnary:
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"ExprUnary({self.operator}{self.right})"
class ExprVariable:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"ExprVariable({self.name})"
#class Statement:  (abstract class (?))
#    def __init__(self):
#        pass

class StmtBlock:
    def __init__(self, statements):
        self.statements = statements

    def __str__(self):
        return f"StmtBlock({self.statements})"

#class StmtClass:
#    def __init__(self, name, superclass, methods):
#        self.name = name
#        self.superclass = superclass
#        self.methods = methods

class StmtExpression:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"StmtExpression({self.expression})"

class StmtFunction:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body
    def __str__(self):
        return f"StmtFunction({self.name}{self.params}{self.body})"
class StmtIf:
    def __init__(self, condition, thenBranch, elseBranch):
        self.condition = condition
        self.thenBranch = thenBranch
        self.elseBranch = elseBranch

    def __str__(self):
        return f"StmtIf({self.condition}{self.thenBranch}{self.elseBranch})"

class StmtLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    def __str__(self):
        return f"StmtLoop({self.condition}{self.body})"
class StmtPrint:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"StmtPrint({self.expression})"

class StmtReturn:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"StmtReturn({self.value})"
class StmtVar:
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer

    def __str__(self):
        return f"StmtVar({self.name}{self.initializer})"
class TipoToken:
    #Tokens de un solo caracter
    LEFT_PAREN = 'LEFT_PAREN'
    RIGHT_PAREN = 'RIGHT_PAREN'
    LEFT_BRACE = 'LEFT_BRACE'
    RIGHT_BRACE = 'RIGHT_BRACE'
    COMMA = 'COMMA'
    DOT = 'DOT'
    MINUS = 'MINUS'
    PLUS = 'PLUS'
    SEMICOLON = 'SEMICOLON'
    SLASH = 'SLASH'
    STAR = 'STAR'

    #Tokens de uno o dos caracteres
    BANG = 'BANG'
    BANG_EQUAL = 'BANG_EQUAL'
    EQUAL = 'EQUAL'
    EQUAL_EQUAL = 'EQUAL_EQUAL'
    GREATER = 'GREATER'
    GREATER_EQUAL = 'GREATER_EQUAL'
    LESS = 'LESS'
    LESS_EQUAL = 'LESS_EQUAL'

    #Literales

    IDENTIFIER = 'IDENTIFIER'
    STRING = 'STRING'
    NUMBER = 'NUMBER'

    #Palabras clave
    AND = 'AND'
    ELSE = 'ELSE'
    FALSE = 'FALSE'
    FUN = 'FUN'
    FOR = 'FOR'
    IF = 'IF'
    NULL = 'NULL'
    OR = 'OR'
    PRINT = 'PRINT'
    RETURN = 'RETURN'
    TRUE = 'TRUE'
    VAR = 'VAR'
    WHILE = 'WHILE'

    EOF = 'EOF'

class ASDR:
    
    def __init__(self, tokens):
        self.i = 0
        self.hayErrores = False
        self.tokens = tokens
        self.preanalisis = self.tokens[self.i]

    def parse(self):
        self.program()

        if self.preanalisis['tipo'] == TipoToken.EOF and not self.hayErrores:
            print("Consulta correcta.")
            return True
        else:
            print("Se encontraron errores.")
            return False

    # PROGRAM -> DECLARATION
    def program(self):
        statements = []
        value = self.declaration(statements)
        for i in value:
            print(f'Aqui {i}')

#Declaraciones
    # DECLARATION -> FUN_DECL DECLARATION
    # DECLARATION -> VAR_DECL DECLARATION
    # DECLARATION -> STATEMENT DECLARATION
    # DECLARATION -> Ɛ
    def declaration(self, statements):

        if self.preanalisis['tipo'] == TipoToken.FUN:
            fundcl = self.fun_decl()
            statements.append(fundcl)
            self.declaration(statements)
            #return fundcl

        elif self.preanalisis['tipo'] == TipoToken.VAR:
            vardcl = self.var_decl()
            statements.append(vardcl)
            self.declaration(statements)
            #return vardcl

        elif self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN or self.preanalisis['tipo'] == TipoToken.FOR or self.preanalisis['tipo'] == TipoToken.IF or self.preanalisis['tipo'] == TipoToken.PRINT or self.preanalisis['tipo'] == TipoToken.RETURN or self.preanalisis['tipo'] == TipoToken.WHILE or self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            stmt = self.statement()
            statements.append(stmt)
            self.declaration(statements)
            print(f'masarriba {stmt}')
            #return stmt
        return statements

    # FUN_DECL -> fun FUNCTION
    def fun_decl(self):
        if self.preanalisis['tipo'] == TipoToken.FUN:
            self.coincidir(TipoToken.FUN)
            fun = self.function()
            return fun
        else:
            self.hayErrores = True
            print('Error. Se esperaba la palabra reservada fun')

    # VAR_DECL -> var id VAR_INIT;
    def var_decl(self):
        if self.preanalisis['tipo'] == TipoToken.VAR:
            self.coincidir(TipoToken.VAR)
            self.coincidir(TipoToken.IDENTIFIER) #Checar
            name = self.previous()
            initializer = self.var_init()
            print(name)
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            stmtv = StmtVar(name['lexema'], str(initializer))
            print(stmtv)
            return stmtv
        else:
            self.hayErrores = True
            print("Error. Se esparaba la palabra reservada var")

    # VAR_INIT -> = EXPRESSION
    # VAR_INIT -> Ɛ
    def var_init(self):
        if self.preanalisis['tipo'] == TipoToken.EQUAL:
            self.coincidir(TipoToken.EQUAL)
            initializer = self.expression()
            return initializer

    #Sentencias
    # STATEMENT -> EXPR_STMT
    # STATEMENT -> FOR_STMT
    # STATEMENT -> IF_STMT
    # STATEMENT -> PRINT_STMT
    # STATEMENT -> RETURN_STMT
    # STATEMENT -> WHILE_STMT
    # STATEMENT -> BLOCK
    def statement(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            return self.expr_stmt()
        elif self.preanalisis['tipo'] == TipoToken.FOR:
            return self.for_stmt()
        elif self.preanalisis['tipo'] == TipoToken.IF:
            return self.if_stmt()
        elif self.preanalisis['tipo'] == TipoToken.PRINT:
            return self.print_stmt()
        elif self.preanalisis['tipo'] == TipoToken.RETURN:
            value = self.return_stmt()
            print(f'Soy return {value}')
            return value
        elif self.preanalisis['tipo'] == TipoToken.WHILE:
            return self.while_stmt()
        elif self.preanalisis['tipo'] == TipoToken.LEFT_BRACE:
            return self.block()
        else:
            self.hayErrores = True
            print('Error.')

    #EXPR_STMT -> EXPRESSION;
    def expr_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expression = self.expression()
            self.coincidir(TipoToken.SEMICOLON)
            return StmtExpression(expression)
        else:
            self.hayErrores = True
            print("Error, se esperaba un expresion de estado")

    #FOR_STMT -> for(FOR_STMT_1 FOR_STMT_2 FOR_STMT_3)STATEMENT
    def for_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.FOR:
            self.coincidir(TipoToken.FOR)
            self.coincidir(TipoToken.LEFT_PAREN)
            initializer = self.for_stmt_1()
            condition = self.for_stmt_2()
            increment = self.for_stmt_3()
            self.coincidir(TipoToken.RIGHT_PAREN)
            body = self.statement()
            if increment is not None:
                body = StmtBlock([body, StmtExpression(increment)])
            if condition is None:
                condition = ExprLiteral(True)
            body = StmtLoop(condition, body)
            if initializer is not None:
                body = StmtBlock([initializer, body])
            return body
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada for")

    #FOR_STMT_1 -> VAR_DECL
    #FOR_STMT_1 -> EXPR_STMT
    #FOR_STMT_1 -> ;
    def for_stmt_1(self):
        if self.preanalisis['tipo'] == TipoToken.VAR:
            return self.var_decl()
        elif self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            return self.expr_stmt()
        elif self.preanalisis['tipo'] == TipoToken.SEMICOLON:
            self.coincidir(TipoToken.SEMICOLON)
            return None
        else:
            self.hayErrores = True
            print("Error, se esparaba la palabra reservada var, declaracion de estado o punto y coma")
            return None

    #FOR_STMT_2 -> EXPRESSION;
    # FOR_STMT_2 -> ;
    def for_stmt_2(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            expr = self.expression()
            self.coincidir(TipoToken.SEMICOLON)
            return expr
        elif self.preanalisis['tipo'] == TipoToken.SEMICOLON:
            self.coincidir(TipoToken.SEMICOLON)
            return None
        else:
            self.hayErrores = True
            print("Error, se esperaba una declaracion de estado o un punto y coma.")
            return None
    #FOR_STMT_3 -> EXPRESSION
    #FOR_STMT_3 -> Ɛ
    def for_stmt_3(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            return self.expression()
        return None

#IF_STMT -> if (EXPRESSION) STATEMENT ELSE_STATEMENT
    def if_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.IF:
            self.coincidir(TipoToken.IF)
            self.coincidir(TipoToken.LEFT_PAREN)
            condition = self.expression()
            print(f'Llegaste {condition}')
            self.coincidir(TipoToken.RIGHT_PAREN)
            thenBranch = self.statement()
            elseBranch = self.else_stmt()
            stmtif = StmtIf(condition, thenBranch, elseBranch)
            print(stmtif)
            return stmtif
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada if.")

    #ELSE_STATEMENT -> else STATEMENT
    #ELSE_STATEMENT -> Ɛ
    def else_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.ELSE:
            self.coincidir(TipoToken.ELSE)
            elseBranch = self.statement()
            return elseBranch
        #return

    #PRINT_STMT -> print EXPRESSION ;
    def print_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.PRINT:
            self.coincidir(TipoToken.PRINT)
            expression = self.expression()
            self.coincidir(TipoToken.SEMICOLON)
            pc = self.previous()
            stmtp = StmtPrint(str(expression))
            print(stmtp)
            return stmtp
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada print.")

    #RETURN_STMT -> return RETURN_EXP_OPC ;
    def return_stmt(self):
        if self.preanalisis['tipo'] == TipoToken.RETURN:
            self.coincidir(TipoToken.RETURN)
            value = self.return_exp_opc()
            print(f'return_stmt {value}')
            self.coincidir(TipoToken.SEMICOLON)
            return StmtReturn(value)
        else:
            self.hayErrores = True
            print("Error, se esperaba la palabra reservada return.")

    #RETURN_EXP_OPC -> EXPRESSION
    #RETURN_EXP_OPC -> Ɛ
    def return_exp_opc(self):
        if self.preanalisis['tipo'] == TipoToken.BANG or self.preanalisis['tipo'] == TipoToken.MINUS or self.preanalisis['tipo'] == TipoToken.TRUE or self.preanalisis['tipo'] == TipoToken.FALSE or self.preanalisis['tipo'] == TipoToken.NULL or self.preanalisis['tipo']==TipoToken.NUMBER or self.preanalisis['tipo']==TipoToken.STRING or self.preanalisis['tipo']==TipoToken.IDENTIFIER or self.preanalisis['tipo'] == TipoToken.LEFT_PAREN:
            value = self.expression()
            return value
