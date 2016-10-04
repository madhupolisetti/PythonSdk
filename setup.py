#!/usr/bin/env python

# Licensed under the VOOC Company, Version 1.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.vooc.com/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from setuptools import setup, find_packages
from distutils.core import setup
import re
import os, sys

PKG = 'smscountrysdk'
sys.path.insert(0, os.path.join(os.path.dirname(__file__), PKG))
from config import __version__, __author__


long_desc = """This SDK is a programatic inteface into the SMSCountry
APIs. It simplifies development and cuts development time by standerizing
calls, response processing, error handling, debugging across the Text Messaging,
Voice Broadcasting, Group Calls, Custom SenderIds and CallerIds APIs. """

setup(
    name=PKG,
    version=__version__,
    description="SMS Country SDK for Python",
    author=__author__,
    author_email="tiendangdht@gmail.com",
    url="https://github.com/vooc/smscountrysdk-python",
    license="COMMON DEVELOPMENT AND DISTRIBUTION LICENSE (CDDL) Version 1.0",
    packages=['smscountrysdk'],
    provides=[PKG],
    install_requires=['requests'],
    test_suite='tests',
    long_description=long_desc,
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ]
)