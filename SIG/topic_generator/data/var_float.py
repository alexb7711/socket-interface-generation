"""!@file var_float.py"""

from SIG.topic_generator.data.variables import Variable, VariableTypes


class VarFloat(Variable):
    """!
    Defines the allowed parameters for an float.

    @param name String defining the name of the float
    @param value float value of the variable
    @param description Description of the variable
    """

    ##==================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize the Variable object
        Variable.__init__(self, data, float, 0.0)

        return
