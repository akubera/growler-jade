#
# growler_jade/jade_renderer.py
#

import logging

from pyjade.ext import mako
from pyjade.ext.mako import preprocessor as mako_preprocessor


class JadeRenderer():
    """
    A render engine using the pyjade package to render jade files into mako
    files, which are then turned into html by the make.template package.
    """

    DEFAULT_FILE_EXTENSIONS = [
        '.jade',
    ]

    def __init__(self):
        """
        Construct the renderer, provided the parent renderer.
        """
        # from mako.template import Template

        self._render = None
        self._engine = mako
        self._preprocessor = mako_preprocessor

        self.log = logging.getLogger(__name__)
        self.log.info("%d Constructed JadeRenderer" % (id(self)))

    def __call__(self, filename, res):
        self.log.info("%d -> %s" % (id(self), filename))
        tmpl = self._render(filename=filename, preprocessor=self._preprocessor)
        html = tmpl.render(**res.locals)
        return html

    @staticmethod
    def register_engine():
        """
        Add this rendering engine to the standard growler renderer
        """

        import growler.middleware.renderer
        growler.middleware.renderer.render_engine_map['jade'] = JadeRenderer
