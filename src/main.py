import click
import yaml

from internal.command import Command

def write_header(f):
    f.write("#!/usr/bin/env python3\n\n")
    f.write("# generated by autocli\n")
    f.write("# https://github.com/ryansmick/autocli\n\n")

def write_imports(f):
    f.write("import click\n\n")

@click.command()
@click.argument('language')
@click.option('--yaml-file', '-y')
def main(language, yaml_file):
    if not yaml_file:
        yaml_file = './cli.yml'

    with open(yaml_file, 'r') as f:
        cli_def = yaml.safe_load(f.read())

    try:
        command = Command.build(cli_def)
    except KeyError as e:
        print("Error in top-level command: {}".format(e))

    with open(command.name + '.py', 'w') as f:
        write_header(f)
        write_imports(f)
        command.write(f)

if __name__ == '__main__':
    main()
