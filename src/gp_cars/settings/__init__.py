from .local import *

# use production if there is a file
try:
    from .production import *
except:
    pass