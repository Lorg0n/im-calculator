import ast
import operator as op
import sys
import ctypes

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}


def calc(expr):
    expr = expr.replace("^", "**")
    try:
        return eval_(ast.parse(expr, mode='eval').body)
    except:
        return None


def eval_(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)


def fix_icon_for_taskbar(app_model_id: str):
    if (sys_platform := sys.platform) == "win32":
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_model_id)
    else:
        raise NotImplementedError(
            f"the 'fix_icon_for_taskbar' function does not currently work for the os: {sys_platform}")