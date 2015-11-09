#
# tests/test_jade.py
#


import pytest

import growler_jade.jade_renderer
from growler_jade.jade_renderer import JadeRenderer


@pytest.fixture
def renderer():
    return JadeRenderer()


def test_renderer(renderer):
    assert isinstance(renderer, growler_jade.jade_renderer.JadeRenderer)
