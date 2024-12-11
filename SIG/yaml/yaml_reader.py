# Modules
import yaml

from typing import TextIO


# ==============================================================================
#
def open_yaml(fp: str, access: str) -> TextIO:
    """!
    The open YAML function is meant to be a wrapper around the PyYAML package
    when parsing YAML files.

    @param fp Path to YAML file
    @param access Character that specifies access rights to the file

    @return
    - fh: File handle to the YAML file
    """
    try:
        with open(fp, access) as fh:
            yml = yaml.load(fh, Loader=yaml.Loader)
            return yml
    except yaml.YAMLError as exc:
        print("ERROR - Unable to open YAML file: ", exc)

    return None
