from pathlib import Path

import pytest
import lya

from server.settings.components import BASE_DIR


@pytest.fixture
def test_settings():
    return lya.AttrDict.from_yaml(str(BASE_DIR / Path('config.yml')))