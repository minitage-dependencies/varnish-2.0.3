#!/usr/bin/env python

# Copyright (C) 2008, Makina Corpus <Makina Corpus freesoftware@makina-corpus.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__docformat__ = 'restructuredtext en'

import os
import getpass
import pwd
import grp
import re
import sys

def conf(o, b):
    if sys.platform.startswith('darwin'):
        libtool_file_name = os.path.join(o["compile-directory"], 'libtool')
        libtool_source = open(libtool_file_name, 'r').read()
        libtool_source = libtool_source.replace('export_dynamic_flag_spec=""', 
                                            'export_dynamic_flag_spec="-flat_namespace"')
        open(libtool_file_name, 'w').write(libtool_source)


# vim:set et sts=4 ts=4 tw=80:
