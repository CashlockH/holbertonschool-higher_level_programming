"""XML module"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """From dictionary to XML tree"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        sub = ET.SubElement(root, key)
        sub.text = value
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """From XML tree to dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()
    old_dict = {}
    for child in root:
        old_dict[child.tag] = child.text
    return old_dict
