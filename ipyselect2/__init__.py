from ._version import version_info, __version__
from .select2 import *


def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'ipyselect2',
        'require': 'ipyselect2/extension'
    }]
