from rply import ParserGenerator
from boxes import (
    AssignmentBox, AssignmentsBox, IntBox, ExpressionBox, ExpressionSBox, MainBox, ActionBox, AppBox
)

pg = ParserGenerator(["OPEN","CLOSE","LOCK","SEND","SEARCH",
                    "UNLOCKPW","APP","EQUALS","WAIT","NUMBER"])


@pg.production("main : assignments expressions")
def main(p):
    return MainBox(p[0],p[1])

@pg.production("assignments : assignments assignment")
def expr_assignments(p):
    return AssignmentsBox(p[0], p[1])
@pg.production("assignments : ")
def expr_empty_assignments(p):
    return AssignmentsBox()
@pg.production("assignment : app EQUALS number")
def assignment_op(p):
    return AssignmentBox(p[0], p[2])

@pg.production("expressions : expressions expression")
def expr_expressions(p):
    return ExpressionSBox(p[0], p[1])

@pg.production("expressions : ")
def expr_empty_expressions(p):
    return ExpressionSBox()

@pg.production("expression : action app")
@pg.production("expression : action number")
def expression_op(p):
    return ExpressionBox(p[0], p[1])



@pg.production("action : SEND")
@pg.production("action : UNLOCKPW")
@pg.production("action : LOCK")
@pg.production("action : WAIT")
@pg.production("action : SEARCH")
@pg.production("action : OPEN")
@pg.production("action : CLOSE")
def action(p):
    return ActionBox(p[0])

@pg.production("app : APP")
def app(p):
    return AppBox(p[0])

@pg.production("number : NUMBER")
def number(p):
    return IntBox(p[0])

parser = pg.build()