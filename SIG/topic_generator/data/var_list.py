"""!@file var_list.py"""

from SIG.topic_generator.data.variables import Variable, VariableTypes


##======================================================================================================================
#
class VarList(Variable):
    """!
    Defines the allowed parameters for an listean.

    @param name String defining the name of the listean
    @param value list value of the variable
    @param description Description of the variable
    """

    ##=================================================================================================================
    #
    def __init__(self, data: dict):
        # Initialize the Variable object
        Variable.__init__(self, data, list, [])

        try:
            # Check if the YAML file specifies what the data type of the list is
            if not data.get("type"):
                raise Exception(
                    f"The list {data['name']} does not specify the list variable type"
                )

            # Update the list data type
            self.list_type = Variable.type_from_str(data["type"])
        except:
            raise

        return
