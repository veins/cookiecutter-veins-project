
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
import os
import subprocess

print('Cookiecutter successful. Running git commands to set up repository.')
subprocess.check_call(['git', 'init'])
subprocess.check_call(['git', 'config', 'user.name', 'Christoph Sommer'])
subprocess.check_call(['git', 'config', 'user.email', 'sommer@ccs-labs.org'])
subprocess.check_call(['git', 'commit', '--allow-empty', '--message', 'Initial commit'])

# INET
{%- if cookiecutter.use_inet == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet', '--message', 'Merge INET 4.2.1', 'https://github.com/inet-framework/inet', 'v4.2.1'])
#subprocess.check_call(['git', 'rm', 'inet/.gitmodules', 'inet/showcases', 'inet/tutorials'])
#subprocess.check_call(['git', 'commit', '--message', 'inet: remove submodules (showcases and tutorials)'])
#subprocess.check_call(['git', 'subtree', 'add', '--squash', '--prefix=inet/tutorials', '--message', 'Merge INET Tutorials 4.0.0', 'https://github.com/inet-framework/inet-tutorials', 'v4.0.0'])
#subprocess.check_call(['git', 'subtree', 'add', '--squash', '--prefix=inet/showcases', '--message', 'Merge INET Showcases 4.0.0', 'https://github.com/inet-framework/inet-showcases', 'v4.0.0'])
{%- endif %}

# INET (version 3)
{%- if cookiecutter.use_inet3 == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=inet', '--message', 'Merge INET 3.6.8', 'https://github.com/inet-framework/inet', 'v3.6.8'])
subprocess.check_call(['git', 'rm', 'inet/.gitmodules', 'inet/showcases', 'inet/tutorials'])
subprocess.check_call(['git', 'commit', '--message', 'inet: remove submodules (showcases and tutorials)'])
#subprocess.check_call(['git', 'subtree', 'add', '--squash', '--prefix=inet/tutorials', '--message', 'Merge INET Tutorials 3.6.4', 'https://github.com/inet-framework/inet-tutorials', 'v3.6.4'])
#subprocess.check_call(['git', 'subtree', 'add', '--squash', '--prefix=inet/showcases', '--message', 'Merge INET Showcases 3.6.4', 'https://github.com/inet-framework/inet-showcases', 'v3.6.4'])
{%- endif %}

# Veins VLC
{%- if cookiecutter.use_veins_vlc == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=veins_vlc', '--message', 'Merge Veins VLC 1.0', 'https://github.com/veins/veins_vlc', 'veins-vlc-1.0'])
{%- endif %}

# Plexe Veins
{%- if cookiecutter.use_plexe_veins == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=plexe_veins', '--message', 'Merge Plexe Veins 3.0-alpha1', 'https://github.com/michele-segata/plexe-veins', 'plexe-3.0a1'])
{%- endif %}

# SimuLTE
{%- if cookiecutter.use_simulte == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=simulte', '--message', 'Merge SimuLTE 1.1.0', 'https://github.com/inet-framework/simulte.git', 'v1.1.0'])
{%- endif %}

# Simu5G
{%- if cookiecutter.use_simu5g == "yes" %}
subprocess.check_call(['git', 'subtree', 'add', '--prefix=simu5g', '--message', 'Merge Simu5G Master', 'https://github.com/Unipisa/Simu5G.git', 'master'])

{%- endif %}

# Veins
subprocess.check_call(['git', 'subtree', 'add', '--prefix=veins', '--message', 'Merge Veins 5.1', 'https://github.com/sommer/veins', 'veins-5.1'])

# Cookiecutter project
subprocess.check_call(['git', 'add', '.'])
subprocess.check_call(['git', 'commit', '--message', '{{ cookiecutter.project_name_as_file_name }}: Add skeleton for {{ cookiecutter.project_name }}'])

print('Repository set up successful. Running git commands to clean up.')
subprocess.check_call(['git', 'config', '--unset', 'user.name'])
subprocess.check_call(['git', 'config', '--unset', 'user.email'])



# Change inet references for Simu5G to 'inet' instead of 'inet4'
{%- if cookiecutter.use_simu5g == "yes" %}

# '.project' file
with open(os.getcwd() + "/simu5g/.project", "r") as file:
    data = file.readlines()
data[5] =" 		<project>inet</project>\n<project>veins</project>\n<project>veins_inet</project>\n"
with open(os.getcwd() + "/simu5g/.project", "w") as file:
    file.writelines(data)

# Makefile
with open(os.getcwd() + "/simu5g/Makefile", "r") as file:
    data = file.readlines()
data[15] ="	@cd src && opp_makemake --make-so -f --deep -o simu5g -O out -KINET_PROJ=../../inet -DINET_IMPORT -I. -I$$\(INET_PROJ\)/src -L$$\(INET_PROJ\)/src -lINET$$\(D\)\n"
with open(os.getcwd() + "/simu5g/Makefile", "w") as file:
    file.writelines(data)

# bin
with open(os.getcwd() + "/simu5g/bin/simu5g", "r") as file:
    data = file.readlines()
data[3] ="INET_SRC=`(cd $SIMU5G_ROOT/../inet/src ; pwd)`\n"
with open(os.getcwd() + "/simu5g/bin/simu5g", "w") as file:
    file.writelines(data)

{%- endif %}


print('Cookiecutter successful.')
