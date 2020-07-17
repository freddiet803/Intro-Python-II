# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player():
    def __init__(self, name, room, health=100):
        self.name = name
        self.health = health
        self.room = room
        self.items = []

    def __str__(self):
        return f'Player name: {self.name}, Health: {self.health}, {self.room}'

    def pickupItem(self, item):
        self.items.append(item)

    def dropItem(self, item):
        self.items.remove(item)
