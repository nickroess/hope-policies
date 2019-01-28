import pytest
import functools
import itertools
import operator
import subprocess
import os.path
import time
import glob
import shutil
import multiprocessing

def test_install_kernel(policy, debug):

    if not policy:
        pytest.fail("No policy specified");
    
    # TODO: don't hardcode path?
    install_path = os.path.join("kernels", policy)
    if not os.path.isdir(install_path):
        os.makedirs(install_path)
    
    # do not remake kernel unneccesarily
    if os.path.isfile(os.path.join(install_path, "librv32-renode-validator.so")):
        pytest.skip("Using previously compiled kernel")
    
    makePolicy(policy, "kernels", debug)

    if not os.path.isfile(os.path.join(install_path, "librv32-renode-validator.so")):
        pytest.fail("Failed to generate validator shared object. Install path: {}".format(install_path))


def makePolicy(policy, install_path, debug):
    install_kernel_cmd = "isp_kernel"
    install_kernel_args = [policy, install_path]
    if debug is True:
        install_kernel_args += ["-d"]

    subprocess.call([install_kernel_cmd] + install_kernel_args)
