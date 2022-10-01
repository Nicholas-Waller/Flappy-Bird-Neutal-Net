#! /bin/bash
cmd="pip install pygame"
$cmd

status=$?

[ $status -eq 0 ] && echo "$cmd was successful" || echo "$cmd failed. Make sure that you have a python distro installed: https://www.python.org/downloads/"
