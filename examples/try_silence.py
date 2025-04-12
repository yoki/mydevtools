# %%
# Before silencing: this will scream like NumPy stubbed its toe.
import numpy as np
import warnings

warnings.warn("this should be shown", DeprecationWarning)

# Now we import the dark magic
from mydevtools import no_warning  # silence.py auto-runs its silencer on import

warnings.warn("this should NOT be shown", DeprecationWarning)


# %%
from mydevtools import filter_lib_traceback
import pandas as pd

pd.DataFrame("str")
# %%
