"""!
@file sig.py
@package SIG
@brief This file defines the core for the Socket Interface Generator (SIG)

The SIG object requires:

- 'base_d': Base path of project to recursively search (Default: pwd)
- 'out_d': Output path for the documentation (Default: pwd)

At this point, the program shall execute, recursively searching directories for
appropriately named YAML files. The appropriate boilerplate code shall generate
with the specified language at the location that the file was located.

The allowed languages are: Python, Rust, C/C++.

After all of the files have been generated, a documentation file of the API
generated will be created and placed in the `out_d/[language]` directory where `[language]`
is a subdirectory used to separate interfaces for each language.
"""

# =====================================================================================================================
# Imports
import os
import re

import SIG.yaml.yaml_reader as yaml_reader
import SIG.topic_generator.topic as topic

from SIG.topic_generator.topic_generator import generate
from SIG.utility.exception_handler import print_exception_warning


# =====================================================================================================================
#


class SIG:
    """!@brief Socket Interface Generation Class."""

    ####################################################################################################################
    # PUBLIC
    ####################################################################################################################

    ##==================================================================================================================
    #
    def __init__(self, base_d: str = ".", out_d: str = ".") -> None:
        """! Initializes and creates the interface files given `base_d` and outputs them code to `out_d`

        @param base_d Base path to begin searching (Default: "."):
        @param out_d Output directory for the documentation (Default: ".")

        @return
        - Generates source code for the associated YAML file in the directory
          that the YAML file was found
        - Generates the API documentation
        """

        # fmt: off
        ## @var base_d
        # Absolute path to the directory from which SIG begins searching
        self.base_d = os.path.abspath(base_d)

        ## @var out_d
        # Absolute path to the directory where the API files and documentation will be output
        self.out_d = os.path.abspath(out_d)

        ## @var _files
        # List of files topic YAML files found
        self._files = []

        ## @var _data
        # List of data within the topics
        self._data = []
        # fmt: on

        return

    # --------------------------------------------------------------------------
    #
    def run(self) -> None:
        """! @brief Executes the SIG process."""

        # Search for YAML files
        self._files = self._search_for_yaml()

        # Generate the files
        self._generate_files()

        # Create documentation
        self._generate_doc()

        return

    # --------------------------------------------------------------------------
    #
    def get_files(self) -> list[str]:
        """!
        @brief Returns a list of the stored YAML file location's

        @return List of file paths separated by type.
        Example: list[0] -> [path]
        """
        return self._files.copy()

    # --------------------------------------------------------------------------
    #
    def get_data(self) -> list[str]:
        """!
        Returns a list of the stored variable data in each YAML topic file found

        @return List of dictionaries of variable information contained in each
        YAML topic file
        Example: list[0] -> [dict]
        """
        return self._data.copy()

    ############################################################################
    # PRIVATE
    ############################################################################

    # --------------------------------------------------------------------------
    #
    def _search_for_yaml(self) -> list[str]:
        """!
        The search for YAML function recursively searches `base_d` for
        appropriately named files and returns the found absolute file paths.

        @return Dictionary of YAML file locations
        """
        # Create empty list
        files = []

        # Recursively search `base_d` for `[name].[yml,yaml]`
        for path, _, f_names in os.walk(self.base_d):
            # For all the files in `f_names`
            for f in f_names:
                ## If a YAML file is found
                if re.match(".*yml$", f) or re.match(".*yaml$", f):
                    ### Append the file to the files list
                    files.append(path + "/" + f)

        # Sort the files for consistency in processing
        files.sort()

        return files

    # --------------------------------------------------------------------------
    #
    def _generate_files(self):
        """! @brief Generate the topic files."""
        # Create a buffer of all the topics
        self._data = self._get_message_data()

        # Call publisher generation function
        generate(self._files, self._data)

        return

    # --------------------------------------------------------------------------
    #
    def _get_message_data(self) -> list[dict]:
        """!
        @brief Extract the variable data from the YAML file.

        @return A list of Topic data objects (i.e. list of topics found in the project)
        """
        # Create empty buffer
        message = []
        files_to_remove = []

        # Iterate through each message to be created
        for fp in self._files:
            # Read in the YAML file
            yml = yaml_reader.open_yaml(fp, "r")

            # Save the data
            try:
                message.append(topic.Topic.format_data(yml))
            except Exception as e:
                ## Print exception
                print_exception_warning(e, None, fp)

                ## Add to list of file paths to remove due to improper formatting
                files_to_remove.append(fp)
                pass

        # Remove the improperly formatted files
        for rm in files_to_remove:
            self._files.remove(rm)

        return message

    # --------------------------------------------------------------------------
    #
    def _generate_doc(self):
        """!Generate the documentation"""
        return
