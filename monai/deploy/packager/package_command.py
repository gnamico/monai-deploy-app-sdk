# Copyright 2020 - 2021 MONAI Consortium
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from argparse import ArgumentParser, Namespace, _SubParsersAction


def create_package_parser(subparser: _SubParsersAction, command: str) -> ArgumentParser:
    parser = subparser.add_parser(command)

    parser.add_argument("application", type=str, help="MONAI application path")
    parser.add_argument("--tag", type=str, help="tag name")

    return parser


def execute_package_command(args: Namespace):
    if not args.tag:  # if tag name is empty
        print("Missing tag name. Use --tag=<tag name>", file=sys.stderr)
        sys.exit(1)