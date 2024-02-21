# Compspec Actions

<p align="center">
  <img height="300" src="https://raw.githubusercontent.com/compspec/spec/main/img/compspec-circle.png">
</p>

These are shared GitHub actions for plugins and compspec libraries (and other parties of interest!) to use for validating and generating compatibility specifications. We currently include:

 - [validate-schema](validate-schema): Validate a compatibility plugin schema.

## Usage

### Validate Schema

This is how you can use the validate schema action.

```yaml
name: actions test
on:
  pull_request: []

jobs:
  validate-schema:
    name: Validate schema
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
      - name: Validate Schema
        uses: compspec/actions/validate-schema@main
        with:
          schema: ./compspec-ior/schema.json
```

## License

HPCIC DevTools is distributed under the terms of the MIT license.
All new contributions must be made under this license.

See [LICENSE](https://github.com/converged-computing/cloud-select/blob/main/LICENSE),
[COPYRIGHT](https://github.com/converged-computing/cloud-select/blob/main/COPYRIGHT), and
[NOTICE](https://github.com/converged-computing/cloud-select/blob/main/NOTICE) for details.

SPDX-License-Identifier: (MIT)

LLNL-CODE- 842614
