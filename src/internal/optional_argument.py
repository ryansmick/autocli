from internal.argument import Argument

# Class to represent an optional argument to a command line tool
class OptionalArgument(object):
    def __init__(self, name=None, short_name=None, argument=None):
        self.name = name
        self.short_name = short_name
        self.argument = argument

    # Function to build a OptionalArgument object based on collections objects
    # Raises KeyError if the argument's name isn't present
    @classmethod
    def build(cls, argument_data):
        if not argument_data or 'name' not in argument_data:
            raise KeyError("All optional arguments must include the 'name' key")

        argument = Argument.build(argument_data.get('argument', None))

        if not argument.name:
            argument.name = argument_data['name']

        return OptionalArgument(
            name=argument_data['name'],
            short_name=argument_data.get('short-name', None),
            argument=argument)
