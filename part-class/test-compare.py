from functools import total_ordering
import re


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.squre_foot = self.length*self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.squre_foot for r in self.rooms)

    def append_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{} area is {}, style is {}'.format(self.name, self.living_space_footage, self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


if __name__ == "__main__":
    # a = Room('bed_room', 20, 30)
    #     # b = Room('living_room', 30, 40)
    #     # c = Room('kitchen_room', 10, 20)
    #     # h = House('home', 'Asia')
    #     # h1 = House('new-home', 'Europe')
    #     # h.append_room(a)
    #     # h.append_room(b)
    #     # h1.append_room(c)
    #     # if h1 > h:
    #     #     print('{} area > {}'.format(h1.living_space_footage, h.living_space_footage))
    #     # else:
    #     #     print('{} area is {} and < {} area is {}'.format(h1.name, h1.living_space_footage, h.name, h.living_space_footage))
    #     #
    #     # data = [1, 3, 3, 2, 5, 7, 5, 4, 5]
    #     # a = list({k:'' for k in data})
    #     # print(a)
    s = re.compile(r'[0-9]+')
    if s.match('1'):
        print('yes')
    data = [1,2,3,5,7,8]
    new = [23, 45, 1]
    new.reverse()

    print(new)
    print(data+new)
    print(round(7/3, 2))