
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

import subprocess

print('Cookiecutter successful. Running git commands to set up repository.')
subprocess.check_call(['git', 'init'])
subprocess.check_call(['git', 'config', 'user.name', 'Christoph Sommer'])
subprocess.check_call(['git', 'config', 'user.email', 'sommer@ccs-labs.org'])
subprocess.check_call(['git', 'commit', '--allow-empty', '--message', 'Initial commit'])

# INET
{%- if cookiecutter.use_inet == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet', '--message', 'Merge INET 4.1.1', 'https://github.com/inet-framework/inet', 'v4.1.1'])
subprocess.check_call(['git', 'rm', 'inet/.gitmodules', 'inet/showcases', 'inet/tutorials'])
subprocess.check_call(['git', 'commit', '--message', 'inet: remove submodules'])
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet/tutorials', '--message', 'Merge INET Tutorials 4.0.0', 'https://github.com/inet-framework/inet-tutorials', 'v4.0.0'])
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet/showcases', '--message', 'Merge INET Showcases 4.0.0', 'https://github.com/inet-framework/inet-showcases', 'v4.0.0'])
{%- endif %}

# INET (version 3)
{%- if cookiecutter.use_inet3 == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet', '--message', 'Merge INET 4.1.1', 'https://github.com/inet-framework/inet', 'v3.6.6'])
subprocess.check_call(['git', 'rm', 'inet/.gitmodules', 'inet/showcases', 'inet/tutorials'])
subprocess.check_call(['git', 'commit', '--message', 'inet: remove submodules'])
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet/tutorials', '--message', 'Merge INET Tutorials 3.6.4', 'https://github.com/inet-framework/inet-tutorials', 'v3.6.4'])
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet/showcases', '--message', 'Merge INET Showcases 3.6.4', 'https://github.com/inet-framework/inet-showcases', 'v3.6.4'])
{%- endif %}

# Veins VLC
{%- if cookiecutter.use_veins_vlc == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=veins_vlc', '--message', 'Merge Veins VLC 1.0', 'https://github.com/veins/veins_vlc', 'veins-vlc-1.0'])
{%- endif %}

# Plexe Veins
{%- if cookiecutter.use_plexe_veins == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=plexe_veins', '--message', 'Merge Plexe Veins 3.0-alpha1', 'https://github.com/michele-segata/plexe-veins', 'plexe-3.0a1'])
{%- endif %}

# Veins
subprocess.check_call(['git', 'subtree', 'add', '--prefix=veins', '--message', 'Merge Veins 5.0', 'https://github.com/sommer/veins', 'veins-5.0'])

print('Repository set up successful. Running git commands to clean up.')
subprocess.check_call(['git', 'config', '--unset', 'user.name'])
subprocess.check_call(['git', 'config', '--unset', 'user.email'])

print('Cookiecutter successful.')
