"""
This module is used by the other example modules in this directory. It is not
meant as a stand-alone application.
Copyright (c) 2020 NetApp, Inc. All Rights Reserved.
Licensed under the BSD 3-Clause "New" or "Revised" License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
https://opensource.org/licenses/BSD-3-Clause
"""

import argparse
from collections import namedtuple
from getpass import getpass
import logging
from typing import List

from netapp_ontap import config, HostConnection


# A structure to hold details of an argument
Argument = namedtuple(
    "Argument", ["short_arg", "long_arg", "help_string"]
)

def parse_args(program_description: str, arguments: List[Argument]) -> argparse.Namespace:
    """Parse the command line arguments from the user"""

    parser = argparse.ArgumentParser(description=program_description)
    for argument in arguments:
        parser.add_argument(
            argument.short_arg, argument.long_arg, 
            help=argument.help_string
        )
    parser.add_argument("-u", "--api_user", help="API Username")
    parser.add_argument("-p", "--api_pass", help="API Password")
    parsed_args = parser.parse_args()

    # collect the password without echo if not already provided
    if not parsed_args.api_pass:
        parsed_args.api_pass = getpass()

    return parsed_args


def setup_logging() -> None:
    """Configure logging for the application"""

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )

def setup_connection(cluster: str, api_user: str, api_pass: str) -> None:
    """Configure logging for the application"""

    config.CONNECTION = HostConnection(
        cluster,
        username=api_user,
        password=api_pass,
        verify=False,
    )

def get_size(vol_size: int):
    """ Convert MB to Bytes"""
    tmp = int(vol_size) * 1024 * 1024
    return tmp
