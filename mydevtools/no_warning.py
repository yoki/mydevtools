import warnings


def _silence():
    warnings.filterwarnings("ignore")


_silence()  # DO IT ON IMPORT
