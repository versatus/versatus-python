#!/usr/bin/env python

import sys
import json

from versatus_python import versatus_python 

JSON_INDENTATION_LEVEL = 4 

def main():
    inputs = versatus_python.ComputeInputs.gather()

    print(json.dumps(inputs.to_json(), indent=JSON_INDENTATION_LEVEL))

    # Convert value to integer
    value = int(inputs.application_input.contract_input.function_inputs.transfer.value, 16)


    # Create output object containing proposed transactions
    output = versatus_python.ComputeOutputs()

    # Write the smart contract results/transactions to stdout
    # output.commit()

if __name__ == "__main__":
    main()
