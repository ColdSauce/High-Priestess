import argparse
import sys
from util import _find_getch

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

    def _tokenize(self, some_string):
        pure_tokenized = some_string.replace(
                "$", " $ ").replace("+", " + ").split()
        return pure_tokenized

    def _read_from_tokens(self, tokens):
        if tokens[0] == "+":
            return { "create hell" : tokens[1] }
        else:
            return { tokens[0] : tokens[2:] }

    def build_ast(self, file_name):
        return []

    def interpret(self, ast):
        pass
    

class Sign():
    def __init__(self):
        self.container = ""

    def scrawl_variable(self, env, varname):
        self.container = self.container + str(env[varname])

    def scrawl_string(self, some_string):
        self.container = self.container + some_string

    def tear(self, count=1):
        self.container = self.container[count:]

    def tear_all(self):
        self.container = ""

    def observe(self, env, varname):
        env[varname] = self.container[0]
        return env

    def steal(self, env, varname):
        env = self.observe(env, varname)
        self.container = self.container[1:]
        return env

    def read_and_delete(self, env):
        env = self.read(env)
        self.container = ""
        return env

    def read(self, env):
        env["VOICELIST"] = [self.container] + env["VOICELIST"]
        return env

class Stalker():
    def __init__(self):
        self.initialized = False
        self.buffer = ""
        self.is_distant = True 

    def stalk(self):
        self.initialized = True

    def get_next_char(self):
        return _find_getch()()

    def control_char(self, env, varname):
        next_char = self.get_next_char()
        env[varname] = next_char
        return env

    def control_int(self, env, varname):
        final_number = ""
        next_char = self.get_next_char()
        while next_char != " " and next_char != "\0" and next_char != "\n":
            final_number += next_char
        env[varname] = int(final_number)
        return env
    
    def action(self, env, varname):
        character = chr(env[varname])

        if self.is_distant:
            self.buffer += character
        else:
            # the ',' makes it so that it doesn't
            # print the \n character at the end
            print(character,)

    def action_numeric(self, env, varname):
        character = str(env[varname])

        if self.is_distant:
            self.buffer += character
        else:
            # the ',' makes it so that it doesn't
            # print the \n character at the end
            print(character,)

    def echo(self, env):
        message = env["VOICELIST"][0]
        env = env["VOICELIST"][1:]
        if self.is_distant:
            self.buffer += message
        else:
            # the ',' makes it so that it doesn't
            # print the \n character at the end
            print(message,)
        return env
    
    def distant(self):
        self.is_distant = True

    def personal(self):
        self.is_distant = False

    def paracusia(self):
        # the ',' makes it so that it doesn't
        # print the \n character at the end
        print(self.buffer,)
        self.buffer = ""

class Manipulator():

    # Creates a new master variable.
    # TODO: ^ This is such a bad comment. fix it
    def manufacture_master(self, varname, disposition, size):
        pass

    # Creates a new servant variable with a given master. The master can   
    # also be nonexistant, in which case the variable is 
    # considered lost and is treated as a master variable 
    # that cannot have servants.
    def manufacture_servant(self, varname, disposition, size):
        pass

    # Forces a variable to kill itself, 
    # freeing it (remember though that it will leave decay).
    def suicide(self, varname):
        pass

    # Kills a variable. The same as the suicide function.
    def kill(self, varname):
        pass

    # Cleans up all decay. This ensures that all 
    # open variable spots are usable.
    def void(self):
        pass

    # Kills all variables of a specified disposition. 
    # Remember, this only affects the variables 
    # directly under the manipulator's control and 
    # leaves decay just like all other functions.
    def genocide(self, disposition):
        pass

    # Kills all variables. Works like genocide.
    def omnicide(self):
        pass

    # Sets a variable to a random value.
    # Uses the Global Chaos Generator.
    def chaos(self, varname):
        pass

    # Sets a variable to a given value.
    # The value may be another variable 
    # from the same manipulator or a number.
    def set(self, varname, value):
        pass
    # Sets a variable to the sum of two values.
    # Once again, values may be either variables or numbers.
    def add(self, varname, val1, val2):
        pass

    # Sets a variable to the difference of two values.
    def subtract(self, varname, val1, val2):
        pass

    # Sets a variable to the product of two values.
    def mutliply(self, varname, val1, val2):
        pass

    # Sets a variable to the quotient of two values.
    def divide(self, varname, val1, val2):
        pass

class YourGlass(Exception):
    pass

class Hell():

    def __init__(self):
        self.variables = { }
        self.variable_types = { }
        
    # Creates a new object.
    def twist(self, objtype, objname):
        self.variable_types[objname] = objtype

    # Destroys an object.
    def consume(self, objname):
        self.variables.pop(objname, None)

    # Destroys all objects.
    def empty(self):
        self.variables = { }
        self.variable_types = { }

    # Throws an error to the interpreter. The reference interpreter 
    # will print a simple error message when this function is issued.
    def break_error(self, error_text="There was an error lmao."):
        raise YourGlass(error_text)

    # Immediately ends the program. All active objects are destroyed as usual.
    def apocalpyse(self):
        sys.exit()

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
