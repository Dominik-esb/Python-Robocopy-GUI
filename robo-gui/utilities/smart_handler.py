"""Module to get SMART data from disks"""
from pySMART import DeviceList


class Smart:
    """Class to get SMART data from disks"""

    def __init__(self):
        """initializes the Smart class"""
        self.devlist = DeviceList()

    def get_smart_data(self):
        """returns the SMART data"""
        return self.devlist
