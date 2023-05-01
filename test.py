# this scripts installs necessary requirements and launches main program in webui.py
import subprocess
import os
import sys
import importlib.util
import shlex
import platform
import json

from modules import cmd_args
from modules.paths_internal import script_path, extensions_dir

commandline_args = os.environ.get('COMMANDLINE_ARGS', "")
print(commandline_args)
sys.argv += shlex.split(commandline_args)
print(sys.argv)
args, _ = cmd_args.parser.parse_known_args()
print(args)
print(args.skip_python_version_check)
