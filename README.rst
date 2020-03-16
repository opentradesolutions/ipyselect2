ipyselect2
==========

Usage
=====

.. code:: python

    from ipyselect2 import Select2
    import ipywidgets as widgets

    s1 = Select2(options=['a', 'b'], width='200px')
    s2 = Select2(options=['x', 'y'], width='200px', multiple='multiple', lazy=True)
    s2.layout.height = '60px'
    def values_change(change):
      with output:
        print(change)
    s1.observe(values_change, 'value')
    s2.observe(values_change, 'values')
    output = widgets.Output()
    tab = widgets.Tab()
    tab.children = [s1, s2]
    def tab_change(x):
      if x['new']: s2.lazy = False
    tab.observe(tab_change, 'selected_index')
    tab.set_title(0, 'single select')
    tab.set_title(1, 'multiple select')
    display(tab, output)

Installation
============

A jupyter widget using `select2 <https://select2.org/>`__

With pip:

.. code:: bash

    pip install ipyselect2

To make it work for Jupyter lab:

::

    jupyter labextension install @jupyter-widgets/jupyterlab-manager
    jupyter labextension install ipyselect2

If you have notebook 5.2 or below, you also need to execute:

.. code:: bash

    jupyter nbextension enable --py --sys-prefix ipyselect2

For a development installation (requires npm),

.. code:: bash

    cd /opt
    git clone https://github.com/opentradesolutions/ipyselect2.git
    cd ipyselect2
    pip install -e .
    jupyter nbextension install --py --symlink --sys-prefix ipyselect2
    jupyter nbextension enable --py --sys-prefix ipyselect2
    jupyter labextension link js

For Jupyter lab development, you may want to start Jupyter lab with
jupyter lab --watch so it instantly picks up changes.
