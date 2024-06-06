#!/usr/bin/python3
"""Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            new = dict()
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new
        return self.__dict__

    def reload_from_json(self, json):
        i = 0
        for key in self.__dict__.keys():
            for jkey in json.keys():
                if key == jkey:
                    self.__dict__[key] = json[jkey]
                    break
