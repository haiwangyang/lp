# https://www.learnpython.org/en/Multiple_Function_Arguments

def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))

foo("a", "b", "c", "d", "e", "f")

### output
# First: a
# Second: b
# Third: c
# And all the rest... ['d', 'e', 'f']
