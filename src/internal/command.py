from internal.optional_argument import OptionalArgument
from internal.required_argument import RequiredArgument

# Repesents a CLI command or subcommand to the code generator internally
class Command(object):
    def __init__(self, name=None, options=frozenset(), arguments=tuple()):
        self.name = name
        self.options = options
        self.arguments = arguments

    # Function to build the Command object given a dictionary containing the parameters
    # Raises KeyError if the 'name' key isn't present
    # Returns None if it receives an error parsing an OptionalArgument
    @classmethod
    def build(cls, command_dict):
        if not command_dict or 'name' not in command_dict:
            raise KeyError("Command must contain a 'name' key")

        try:
            index = 0
            options=frozenset({OptionalArgument.build(x) for index, x in enumerate(command_dict.get('options', []))})
        except KeyError as e:
            print("Error parsing optional argument number {} for command \"{}\": {}".format(index + 1, command_dict['name'], str(e)))
            return None

        try:
            index = 0
            arguments=tuple({RequiredArgument.build(x) for index, x in enumerate(command_dict.get('arguments', []))})
        except KeyError as e:
            print("Error parsing required argument number {} for command \"{}\": {}".format(index + 1, command_dict['name'], str(e)))

        return Command(
            name=command_dict['name'],
            options=options,
            arguments=arguments)

    # Returns a list of the decorators required for this Command object
    def get_decorators(self):
        decorators = ["@click.command()"]
        for arg in self.arguments:
            decorators.append(arg.get_decorator())
        for option in self.options:
            decorators.append(option.get_decorator())
        return decorators

    # Returns the function prototype for this Command object
    def get_prototype(self):
        input_args = []
        for arg in self.arguments:
            input_args.append(arg.argument.name.replace('-', '_'))
        for option in self.options:
            input_args.append(option.name.replace('-', '_'))
        return 'main({})'.format(', '.join(input_args))

    # Write the Command object to a file referenced by File object f
    def write(self, f):
        f.write(
            '\n'.join(self.get_decorators()) + '\n' +
            'def {}:'.format(self.get_prototype()) + '\n' +
            '\tpass\n\n' +
            'if __name__ == \'__main__\':\n' +
            '\tmain()\n'
        )
