# -*- coding: utf-8 -*-

import lya

from pathlib import PurePath, Path

BASE_DIR = PurePath(__file__).parent.parent.parent.parent

config = lya.AttrDict.from_yaml(str(BASE_DIR / Path('configs/config.yml')))
