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

    def to_json(self, attrs=None):
        """returns dictionary desc"""
        rep_dic = self.__dict__
        new_dic = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return rep_dic

                if attr in rep_dic:
                    new_dic[attr] = rep_dic[attr]
            return new_dic

        return rep_dic
