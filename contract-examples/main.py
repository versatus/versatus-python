#!/usr/bin/env python

import sys
import os
import inspect

from versatus_python import versatus_python 

def main():
    inputs = versatus_python.ComputeInputs.gather()

    # Do contract stuff to generate proposed transactions
    transactions = []
    amount_each = inputs.application_input.amount // len(inputs.application_input.recipients)
    for recipient in inputs.application_input.recipients:
        txn = versatus_python.ComputeTransaction()
        txn.recipient = recipient
        txn.amount = amount_each
        transactions.append(txn)

    # Create output object containing proposed transactions
    output = versatus_python.ComputeOutputs()
    output.transactions = transactions

    # Write the smart contract results/transactions to stdout
    output.commit()

if __name__ == "__main__":
    main()

