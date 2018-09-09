# Class to represent an argument on the command line
# Can be user for both required arguments as well as values for optional arguments
class Argument(object):
    def __init__(self, name=None):
        self.name = name

    @classmethod
    def build(cls, argument_dict):
        return Argument(name=argument_dict.get('name', None))
