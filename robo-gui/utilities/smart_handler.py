"""Module to get SMART data from disks"""  # TODO: Request UAC elevation
import re

from pySMART import DeviceList


class Smart:
    """Class to get SMART data from disks"""

    def __init__(self):
        """initializes the Smart class"""
        self.devlist = []
        self.pattern = r"sn:(\S+)"
        self.list = []

    def get_smart_data(self):
        """returns the SMART data"""
        self.devlist = DeviceList()
        print(type(self.devlist))

        return self.devlist


s = Smart()
s.get_smart_data()
