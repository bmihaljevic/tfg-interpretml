# Copyright (c) 2023 The InterpretML Contributors
# Distributed under the MIT software license

import sys

from interpret_extension.ext.extension import GREYBOX_EXTENSION_KEY, _is_valid_greybox_explainer
from interpret_extension.ext.extension_utils import load_class_extensions

load_class_extensions(
    sys.modules[__name__], GREYBOX_EXTENSION_KEY, _is_valid_greybox_explainer
)
