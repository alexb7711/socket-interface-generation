"""!@file var_float.py"""

from SIG.topic_generator.data.variables import Variable, VariableTypes


class VarInt(Variable):
    """!
    Defines the allowed parameters for an integer.

    @param name String defining the name of the integer
    @param value Integer value of the variable
    @param description Description of the variable
    """

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize variable
        Variable.__init__(self, data, int, 0)

        return
