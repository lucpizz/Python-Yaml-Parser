import yaml
import click
from schema import SchemaFile

@click.group()
def cli()
    pass

@click.option("--filename", default="test.yaml")

    schema = SchemaFile(output_file=filename)
    output_schema = {}
    for key in schema.value.keys():
        value = click.prompt(f"What is the value for {key}")
        out_schema[key] = value


    schema.set_values(output_schema)


if __name__ == '__main__':
    cli()
