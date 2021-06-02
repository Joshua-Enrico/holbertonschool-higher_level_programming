#!/usr/bin/python3
"""
student class
"""


class Student:
    """defines student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary desc"""
        return self.__dict__
