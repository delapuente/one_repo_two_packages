import os
import shutil
import importlib

# Validate the target package
VALID_TARGETS = {'pack_a', 'pack_b'}
target_name = os.getenv('TARGET_PACKAGE_NAME')

if target_name not in VALID_TARGETS:
    raise Exception(f'Unknown target package name: "{target_name}". '
                    f'Can be one of {list(VALID_TARGETS)}.')

# Write a memory backup of this setup.py file
backup = open(__file__).readlines()

# Replace with the setup of the target package
shutil.copy(f'{target_name}_setup.py', 'setup.py')

# Delegate on it (from this point, everything should be transparent and
# equivalent to have run the package setup in the first place).
importlib.import_module(f'{target_name}_setup')

# Restore the backup
open(__file__, 'w').writelines(backup)
