"""!@file var_dict.py"""

from SIG.topic_generator.data.variables import Variable, VariableTypes


##======================================================================================================================
#
class VarDict(Variable):
    """!
    Defines the allowed parameters for an dictean.

    @param name String defining the name of the dictean
    @param value dict value of the variable
    @param description Description of the variable
    """

    ##=================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize the Variable object
        Variable.__init__(self, data, dict, {})
        return
