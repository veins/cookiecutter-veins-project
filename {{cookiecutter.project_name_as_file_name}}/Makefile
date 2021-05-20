
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

.PHONY: all clean

all:
	$(MAKE) -C veins all
{%- if cookiecutter.use_inet == "yes" %}
ifdef MODE
	$(MAKE) -C inet all
else
	$(MAKE) -C inet all MODE=release
	$(MAKE) -C inet all MODE=debug
endif
	$(MAKE) -C veins/subprojects/veins_inet all
{%- endif %}
{%- if cookiecutter.use_inet3 == "yes" %}
ifdef MODE
	$(MAKE) -C inet all
else
	$(MAKE) -C inet all MODE=release
	$(MAKE) -C inet all MODE=debug
endif
	$(MAKE) -C veins/subprojects/veins_inet3 all
{%- endif %}
{%- if cookiecutter.use_veins_vlc == "yes" %}
	$(MAKE) -C veins_vlc all
{%- endif %}
{%- if cookiecutter.use_plexe_veins == "yes" %}
	$(MAKE) -C plexe_veins all
{%- endif %}
{%- if cookiecutter.use_simu5g == "yes" %}
ifdef MODE
	$(MAKE) -C simu5g all
else
	$(MAKE) -C simu5g all MODE=release
	$(MAKE) -C simu5g all MODE=debug
endif
{%- endif %}
{%- if cookiecutter.use_simulte == "yes" %}
ifdef MODE
	$(MAKE) -C simulte all
else
	$(MAKE) -C simulte all MODE=release
	$(MAKE) -C simulte all MODE=debug
endif
{%- endif %}
	$(MAKE) -C {{ cookiecutter.project_name_as_file_name }} all

clean:
	$(MAKE) -C veins clean
{%- if cookiecutter.use_inet == "yes" %}
	$(MAKE) -C veins/subprojects/veins_inet clean
	$(MAKE) -C inet clean
{%- endif %}
{%- if cookiecutter.use_inet3 == "yes" %}
	$(MAKE) -C veins/subprojects/veins_inet3 clean
	$(MAKE) -C inet clean
{%- endif %}
{%- if cookiecutter.use_veins_vlc == "yes" %}
	$(MAKE) -C veins_vlc clean
{%- endif %}
{%- if cookiecutter.use_plexe_veins == "yes" %}
	$(MAKE) -C plexe_veins clean
{%- endif %}
{%- if cookiecutter.use_simu5g == "yes" %}
	$(MAKE) -C simu5g clean
{%- endif %}
{%- if cookiecutter.use_simulte == "yes" %}
	$(MAKE) -C simulte clean
{%- endif %}
	$(MAKE) -C {{ cookiecutter.project_name_as_file_name }} clean
