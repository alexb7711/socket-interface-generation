"""!@file topic_generator.py

This module calls the appropriate generators to create the topic file with
the correct language.
"""

from SIG.topic_generator.generators.gen_c import GenerateC
from SIG.topic_generator.generators.gen_python import GeneratePython
from SIG.topic_generator.generators.gen_rust import GenerateRust
from SIG.topic_generator.topic import Topic


# ==============================================================================
#
def generate(fp: list[str], topic: list[Topic]):
    """!
    Call the correct generation module to create each of the provided topic
    YAML files in their respective locations.

    @param fp List of file paths to each of the topic YAML files
    @param topic List of dictionaries containing the topic data

    @return
    None
    """

    # For each language in the topic
    for f,t in zip(fp, topic):
        if t.lang == "python":
            pygen(f, t)
        elif t.lang == "rust":
            rsgen(f, t)
        elif t.lang == "c++" or t.lang == "c":
            cgen(f, t)

    return
