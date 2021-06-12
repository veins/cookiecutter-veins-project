
#
# Copyright (C) 2019 Christoph Sommer <sommer@ccs-labs.org>
#
# Documentation for these modules is at http://veins.car2x.org/
#
# SPDX-License-Identifier: GPL-2.0-or-later
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
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import re
import subprocess
import sys

project_name_as_file_name = '{{ cookiecutter.project_name_as_file_name }}'
project_name_as_macro_name = '{{ cookiecutter.project_name_as_macro_name }}'
use_inet = '{{ cookiecutter.use_inet }}'
use_inet3 = '{{ cookiecutter.use_inet3 }}'
use_simulte = '{{ cookiecutter.use_simulte }}'
use_simu5g = '{{ cookiecutter.use_simu5g }}'

print('Cookiecutter checks starting.')

print('Making sure we can run git')
subprocess.check_call(['git', '--version'])

if not re.match(r'^[a-z0-9_]+$', project_name_as_file_name):
    print('ERROR: project_name_as_file_name "%s" does not solely consist of characters a-z, 0-9, and underscore.' % project_name_as_file_name)
    sys.exit(1)

if not re.match(r'^[A-Z0-9_]+$', project_name_as_macro_name):
    print('ERROR: project_name_as_macro_name "%s" does not solely consist of characters A-Z, 0-9, and underscore.' % project_name_as_macro_name)
    sys.exit(1)

if use_inet == "yes" and use_inet3 == "yes":
    print('ERROR: use_inet and use_inet3 cannot both be "yes" (these two versions of the INET framework cannot coexist).')
    sys.exit(1)

if use_simulte == "yes" and use_inet == "no":
    print('ERROR: use_simulte requires use_inet (SimuLTE requires INET version 4).')
    sys.exit(1)

if use_simu5g == "yes" and use_inet == "no":
    print('ERROR: use_simu5g requires use_inet (SIMU5G requires INET version 4).')
    sys.exit(1)

print('Cookiecutter checks successful.')
