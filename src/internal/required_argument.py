from internal.argument import Argument

# Class to represent a required argument to a command line tool
class RequiredArgument(object):
    def __init__(self, argument=None):
        self.argument = argument

    # Function to build a RequiredArgument object based on collections objects
    # Raises KeyError if the argument's name isn't present
    @classmethod
    def build(cls, argument_data):
        if not argument_data or 'name' not in argument_data:
            raise KeyError("All required arguments must include the 'name' key")

        argument = Argument.build(argument_data)

        return RequiredArgument(
            argument=argument)

    # Returns the decorator for this RequiredArgument
    def get_decorator(self):
        return '@click.argument(\'{}\')'.format(self.argument.name)
