import os
from .constants import *

class Automation:

    def create_result_dir(self):
        cmd = "mkdir %s" %(OUT_PUT)
        os.system(cmd)

    def run_test(self):
        cmd = 'sh %s -r -a -j -f%s %s'% (RUNNER, OUT_PUT, PROJECT)
        os.system(cmd)

    def clean_results(self):
        cmd = 'rm -rf %s'% (OUT_PUT)
        os.system(cmd)
    

