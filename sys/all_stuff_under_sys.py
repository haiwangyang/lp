import sys

""" print out all stuff under sys object """

for i in [ i for i in dir(sys) if not "_" in i ]:
    print("# " + i + " #")
    print(sys.__dict__[i])
    print("\n")

