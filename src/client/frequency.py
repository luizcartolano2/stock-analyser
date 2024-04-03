""" Docstring for the frequency enum.

"""
from enum import Enum


class Frequency(Enum):
    """ Enum for frequencies."""
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    ANNUALLY = 'annually'
