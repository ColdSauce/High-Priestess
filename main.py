import argparse

class Interpreter():
    def __init__(self, break_on_error=False, 
            continue_on_error=False, keep_extra=False, 
            strict=False, strip_code=False, trace_off=False, 
            trace_on=False, wimp_mode=True):
        self.break_on_error = break_on_error
        self.continue_on_error = continue_on_error
        self.keep_extra = keep_extra
        self.strict = strict
        self.strip_code = strip_code
        self.trace_off = trace_off
        self.trace_on = trace_on
        self.wimp_mode = wimp_mode

    def build_ast(self, file_name):
        return []

    def interpret(self, ast):
        pass
    
class Hell():
    # Creates a new object.
    def twist(self, objtype, objname):
        pass

    # Destroys an object.
    def consume(self, objname):
        pass

    # Destroys all objects.
    def empty(self):
        pass

    # Throws an error to the interpreter. The reference interpreter 
    # will print a simple error message when this function is issued.
    def break_error(self, error_text="There was an error lmao."):
        pass

    # Immediately ends the program. All active objects are destroyed as usual.
    def apocalpyse(self):
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
    interpreter = Interpreter(wimp_mode = args.wimpmode,
            strict = args.strict,
            trace_on = args.traceon,
            trace_off = args.traceoff,
            strip_code = args.stripcode,
            keep_extra = args.keepextra,
            break_on_error = args.breakonerror,
            continue_on_error = args.continueonerror)
    for file_name in args.files:
        ast = interpreter.build_ast(file_name)
        interpreter.interpret(ast)

if __name__ == '__main__':
    ameno()
