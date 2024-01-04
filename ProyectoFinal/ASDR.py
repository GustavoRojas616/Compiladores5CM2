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
