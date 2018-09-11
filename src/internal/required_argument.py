from internal.argument import Argument

# Class to represent a required argument to a command line tool
class RequiredArgument(object):
    def __init__(self, argument=None):
        self.argument = argument

    # Function to build a RequiredArgument object based on collections objects
    # Raises KeyError if the argument's name isn't present
    @classmethod
    def build(cls, argument_data):
        argument = Argument.build(argument_data.get('argument', None))

        if not argument.name:
            argument.name = argument_data['name']

        return RequiredArgument(
            argument=argument)
