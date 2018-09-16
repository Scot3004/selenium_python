# selenium_python

## Install

Please use virtualenv if you don't want to add dependencies to your global python install

```bash
pip install -r requirements.txt
```

## Generate graph

```bash
pycallgraph --include "pages.*" --include "TestPythonOrgSearch*" --include "elements.*" --include "selenium*" graphviz -- ./test_python_search.py
```
