ipyselect2
=======

A jupyter Widget using ![select2](https://select2.org/)

Installation
```bash
cd /opt
git clone https://github.com/opentradesolutions/ipyselect2.git
cd ipyselect2
pip install -e .
jupyter nbextension install --py --symlink --sys-prefix ipyselect2
jupyter nbextension enable --py --sys-prefix ipyselect2
jupyter labextension install js
```
