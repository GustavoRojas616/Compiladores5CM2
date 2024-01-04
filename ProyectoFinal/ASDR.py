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


class ASDR:
    global tokens
    def __init__(self, tokens):
        self.i = 0
        self.hayErrores = False
        self.tokens = tokens
        self.preanalisis = self.tokens[self.i]

    def parse(self):
        self.program()

        if len(self.preanalisis) == len(tokens) and self.hayErrores==False:
            print("Consulta correcta.")
            return True
        else:
            print("Se encontraron errores.")
            return False

    # PROGRAM -> DECLARATION
    def program(self):
        self.declaration()

    # DECLARATION -> FUN_DECL DECLARATION
    # DECLARATION -> VAR_DECL DECLARATION
    # DECLARATION -> STATEMENT DECLARATION
    # DECLARATION -> Ɛ
    def declaration(self):

        if self.preanalisis == reservadas.get('FUN'):
            self.fun_decl()
            self.declaration()

        elif self.preanalisis == reservadas.get('VAR'):
            self.var_decl()
            self.declaration()

        elif self.preanalisis == simbolos.get('BANG') or self.preanalisis == simbolos.get('MINUS') or self.preanalisis == reservadas.get('TRUE') or self.preanalisis == reservadas.get('FALSE') or self.preanalisis == reservadas.get('NULL') or self.preanalisis.isnumber() == True or self.preanalisis.isalnum() == True or (self.preanalisis not in simbolos_values and self.preanalisis not in reservadas_values) or self.preanalisis == simbolos.get('LEFT_PAREN') or self.preanalisis == reservadas.get('FOR') or self.preanalisis == reservadas.get('IF') or self.preanalisis == reservadas.get('PRINT') or self.preanalisis == reservadas.get('RETURN') or self.preanalisis == reservadas.get('WHILE') or self.preanalisis == simbolos.get('LEFT_BRACE'):
            self.statement()
            self.declaration()

    # FUN_DECL -> fun FUNCTION
    def fun_decl(self):
        if self.preanalisis == reservadas.get('FUN'):
            self.coincidir(reservadas.get('FUN'))
            self.function()
        else:
            self.hayErrores = True
            print('Error. Se esperaba la palabra reservada fun')

    # VAR_DECL -> var id VAR_INIT;
    def var_decl(self):
        if self.preanalisis == reservadas.get('VAR'):
            self.coincidir(reservadas.get('VAR'))
            self.coincidir() #Checar
            self.var_init()
            self.coincidir(simbolos.get('SEMICOLON'))
        else:
            self.hayErrores = True
            print("Error. Se esparaba la palabra reservada var")

    # VAR_INIT -> = EXPRESSION
    # VAR_INIT -> Ɛ
    def var_init(self):
        if self.preanalisis == simbolos.get('EQUAL'):
            self.coincidir(simbolos.get('EQUAL'))
            self.expression()

    # STATEMENT -> EXPR_STMT
    # STATEMENT -> FOR_STMT
    # STATEMENT -> IF_STMT
    # STATEMENT -> PRINT_STMT
    # STATEMENT -> RETURN_STMT
    # STATEMENT -> WHILE_STMT
    # STATEMENT -> BLOCK
    def statement(self):
        if self.preanalisis == simbolos.get('BANG') or self.preanalisis == simbolos.get('MINUS') or self.preanalisis == reservadas.get('TRUE') or self.preanalisis == reservadas.get('FALSE') or self.preanalisis == reservadas.get('NULL') or self.preanalisis.isnumber() == True or self.preanalisis.isalnum() == True or (self.preanalisis not in simbolos_values and self.preanalisis not in reservadas_values) or self.preanalisis == simbolos.get('LEFT_PAREN'):
            self.expr_stmt()
        elif self.preanalisis == reservadas.get('FOR'):
            self.for_stmt()
        elif self.preanalisis == reservadas.get('IF'):
            self.if_stmt()
        elif self.preanalisis == reservadas.get('PRINT'):
            self.print_stmt()
        elif self.preanalisis == reservadas.get('RETURN'):
            self.return_stmt()
        elif self.preanalisis == reservadas.get('WHILE'):
            self.while_stmt()
        elif self.preanalisis == simbolos.get('LEFT_BRACE'):
            self.block()
        else:
            self.hayErrores = True
            print('Error.')
