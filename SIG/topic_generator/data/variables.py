"""! @file variables.py"""

from typing import Any

from dataclasses import dataclass


##======================================================================================================================
#
@dataclass
class VariableTypes:
    """! @brief Dataclass to standardize the formatting of the variable types."""

    bool: str = "bool"
    dict: str = "dict"
    float: str = "float"
    int: str = "int"
    list: str = "list"
    str: str = "str"


##======================================================================================================================
#
class Variable:
    """! @brief Class to verify the data provided is complete and consistent."""

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    # Static Variables
    types: list[str] = []  #!< Track the types of variables found in the current topic

    ##==================================================================================================================
    #
    def __init__(self, data: dict, t: type, default: Any):
        # Define class variables
        self.name: str
        self.desc: str
        self._value: Any
        self._type: type = t

        # Try to populate the variable data
        try:
            ## Required data
            self.name = data["name"]

            ## Optional Data
            self._value = data.get("value", default)
            self.desc = data.get("desc")

            ## If a default value is provided, ensure the data is the correct type
            if data.get("value") and not isinstance(data.get("value"), self._type):
                raise Exception(f"THE PROVIDED DATA IS NOT OF TYPE: {t}")

        except Exception:
            raise

        # Subscribe the current data type to `Variable`
        vb = Variable.str_from_type(t)

        if vb not in Variable.types:
            Variable.types.append(vb)

        return

    ##==================================================================================================================
    #
    def get_value(self) -> Any:
        """! @brief Return a copy of the variable data."""
        return self._value

    ##==================================================================================================================
    #
    def get_type(self) -> str:
        """! @brief Return a copy of the type of data as a string"""
        return self._type

    ##==================================================================================================================
    #
    def str_from_type(t: type) -> str:
        """!
        @brief Given a topic, return the VariableType string representation.

        @param t Variable type

        @return VariableType string representation if the type is supported, None otherwise
        """
        vb = None

        # Update vb with the `VariableType` representation if it is supported
        if t == bool:
            vb = VariableTypes.bool
        elif t == int:
            vb = VariableTypes.int
        elif t == float:
            vb = VariableTypes.float
        elif t == str:
            vb = VariableTypes.str
        elif t == list:
            vb = VariableTypes.list
        elif t == dict:
            vb = VariableTypes.dict

        return vb

    ##==================================================================================================================
    #
    def type_from_str(t: str) -> type:
        """!
        @brief Given a topic, return the VariableType type representation.

        @param t Variable type as string

        @return VariableType type representation if the type is supported, None otherwise
        """
        vb = None

        # Update vb with the `VariableType` representation if it is supported
        if t == VariableTypes.bool:
            vb = bool
        elif t == VariableTypes.int:
            vb = int
        elif t == VariableTypes.float:
            vb = float
        elif t == VariableTypes.str:
            vb = str
        elif t == VariableTypes.list:
            vb = list
        elif t == VariableTypes.dict:
            vb = dict

        return vb

    ####################################################################################################################
    # PRIVATE
    ####################################################################################################################
