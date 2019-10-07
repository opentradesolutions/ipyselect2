ipyselect2
=======

# Usage
```python
from ipyselect2 import Select2
import ipywidgets as widgets

s = Select2(options=['x', 'y'], width='200px')

def test(change):
  with output:
    print(change)

s.observe(test, 'value')
output = widgets.Output()
display(s, output)
```

# Installation
A jupyter widget using [select2](https://select2.org/)


With pip:

```bash
pip install ipyselect2
```

To make it work for Jupyter lab:
```
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install ipyselect2
```

If you have notebook 5.2 or below, you also need to execute:
```bash
jupyter nbextension enable --py --sys-prefix ipyselect2
```

For a development installation (requires npm),
```bash
cd /opt
git clone https://github.com/opentradesolutions/ipyselect2.git
cd ipyselect2
pip install -e .
jupyter nbextension install --py --symlink --sys-prefix ipyselect2
jupyter nbextension enable --py --sys-prefix ipyselect2
jupyter labextension link js
```

For Jupyter lab development, you may want to start Jupyter lab with jupyter lab --watch so it instantly picks up changes.
