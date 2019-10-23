#!/usr/bin/env python3
# 7. Pipelines:
#    a. Create a script that runs a command with subprocess.run.
#    b. Check the exit status
#    c. If exit status is good, run a second command.

import subprocess

# When writing pipelines, sometimes its necessary to know which version of some
# software your pipeline is using and behave accordingly. For instance, samtools
# v0.1.19 has a different command line interface (CLI) than v1.0+ and is not
# compatible with pipelines that rely on v1.0+. So, below is an example where we
# are going to check the version of python we are using


# Is python in your PATH environment variable?
call = subprocess.run(["which","python"], stdout=subprocess.PIPE, check=True)

# If it is, `which` will return exit code 0, otherwise exit code 1
if call.returncode is 0:
    # now, determine the version of python we are using by calling it wit the
    # --version flag. Most well-written software will include such an option
    # and write the version to stderr, so we must read the version from stderr:
    call = subprocess.run(["python","--version",], stderr=subprocess.PIPE, check=True)

    if call.returncode is 0: # if the above command doesn't return an error...
        print("You are using '{}'".format(call.stderr.decode('utf-8').rstrip()))
        
