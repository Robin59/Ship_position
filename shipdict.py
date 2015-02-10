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
    """
    basic represtation of a ship, that include is id, is name and country and a list of its known positions
    """
    def __init__(self,id,name='na',country='na'):
        self.id=id
        self.name)=name
        self.country=country
        self.positions=[]
    
    def add_position(self,position):
        pass
    
    def sort_positions(self):
        """
        sort the positions by chronological order
        """
        pass

class Position(object):
    """
    A record that encapsulate position datas
    """
    def __init__(self,latitude, longitude, time):
        self.latitude=latitude
        self.longitude=longitude
        self.time=time
