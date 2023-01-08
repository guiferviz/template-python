################
#  Base image  #
################

FROM python:3.8


#########################
# Define env variables. #
#########################

ENV WORKDIR /workspace


#####################
# Install programs. #
#####################

# Install any other dependencies here.
# ...
# Install Python wheel.
COPY dist/*.whl /root/wheel/
RUN pip install /root/wheel/*.whl


#########
# Setup #
#########

WORKDIR $WORKDIR

{%- if 'none' in cookiecutter.command_line_interface|lower %}
ENTRYPOINT ["python"]
{%- endif %}
{%- if 'none' not in cookiecutter.command_line_interface|lower %}
ENTRYPOINT ["{{ cookiecutter.module_name }}"]
# Default command:
CMD ["--help"]
{%- endif %}
