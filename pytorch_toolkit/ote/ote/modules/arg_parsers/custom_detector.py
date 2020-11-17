"""
 Copyright (c) 2020 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import argparse

from ote.api import train_args_parser, test_args_parser, export_args_parser

from .default import DefaultArgParser
from ..registry import ARG_PARSERS


@ARG_PARSERS.register_module()
class CustomDetectorArgParser(DefaultArgParser):
    def __init__(self):
        super(CustomDetectorArgParser, self).__init__()

    def get_train_parser(self, config):
        parser = argparse.ArgumentParser(parents=[train_args_parser(config)], add_help=False)
        parser.add_argument('--classes', required=True,
                            help='Comma-separated list of classes (e.g. "cat,dog,mouse").')

        return parser

    def get_test_parser(self, config):
        parser = argparse.ArgumentParser(parents=[test_args_parser(config)], add_help=False)
        parser.add_argument('--classes', required=True,
                            help='Comma-separated list of classes (e.g. "cat,dog,mouse").')

        return parser
