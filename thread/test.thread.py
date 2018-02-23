from thread import start_new_thread
# https://www.python-course.eu/threads.php

def heron(a):
    """Calculates the square root of a"""
    eps = 0.0000001
    old = 1
    new = 1
    while True:
        old,new = new, (new + a/new) / 2.0
        print([old, new])
        if abs(new - old) < eps:
            break
    return new

start_new_thread(heron,(99,))
start_new_thread(heron,(999,))
start_new_thread(heron,(1733,))

c = raw_input("Type something to quit.")
