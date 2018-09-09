from internal.optional_argument import OptionalArgument

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
        if not command_dict or not 'name' in command_dict:
            raise KeyError("Command must contain a 'name' key")

        try:
            index = 0
            options=frozenset({OptionalArgument.build(x) for index, x in enumerate(command_dict.get('options', []))})
        except KeyError as e:
            print("Error parsing optional argument number {} for command \"{}\": {}".format(index + 1, command_dict['name'], str(e)))
            return None

        return Command(
            name=command_dict['name'],
            options=options)