# -*- coding: <UTF-8> -*-
from random import *
import renpy.store as store
import renpy.exports as renpy

def make_menu(location):
    locations = edge.get_locations('grim_battlefield')
    menu_list = [(location.name + ' ' + location.owner, location) for location in locations]
    choice = renpy.display_menu(menu_list)
    return edge.go_to(choice)
ownerable = ['charity_mission']
unique = ['outpost', 'shifting_mist']
class EdgeEngine(object):
    """
    This is the main script of Edge of Mists core module for Mists of Eternal Rome.
    """

    def __init__(self):
        self.locations = []
        self.house = None
        self.max_loc = 0

    def explore_location(self):
        location = choice(renpy.store.edge_locations.items())
        while self.has_location(location[0]) and location[0] in unique:
            location = choice(renpy.store.edge_locations.items())
        location = EdgeLocation(location[0])
        location.gen_owner()
        self.locations.append(location)
        return location
    
    def has_location(self, location_id):
        for location in self.locations:
            if location.id == location_id:
                return True
        return False
    

    def get_locations(self, location_id):
        list_ = []
        for location in self.locations:
            if location.id == location_id:
                list_.append(location)
        return list_

    def go_to(self, location):
        location.go_to()

    def make_locations_menu(self):
        menu_list = []
        for location in self.locations:
            displayed = location.name
            menu_list.append((displayed, location))
        menu_list.append(('Done', 'done'))
        choice = renpy.display_menu(menu_list)
        if choice == 'done':
            return renpy.call('lbl_edge_manage')
        return self.go_to(choice)

    def remove_location(self, location):
        self.locations.remove(location)

    def is_maximum_scouted(self):
        if len(self.locations) < self.max_loc:
            return False
        return True



class EdgeLocation(object):
    def __init__(self, id_, permanent=False):
        self.id = id_
        self.lbl_to_go = 'lbl_edge_' + self.id
        self.owner = None
        self.job = None
        self.permanent = permanent
    @property
    def name(self):
        return renpy.store.edge_locations[self.id].format(self.show_owner())
    def gen_owner(self):
        self.owner = choice(renpy.store.house_names.keys())

    def show_owner(self):
        try:
            value = renpy.store.house_names[self.owner]
            return value
        except KeyError:
            return

    def go_to(self):
        renpy.call(self.lbl_to_go, self)

    def job_available(self):
        pass

