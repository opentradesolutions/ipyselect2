from traitlets import CUnicode, Unicode, Tuple, Bool
from ipywidgets import register, DOMWidget
from ._version import __version__


@register
class Select2(DOMWidget):
    """ The base Select2 widget """
    _view_name = Unicode('Select2View').tag(sync=True)
    _model_name = Unicode('Select2Model').tag(sync=True)
    _view_module = Unicode('ipyselect2').tag(sync=True)
    _model_module = Unicode('ipyselect2').tag(sync=True)
    _view_module_version = Unicode(__version__).tag(sync=True)
    _model_module_version = Unicode(__version__).tag(sync=True)

    value = CUnicode(None).tag(sync=True)
    values = Tuple(trait=Unicode('')).tag(sync=True)
    width = Unicode('').tag(sync=True)
    placeholder = Unicode('').tag(sync=True)
    multiple = Unicode('').tag(sync=True)
    options = Tuple(trait=Unicode('')).tag(sync=True)
    disabled = Bool(False).tag(sync=True)
    lazy = Bool(False).tag(sync=True)
