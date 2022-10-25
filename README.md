<div align="center">
<h1>Data Structures and Algorithm Documentation</a></h1>
by Hongnan Gao
Oct, 2022
<br>
</div>

This is the documentation for various data structures and algorithms concepts.

## Workflow

### Installation

```bash
~/gaohn                  $ git clone https://github.com/gao-hongnan/gaohn-dsa.git gaohn-dsa
~/gaohn                  $ cd gaohn-dsa
~/gaohn/gaohn-dsa        $ python -m venv <venv_name> && <venv_name>\Scripts\activate 
~/gaohn/gaohn-dsa (venv) $ python -m pip install --upgrade pip setuptools wheel
~/gaohn/gaohn-dsa (venv) $ pip install -r requirements.txt
~/gaohn/gaohn-dsa (venv) $ pip install myst-nb==0.16.0 
```

The reason for manual install of `myst-nb==0.16.0` is because it is not in sync with the current jupyterbook
version, I updated this feature to be able to show line numbers in code cells.

### Building the book

After cloning, you can edit the books source files located in the `content/` directory. 

You run

```bash
~/gaohn (venv) $ jupyter-book build content/
```

to build the book, and

```bash
~/gaohn (venv) $ jupyter-book clean content/
```

to clean the build files.

A fully-rendered HTML version of the book will be built in `content/_build/html/`.