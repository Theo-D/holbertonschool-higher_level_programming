#!/usr/bin/python3
"""
task_03_xml.py - Module containing functions serializing and deserializing XML data.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Function for Serializing a python dictionary into XML and writes it to a file.
    """
    tree = ET.Element("data")
    for key in dictionary:
        child = ET.Element(key)
        child.text = str(dictionary[key])
        tree.append(child)

    string = ET.tostring(tree)
    with open(filename, 'wb') as f:
        f.write(string)


def deserialize_from_xml(filename):
    """
    Function for deserializing XML data into a python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}

    for child in root:
        dictionary[child.tag] = child.text
    return dictionary
