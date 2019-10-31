.phony: clean all

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
{%- if cookiecutter.use_simulte == "yes" %}
	$(MAKE) -C simulte clean
{%- endif %}
	$(MAKE) -C {{ cookiecutter.project_name_as_file_name }} clean
