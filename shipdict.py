#!/usr/bin/env python


class ShipDict(dict):
    """
    extension of dictionary that allow to store (and sort, etc.) Ship objects. They're indexed by id
    """

    def __init__(self):
        super(self)

    def clean_unnamed(self):
        """
        remove ships without name
        """
        pass

    def add_chunk(self,chunk):
        """
        add ship position in the dictionary and create a new entry if there is no ship
        """
        try :
            if is_abbreviated(chunk):
                add_abbreviated(chunk)
            else :
                add_extended(chunk)
        except InvalidImputFormatError:
            print "some data aren't using the correct format, they won't be used"

    def sort(self):
        """
        sort by name and id if they have the same name
        """
        pass

    def sort_ships_by_name(self,ships):
        pass

    def all_ships(self):
        """
        return a list with all the ships in the dictionnary 
        """
        pass

    def ships_by_name(self,name):
        """
        return a list with the coordinate of the ship gived in parameter
        """
        pass

    # private methods
    def add_abbreviated(self,chunk):
        if self[chunk[0]] :
            #creation of a new entry
            self[chunk[0] : Ship(chunk[0])]
        self[chunk[0]].add_position(Position(chunk[1],chunk[2],chunk[6]))

    def add_extended(self,chunk):
        pass

    def is_abbreviated(self,chunk):
        """
        tell if an imput is abbreviated (7 characters) or not (>=11), may raise an exeption if the imput is <11 and !=7 .
        """
        if len(chunk)==7 :
            return true
        elif len(chunk)>10 :
            return false
        else :
            raise InvalidImputFormatError

class Ship(object):
    """
    basic represtation of a ship, that include is id, is name and country and a list of its known positions
    """
    def __init__(self,id,name=None,country=None):
        self.id=id
        self.name=name
        self.country=country
        self.positions=[]
    
    def add_position(self,position):
        positions.append(position)
    
    def sort_positions(self):
        """
        sort the positions by chronological order
        """
        

class Position(object):
    """
    A record that encapsulate position datas
    """
    def __init__(self,latitude, longitude, time):
        self.latitude=latitude
        self.longitude=longitude
        self.time=time
