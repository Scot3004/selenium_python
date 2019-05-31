# Selenium with Python

## Install

Please use virtualenv if you don't want to add dependencies to your global python install

```bash
pip install -r requirements.txt
```

### Install webdriver

As dependency was installed webdriverdownloader for use it:

By default it will install the drivers on `$HOME/bin` you can add this to your `~/.bashrc` in linux or `~/.bash_profile` in mac 
```
export PATH=${PATH}:$HOME"/bin"
```

then install the driver for firefox

```
webdriverdownloader firefox
```

## Run tests
```bash
python -m unittest
```

## Lint Code

```bash
pylint ./**/*.py
```

## Generate graph

```bash
pycallgraph --include "pages.*" --include "TestPythonOrgSearch*" --include "elements.*" --include "selenium*" graphviz -- ./test_python_search.py
```
