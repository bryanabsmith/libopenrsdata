#!/usr/bin/env python

"""
    OpenRSData Python 3 Library.
"""

import xml.etree.ElementTree as etree
import urllib.request

__version__ = "0.1"

class LibOpenRSData(object):
    """
        Main OpenRSData module
    """

    @staticmethod
    def get_all_school_data():
        """
            Return all the school data.
        """

        full_list = []

        tree = etree.parse(urllib.request.urlopen(
            "http://www.bryanabsmith.com/openrsdata/get_school_data.php")).getroot()

        for child in tree:
            temp_list = {}
            temp_list["id"] = child.attrib["id"]
            temp_list["name"] = child.attrib["name"]
            temp_list["location"] = child.attrib["location"]
            temp_list["juris"] = child.attrib["juris"]
            temp_list["years"] = child.attrib["years"]
            temp_list["lat"] = child.attrib["lat"]
            temp_list["lng"] = child.attrib["lng"]
            temp_list["yropen"] = child.attrib["yropen"]
            temp_list["yrclosed"] = child.attrib["yrclosed"]
            temp_list["notes"] = child.attrib["notes"]
            temp_list["source"] = child.attrib["source"]
            full_list.append(temp_list)

        return full_list

    @staticmethod
    def get_number_of_schools():
        """
            Get the number of schools.
        """
        tree = etree.parse(urllib.request.urlopen(
            "http://www.bryanabsmith.com/openrsdata/get_school_data.php")).getroot()
        return len(tree)

    @staticmethod
    def get_valid_juris():
        """
            Return the valid jursdictions.
        """
        return ("BC", "AB", "SK", "MB", "ON", "QC", "NS", "YK", "NT", "NU")

    @staticmethod
    def get_number_of_schools_by_juris(prov_code):
        """
            Return the number of schools by valid jursdictions.
        """
        if prov_code in ("BC", "AB", "SK", "MB", "ON", "QC", "NS", "YK", "NT", "NU"):
            list_of_schools = 0
            tree = etree.parse(urllib.request.urlopen(
                "http://www.bryanabsmith.com/openrsdata/get_school_data.php")).getroot()
            for child in tree:
                if child.attrib["juris"] == prov_code:
                    list_of_schools += 1
            return list_of_schools
        else:
            return "libopenrsdata: Invalid prov_code provided"

    @staticmethod
    def get_version():
        """
            Return the version of the library.
        """
        return __version__
