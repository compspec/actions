#!/usr/bin/env python3

import argparse
import sys
import os
import json
import jsonschema

here = os.path.abspath(__file__)
root = os.path.dirname(here)

# Validation for the compspec.json files, a compatibility group schema,
# is done with an existing standard, json graph format
schema_file = os.path.join(here, "json-graph-schema_v2.json")


def read_json(filename):
    with open(filename, "r") as fd:
        content = json.loads(fd.read())
    return content


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compatibility Schema Validator",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("schema", help="path to schema file to validate")
    return parser


def main():
    """
    Validate the format of WIP prototype specs.
    """
    parser = get_parser()

    # If an error occurs while parsing the arguments, the interpreter will exit with value 2
    args, extra = parser.parse_known_args()

    # Show args to the user
    print("     schema: %s" % args.schema)

    to_validate = os.path.abspath(args.schema)
    if not os.path.exists(to_validate):
        sys.exit(f"{to_validate} does not exist.")

    schema = read_json(schema_file)
    spec = read_json(to_validate)

    # Validate
    print(f"⭐️ Validating spec {to_validate}")

    try:
        spec = read_json(to_validate)
    except:
        sys.exit("Invalid: cannot read json file")
    jsonschema.validate(spec, schema=schema)


if __name__ == "__main__":
    main()
