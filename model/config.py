# -*- coding: utf-8 -*-

"""
@Author  :   Xu
 
@Software:   PyCharm
 
@File    :   config.py
 
@Time    :   2020/9/29 10:16 下午
 
@Desc    :
 
"""

import os
import pathlib

basedir = str(pathlib.Path(os.path.abspath(__file__)).parent.parent)

class Config:

    def __init__(self):

        self.maxlen = 512
        self.batch_size = 16
        self.steps_per_epoch = 1000
        self.epochs = 10000

        self.config_path = basedir + '/model/saved_models/config.json'
        self.checkpoint_path = basedir + '/model/saved_models/model.ckpt'
        self.dict_path = basedir + '/model/saved_models/vocab.txt'