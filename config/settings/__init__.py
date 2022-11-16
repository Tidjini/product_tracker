import os
from .base import *

environement = os.environ.get("ENV")

if environement == "development":
    from .local import *
else:
    from .production import *
