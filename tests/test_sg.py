#!/usr/bin/python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Standard Lib
import SIG.sig as sig
import os
import unittest

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Packages

# ===============================================================================
#


class TestSIG(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def get_files():
        d = sig.SIG("./examples", "./examples/build")
        d.run()
        return d

    # -------------------------------------------------------------------------------
    #
    def test_dir_search(self):
        # Find the files
        d = TestSIG.get_files()
        f = d.get_files()

        # Count the files
        self.assertEqual(len(f), 7)

        # Check file names
        pwd = os.path.abspath("./examples")

        self.assertTrue(pwd + "/topics/topic_position.yml" in f)

        return

    # -------------------------------------------------------------------------------
    #
    def test_first_level_data_structure(self):
        # Find the files
        d = TestSIG.get_files()
        f = d.get_data()

        # Search for the position test topic
        for x in f:
            if x.name == "position_test_topic":
                f = x

        # Topics
        self.assertTrue(f.name == "position_test_topic")
        self.assertEqual(f.lang, ["python"])
        self.assertEqual(f.protocol, "UDP")
        self.assertTrue(isinstance(f.data["int"], list))
        self.assertTrue(isinstance(f.data["float"], list))
        self.assertEqual(f.desc, "This is a test topic")

        return
