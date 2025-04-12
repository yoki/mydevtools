
# MyDevTools

A collection of developer tools to improve your Python development workflow.

## Features

### Filtered Traceback

It automatically removes error traceback frames from site-packages just by importing.
```
from mydevtools import filter_lib_traceback
```
This can be safely commented out without affecting comments. 

### surpress waring
Surpress all kind of warnings from Pandas and others
```
from mydevtools import no_warning
```
This can be safely commented out without affecting comments. 

## Installation

```bash
$ pip install git+https://github.com/yoki/mydevtools.git@v0.1.0
```

## Memo for dev

```
$ git clone git+https://github.com/yoki/mydevtools.git@v0.1.0
$ pip install -e .
$ python examples/sample_usage.py
$ git tag v0.1.1 -m "Bugfix"
$ git push origin v0.1.1
```