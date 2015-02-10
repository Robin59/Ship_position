#!/usr/bin/env python


class ShipDict(dict):
    """
    extension of dictionary that allow to store (and sort, etc.) Ship objects. They're indexed by id
    """

    def __init__(self):
        pass

    def clean_unnamed(self):
        pass

    def add_chunk(self,chunk):
        pass

    def sort(self):
        pass

    def sort_ships_by_name(self,ships):
        pass

    def all_ships(self):
        pass

    def ships_by_name(self,name):
        pass

    # private methods
    def add_abbreviated(self):
        pass

    def add_extended(self):
        pass

    def is_abbreviated(self,chunk):
        #tell if the chunk is abreviated or not
        pass

class Ship(object):

class Position(object):
