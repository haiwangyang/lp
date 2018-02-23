import os

""" print out all stuff under os object """

for i in [ i for i in dir(os) if not "_" in i ]:
    print("# " + i + " #")
    print(os.__dict__[i])
    print("\n")
