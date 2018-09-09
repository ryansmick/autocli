import click
import yaml

from internal.command import Command

@click.command()
@click.argument('language')
@click.option('--yaml-file', '-y')
def main(language, yaml_file):
    if not yaml_file:
        yaml_file = './cli.yml'

    with open(yaml_file, 'r') as f:
        cli_def = yaml.safe_load(f.read())

    try:
        Command.build(cli_def)
    except KeyError as e:
        print("Error in top-level command: {}".format(e))

if __name__ == '__main__':
    main()
