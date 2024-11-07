"""!@file var_bool.py"""

from SIG.topic_generator.data.data_types.variables import Variable, VariableTypes


##======================================================================================================================
#
class VarBool(Variable):
    """!
    Defines the allowed parameters for an boolean.

    @param name String defining the name of the boolean
    @param value boolean value of the variable
    @param description Description of the variable
    """

    ##=================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize the Variable object
        Variable.__init__(self, data, bool, VariableTypes.bool, True)

        # Attempt to populate object
        # self.populate(data, VariableTypes.bool, True)

        return
