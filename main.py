import argparse

class Interpreter():
    def __init__(self, breakOnError=False, 
            continueOnError=False, keepExtra=False, 
            strict=False, stripCode=False, traceOff=False, 
            traceOn=False, wimpMode=True):
        self.breakOnError = breakOnError
        self.continueOnError = continueOnError
        self.keepExtra = keepExtra
        self.strict = strict
        self.stripCode = stripCode
        self.traceOff = traceOff
        self.traceOn = traceOn
        self.wimpMode = wimpMode

    def build_ast(self, file_name):
        return []

    def interpret(self, ast):
        pass
    

def ameno():
    FILES_HELP = "List of files to interpret. They get interpreted sequentially"

    WIMPMODE_HELP = """Turns on wimpmode. 
    This is not part of the official specification and is off by default.
    In wimpmode variables don't accumulate corruption 
    and default error handlers are replaced with meaningful error messages."""

    STRICT_HELP = """Turns off wimpmode.
    This ensures that the interpreter runs compliant to the full standard 
    (except for the TRACE mode)."""

    TRACEON_HELP = """Taking the advice of Emiya Shirou,
    you will see everything that happens inside the interpreter.
    All lines are printed as they are executed,
    and all error handlers are replaced as in wimpmode."""

    TRACEOFF_HELP = "Turns off trace mode."

    STRIPCODE_HELP = """Allows the interpreter to 
    remove comments and empty lines upon loading a source file.
    This is on by default, and will result in better performance.
    The actual source file is not modified. While in wimpmode, 
    this will cause invalid line numbers to be printed with 
    the error messages."""

    KEEPEXTRA_HELP = """Forces the interpreter to keep all extra code,
    such as comments and empty lines. Only useful for debugging."""

    BREAKONERROR_HELP = """Causes the interpreter to stop execution 
    and wait for a keypress after each error message.
    Again, this is off by default and will only affect wimpmode."""

    CONTINUEONERROR_HELP = """Does not stop when error messages are output.
    The default behavior of the interpreter."""

    parser = argparse.ArgumentParser(
            description="Dark programming language arguments.")
    parser.add_argument("files", nargs="+", help=FILES_HELP)
    parser.add_argument("-wimpmode", action="store_true", help=WIMPMODE_HELP)
    parser.add_argument("-strict", action="store_true", help=STRICT_HELP)
    parser.add_argument("-traceon", action="store_true", help=TRACEON_HELP)
    parser.add_argument("-traceoff", action="store_true", help=TRACEOFF_HELP)
    parser.add_argument("-stripcode", action="store_true", help=STRIPCODE_HELP)
    parser.add_argument("-keepextra", action="store_true", help=KEEPEXTRA_HELP)
    parser.add_argument("-breakonerror", 
            action="store_true", help=BREAKONERROR_HELP)
    parser.add_argument("-continueonerror", 
            action="store_true", help=CONTINUEONERROR_HELP)
    args = parser.parse_args()
    interpreter = Interpreter(wimpMode = args.wimpmode,
            strict = args.strict,
            traceOn = args.traceon,
            traceOff = args.traceoff,
            stripCode = args.stripcode,
            keepExtra = args.keepextra,
            breakOnError = args.breakonerror,
            continueOnError = args.continueonerror)
    for file_name in args.files:
        ast = interpreter.build_ast(file_name)
        interpreter.interpret(ast)

if __name__ == '__main__':
    ameno()
