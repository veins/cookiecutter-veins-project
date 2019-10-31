# cookiecutter-veins-project #

Cookiecutter project template for quickly setting up a simulation model library using Veins.

## Supported Program Versions ##

- Cookiecutter 1.6.0 (see <https://github.com/cookiecutter/cookiecutter>)
- git 2.23.0 (see <https://git-scm.com/>)

## Running ##

Save the contents of this repository to disk, e.g., in `~/src/cookiecutter-veins-project` (that is, this file resides in `~/src/cookiecutter-veins-project/README.md`).

Open a terminal and switch to a directory that should contain your new project, e.g., `~/src`.

Run cookiecutter, e.g., as `cookiecutter ~/src/cookiecutter-veins-project`.
You will be prompted for a number of configuration variables (each with a default value, which you can accept by pressing the `enter` key).
After finishing, cookiecutter will have created a directory named after your `project_name_as_file_name` directory.

## Example ##

```
% cd ~/src
% cookiecutter ~/src/cookiecutter-veins-project
project_name [Veins Proj]:
project_brief [Sample combination of Veins and a custom project]:
project_name_as_file_name [veins_proj]:
project_name_as_macro_name [VEINS_PROJ]:
Select use_inet:
1 - no
2 - yes
Choose from 1, 2 (1, 2) [1]:
Select use_inet3:
1 - no
2 - yes
Choose from 1, 2 (1, 2) [1]:
Select use_veins_vlc:
1 - no
2 - yes
Choose from 1, 2 (1, 2) [1]:
Select use_plexe_veins:
1 - no
2 - yes
Choose from 1, 2 (1, 2) [1]:
Select use_simulte:
1 - no
2 - yes
Choose from 1, 2 (1, 2) [1]:
Cookiecutter checks starting.
Making sure we can run git
git version 2.23.0
Cookiecutter checks successful.
Cookiecutter successful. Running git commands to set up repository.
[...]
From https://github.com/sommer/veins
 * tag               veins-5.0  -> FETCH_HEAD
Added dir 'veins'
Repository set up successful. Running git commands to clean up.
Cookiecutter successful.

% cd ~/src/veins_proj
% ls *
Makefile  configure

veins:
COPYING             doc                 images              sumo-launchd.py
Makefile            doxy.cfg            print-veins-version
README.txt          examples            src
configure           format-code.sh      subprojects

veins_proj:
COPYING                  doc                      images
Makefile                 doxy.cfg                 print-veins_proj-version
README.md                examples                 src
configure                format-code.sh
```

## More Information ##

See the Veins website <http://veins.car2x.org/> for a tutorial, documentation,
and publications.

## License ##

Veins is composed of many parts. See the version control log for a full list of
contributors and modifications. Each part is protected by its own, individual
copyright(s), but can be redistributed and/or modified under an open source
license. License terms are available at the top of each file. Parts that do not
explicitly include license text shall be assumed to be governed by the "GNU
General Public License" as published by the Free Software Foundation -- either
version 2 of the License, or (at your option) any later version
(SPDX-License-Identifier: GPL-2.0-or-later). Parts that are not source code and
do not include license text shall be assumed to allow the Creative Commons
"Attribution-ShareAlike 4.0 International License" as an additional option
(SPDX-License-Identifier: GPL-2.0-or-later OR CC-BY-SA-4.0). Full license texts
are available with the source distribution.

