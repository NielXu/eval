"""
This is the CLI entry for ast
"""
import textwrap
import os
from ast import ast, expr, lat


def main():
    "Entrance of the script"
    import argparse
    parser = argparse.ArgumentParser(prog="ast",
        description="Generate and view Abstract-Syntax-Tree",
        epilog=textwrap.dedent('''additional information:
                Please notice that quotations are required since some
                of the symbols are special characters in command line.
                And brackets are also necessary in most of the cases
                since minus sign is a special character as well.'''))
    parser.add_argument("eval",
        help="Evaluate the given expression and display the result if possible",
        metavar="expr",
        nargs="?")
    parser.add_argument("-v", "--view",
        help="View the abstract-syntax-tree that generated by the given expression",
        required=False,
        action="store_true")
    parser.add_argument("-p", "--pdf",
        help="Generate and open the PDF of the math expression",
        required=False,
        action="store_true")
    args = parser.parse_args()
    if args.eval is not None:
        exp = args.eval
        a = ast.build(exp)
        if expr.is_evaluable(exp):
            print(ast.evaluate(a))
        else:
            print("Expression not evaluable: "+exp)
        if args.view:
            ast.view(a)
        if args.pdf:
            temp_path = os.path.dirname(os.path.realpath(__file__))
            lat.quickgen(a, temp_path, "temp", op=True)


if __name__ == "__main__":
    main()