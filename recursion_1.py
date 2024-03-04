#!/usr/bin/python3
from timeit import timeit


def TowersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
    """
    Move Disks on hanoi towers from source 
    to destination using Recursion.
    """
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks - 1, startPeg, 6 - startPeg - endPeg)
        print("Move disk {} from Peg {} to Peg {}".format(
            numberOfDisks, startPeg, endPeg))
        TowersOfHanoi(numberOfDisks - 1, 6 - startPeg - endPeg, endPeg)


"""
def TowersOfHanoi(numberOfDisks, startPeg=1, extraPeg=2, endPeg=3):
    if numberOfDisks:
        TowersOfHanoi(numberOfDisks - 1, startPeg, endPeg, extraPeg)
        print("Move disk {} from Peg {} to Peg {}".format(
            numberOfDisks, startPeg, endPeg))
        TowersOfHanoi(numberOfDisks - 1, extraPeg, startPeg, endPeg)
"""

TowersOfHanoi(numberOfDisks=3)
# timeit("TowersOfHanoi", TowersOfHanoi(numberOfDisks=5))
# mySetup = """
# def TowersOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
#     if numberOfDisks:
#         TowersOfHanoi(numberOfDisks - 1, startPeg, 6 - startPeg - endPeg)
#         print("Move disk {} from Peg {} to Peg {}".format(
#             numberOfDisks, startPeg, endPeg))
#         TowersOfHanoi(numberOfDisks - 1, 6 - startPeg - endPeg, endPeg)
# """
# myCode = """TowersOfHanoi(numberOfDisks=5)"""


# print(timeit(setup=mySetup, stmt=myCode, number=1))
