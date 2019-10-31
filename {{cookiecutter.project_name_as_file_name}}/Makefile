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
	$(MAKE) -C {{ cookiecutter.project_name_as_file_name }} all

clean:
	$(MAKE) -C veins clean
{%- if cookiecutter.use_inet == "yes" %}
	$(MAKE) -C veins/subprojects/veins_inet clean
	$(MAKE) -C inet clean
{%- endif %}
	$(MAKE) -C {{ cookiecutter.project_name_as_file_name }} clean
