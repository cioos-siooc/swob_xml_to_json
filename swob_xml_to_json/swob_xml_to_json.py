#!/usr/bin/env python3
import xmltodict

from swob_xml_to_json.flatten_json import flatten_json

"""

Parse XML from swob-ml and flatten

"""


def replace_values(input_dict, from_value, to_value):
    """
    Replaces values at top level of dictionary. Mutates source dictionary. Non-recursive
    """
    for key, val in input_dict.items():
        if val == from_value:
            input_dict[key] = to_value
    return input_dict

def parseFile(xml_file_path):
    with open(xml_file_path, "r") as content_file:
        xml_string = content_file.read()
    return parseText(xml_string)

def parseText(xml_string):
    """
    Converts XML to JSON
    """

    data_dict = xmltodict.parse(xml_string)

    # parse out a flat dictionary of the data/metadata fields
    record = flatten_json(data_dict)

    # remove fill values
    replace_values(record["results"], "MSNG", None)
    replace_values(record["metadata"], "MSNG", None)
    return record
