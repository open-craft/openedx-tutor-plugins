from __future__ import annotations
import os
from importlib import resources

from tutor import hooks as tutor_hooks

from .__about__ import __version__

########################################
# CONFIGURATION
########################################

tutor_hooks.Filters.CONFIG_DEFAULTS.add_item(
    ("SCOUT_KEY", "")
)
tutor_hooks.Filters.CONFIG_DEFAULTS.add_item(
    ("SCOUT_LMS_LOG_KEY", "")
)
tutor_hooks.Filters.CONFIG_DEFAULTS.add_item(
    ("SCOUT_NAME", "")
)

########################################
# INITIALIZATION TASKS
########################################


########################################
# TEMPLATE RENDERING
########################################


########################################
# PATCH LOADING
########################################

# For each file in tutor_media/patches,
# apply a patch based on the file's name and contents.
patches = resources.files("tutor_scout_apm") / "patches"
for path in patches.glob("*"):
    with open(path, encoding="utf-8") as patch_file:
        tutor_hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
