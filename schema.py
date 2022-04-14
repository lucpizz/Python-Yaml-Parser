import yaml


SCHEMA = {

    "name": {
        "required": True,
        "type": "string"
    },
    "description": {
        "required": True,
        "type": "string"
    },
    "version": {
        "required": True,
        "type": "string"
    },
    "author": {
        "required": True,
        "type": "string"
    },
    "license": {
        "required": True,
        "type": "string"
    },
    "posts": [
        {
            "title": "",
            "date": "",
            "content": ""
        }
    ]
}


class SchemaFile:

    def __init__(self, output_file, value=SCEMA):
        self.value = set_value
        self.output_file = output_file

    def set_values(self, input_values):

        with open(self.output_file, "w") as file_name:
            file_name.write(yaml.dumps(input_values))
