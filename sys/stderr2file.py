import sys
# https://www.python-course.eu/sys_module.php

save_stderr = sys.stderr
fh = open("errors.txt","w")
sys.stderr = fh

x = 10 / 0

# return to normal:
sys.stderr = save_stderr

fh.close()
