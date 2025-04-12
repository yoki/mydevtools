# mydevtools/filter_lib_traceback.py
import sys
from types import TracebackType

try:
    from IPython.core.getipython import get_ipython
    from IPython.core.ultratb import VerboseTB
except ImportError:
    # IPython not available — silently skip setup
    def _install():
        return
else:

    class FilteredVerboseTB(VerboseTB):
        def get_records(self, etb: TracebackType, context: int, tb_offset: int):
            records = super().get_records(etb, context, tb_offset)
            exclude = ("site-packages",)
            filtered = []
            for r in records:
                filename = getattr(r, "filename", None)
                if isinstance(filename, str) and any(excl in filename for excl in exclude):
                    continue
                filtered.append(r)
            if len(filtered) < len(records):
                print("[mydevtools] Traceback from site-packages are filtered out.")
            return filtered if filtered else records

    def _install():
        ip = get_ipython()
        if not ip:
            return  # Not in IPython or Jupyter

        try:
            tb = FilteredVerboseTB(call_pdb=False, ostream=sys.stderr)

            def ipython_exc_handler(*args, **kwargs):
                etype, value, tb_obj = args[:3]
                tb((etype, value, tb_obj))

            ip.set_custom_exc((Exception,), ipython_exc_handler)
        except Exception as e:
            # Optional: log or suppress
            print(f"[mydevtools] Could not install filtered traceback: {e}", file=sys.stderr)


# 👇 Automatically run on import
_install()
