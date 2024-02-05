#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    def __eq__(self, value):
        """Override == opeartor with !="""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with =="""
        return self.real == value
