#!/usr/bin/env python

##############################################################################
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
##############################################################################

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .caffe2.caffe2 import Caffe2Framework
from .generic.generic import GenericFramework
from .oculus.oculus import OculusFramework
from .pytorch.pytorch import PytorchFramework
from .tflite.tflite import TFLiteFramework
from .glow.glow import GlowFramework

frameworks = {
    'caffe2': Caffe2Framework,
    'generic': GenericFramework,
    'oculus': OculusFramework,
    'pytorch': PytorchFramework,
    'tflite': TFLiteFramework,
    'glow': GlowFramework
}


def getFrameworks():
    global frameworks
    return frameworks
