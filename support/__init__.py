"""
A package with supportive Python modules that are not part of the PyBayes itself, but faciliate
PyBayes building, installation, testing, stress-testing etc.
"""

import os
import subprocess


def determine_pybayes_version(dir, fallback):
    try: # try to get current version from git
        orig_dir = os.getcwd()
        os.chdir(dir)
        version = str(subprocess.check_output(['git', 'describe', '--dirty'])).lstrip('v').rstrip()
        os.chdir(orig_dir)
    except Exception as e:  # CalledProcessError subclassed Exception directly
        print("Failed to determine version using git:", e)
        version = fallback
    return version
