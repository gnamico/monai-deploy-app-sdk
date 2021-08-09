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

import os
from abc import ABC
from typing import Dict, Tuple

from monai.deploy.core.datastores.factory import DatastoreFactory
from monai.deploy.core.executors.factory import ExecutorFactory
from monai.deploy.core.graphs.factory import GraphFactory


class RuntimeEnv(ABC):
    """Class responsible to managing run time settings.

    The expected environment variables are the keys in the defaults dictionary,
    and they can be set to override the defaults.
    """

    ENV_DEFAULT = {
        "input": ("MONAI_INPUTPATH", "input"),
        "output": ("MONAI_OUTPUTPATH", "output"),
        "model": ("MONAI_MODELPATH", "models"),
        "graph": ("MONAI_GRAPH", GraphFactory.DEFAULT),
        "datastore": ("MONAI_DATASTORE", DatastoreFactory.DEFAULT),
        "executor": ("MONAI_EXECUTOR", ExecutorFactory.DEFAULT),
    }

    input: str = ""
    output: str = ""
    model: str = ""

    def __init__(self, defaults: Dict[str, Tuple[str]] = None):
        if defaults is None:
            defaults = self.ENV_DEFAULT
        for key, (env, default) in defaults.items():
            self.__dict__[key] = os.environ.get(env, default)
