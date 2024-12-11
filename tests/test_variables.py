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


class TestVariables(unittest.TestCase):
    # -------------------------------------------------------------------------------
    #
    def get_files(self):
        s = sig.SIG("./examples", "./examples/build")
        s.run()
        return s

    # -------------------------------------------------------------------------------
    #
    def get_topic(self, topic: str, d: list):
        t = None
        for x in d:
            if x.name == topic:
                t = x
                break

        return t

    # -------------------------------------------------------------------------------
    #
    def test_bool(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the Boolean topic
        t = self.get_topic("test_bool_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["bool"][0].name, "my_false")
        self.assertEqual(t.data["bool"][1].name, "my_true")
        self.assertEqual(t.data["bool"][2].name, "my_bool")

        self.assertEqual(t.data["bool"][0].get_value(), False)
        self.assertEqual(t.data["bool"][1].get_value(), True)
        self.assertEqual(t.data["bool"][2].get_value(), True)

        self.assertEqual(len(t.data["bool"]), 3)

        return

    # -------------------------------------------------------------------------------
    #
    def test_float(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the Float topic
        t = self.get_topic("test_float_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["float"][0].name, "float1")
        self.assertEqual(t.data["float"][1].name, "float2")
        self.assertEqual(t.data["float"][2].name, "float3")

        self.assertEqual(t.data["float"][0].get_value(), 10.0)
        self.assertEqual(t.data["float"][1].get_value(), 5.0)
        self.assertEqual(t.data["float"][2].get_value(), 0.0)

        self.assertEqual(len(t.data["float"]), 3)

        return

    # -------------------------------------------------------------------------------
    #
    def test_int(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the Int topic
        t = self.get_topic("test_int_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["int"][0].name, "int1")
        self.assertEqual(t.data["int"][1].name, "int2")
        self.assertEqual(t.data["int"][2].name, "int3")

        self.assertEqual(t.data["int"][0].get_value(), 1)
        self.assertEqual(t.data["int"][1].get_value(), 2)
        self.assertEqual(t.data["int"][2].get_value(), 0)

        self.assertEqual(len(t.data["int"]), 3)

        return

    # -------------------------------------------------------------------------------
    #
    def test_str(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the String topic
        t = self.get_topic("test_string_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["str"][0].name, "my_string1")
        self.assertEqual(t.data["str"][1].name, "my_string2")
        self.assertEqual(t.data["str"][2].name, "my_string3")

        self.assertEqual(t.data["str"][0].get_value(), "My default string value")
        self.assertEqual(t.data["str"][1].get_value(), "Remove the description")
        self.assertEqual(t.data["str"][2].get_value(), "")

        self.assertEqual(len(t.data["str"]), 3)

        return

    # -------------------------------------------------------------------------------
    #
    def test_list(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the String topic
        t = self.get_topic("test_list_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["list"][0].name, "list")
        self.assertEqual(t.data["list"][1].name, "list1")
        self.assertEqual(t.data["list"][2].name, "list2")

        self.assertEqual(t.data["list"][0].get_type(), list)
        self.assertEqual(t.data["list"][1].get_type(), list)
        self.assertEqual(t.data["list"][2].get_type(), list)

        self.assertEqual(t.data["list"][0].list_type, int)
        self.assertEqual(t.data["list"][1].list_type, float)
        self.assertEqual(t.data["list"][2].list_type, str)

        self.assertEqual(t.data["list"][0].get_value(), [1, 2, 3])
        self.assertEqual(t.data["list"][1].get_value(), [3.0, 2.0, 1.0])
        self.assertEqual(t.data["list"][2].get_value(), [])

        self.assertEqual(t.data["list"][0].desc, "A list of integers")
        self.assertEqual(t.data["list"][1].desc, None)
        self.assertEqual(t.data["list"][2].desc, None)

        self.assertEqual(len(t.data["list"]), 3)

        return

    # -------------------------------------------------------------------------------
    #
    def test_dict(self):
        # Find the files
        s = self.get_files()
        d = s.get_data()

        # Find the String topic
        t = self.get_topic("test_dict_topic", d)

        # Test the data in the topic `t`
        self.assertEqual(t.data["dict"][0].name, "dict")
        self.assertEqual(t.data["dict"][1].name, "dict1")

        self.assertEqual(t.data["dict"][0].get_type(), dict)
        self.assertEqual(t.data["dict"][1].get_type(), dict)

        self.assertEqual(
            t.data["dict"][0].get_value(),
            {"item1": "item1 value", "item2": "item2 value", "item3": "item3 value"},
        )
        self.assertEqual(
            t.data["dict"][1].get_value(),
            {"item1": 1, "item2": 2, "item3": 3},
        )

        self.assertEqual(t.data["dict"][0].desc, "A dictionary")
        self.assertEqual(t.data["dict"][1].desc, None)

        self.assertEqual(len(t.data["dict"]), 2)

        return
