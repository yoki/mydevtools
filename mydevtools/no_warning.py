import warnings


def _silence():
    warnings.simplefilter("ignore", category=FutureWarning)
    warnings.simplefilter("ignore", category=DeprecationWarning)
    warnings.simplefilter("ignore", category=UserWarning)
    warnings.simplefilter("ignore", category=RuntimeWarning)
    warnings.simplefilter("ignore", category=PendingDeprecationWarning)
    warnings.simplefilter("ignore", category=ImportWarning)
    warnings.simplefilter("ignore", category=ResourceWarning)
    warnings.simplefilter("ignore", category=SyntaxWarning)
    try:
        warnings.simplefilter("ignore", category=EncodingWarning)
    except NameError:
        pass
    warnings.simplefilter("ignore", category=UnicodeWarning)
    warnings.simplefilter("ignore", category=BytesWarning)
    warnings.simplefilter("ignore", category=Warning)

    try:
        import numpy as np

        warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)  # type: ignore
    except (ImportError, AttributeError):
        pass


_silence()  # DO IT ON IMPORT
