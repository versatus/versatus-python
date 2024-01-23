#!/usr/bin/env python

import sys
import json

from versatus_python import versatus_python 
from versatus_python.erc20.erc20 import ERC20
from versatus_python.erc20.ierc20 import IERC20

class MyTokenSmartContract(ERC20):
    def __init__(self, name, symbol, decimals, initial_supply, msg_sender):
        super().__init__(name, symbol, decimals, initial_supply, msg_sender)
        self._msg_sender = msg_sender

    @property
    def msg_sender(self):
        return self._msg_sender

    @msg_sender.setter
    def msg_sender(self, value):
        self._msg_sender = value

    def print_erc20_properties(self):
        # Accessing ERC-20 properties
        print("Name:", self.name)
        print("Symbol:", self.symbol)
        print("Decimals:", self.decimals)
        print("Total Supply:", self.totalSupply)

    def perform_transfers(self, account2, transfer_amount):
        # Transfers between accounts
        account1 = self.msg_sender
        self.transfer(account1, account2, transfer_amount)
        print(f"Balance of {account1}: {self.balanceOf(account1)}")
        print(f"Balance of {account2}: {self.balanceOf(account2)}")

    def approve_and_transfer_from(self, spender, approval_amount):
        # Approve and transferFrom
        account1 = self.msg_sender
        account2 = "0x89abcdef0123456789abcdef0123456789abcdef"
        self.approve(account1, spender, approval_amount)
        self.transferFrom(account1, account2, spender, 30)
        print(f"Allowance for {account1} to {spender}: {self.allowance(account1, spender)}")
        print(f"Balance of {account1}: {self.balanceOf(account1)}")
        print(f"Balance of {account2}: {self.balanceOf(account2)}")

def my_token_smart_contract():

    msg_sender = "0x0123456789abcdef0123456789abcdef01234567"

    # Deploy the MyTokenSmartContract
    my_token = MyTokenSmartContract(name="MyToken", symbol="MTK", decimals=18, initial_supply=1000000000000, msg_sender=msg_sender)

    # Accessing ERC-20 properties
    my_token.print_erc20_properties()

    # Perform transfers
    account2 = "0x89abcdef0123456789abcdef0123456789abcdef"
    transfer_amount = 10000000000
    my_token.perform_transfers(account2, transfer_amount)

    # Approve and transferFrom
    spender = "0x456789abcdef0123456789abcdef0123456789ab"
    approval_amount = 50000
    my_token.approve_and_transfer_from(spender, approval_amount)


def parse_json():
    JSON_INDENTATION_LEVEL = 4

    inputs = versatus_python.ComputeInputs.gather()

    print(json.dumps(inputs.to_json(), indent=JSON_INDENTATION_LEVEL))

    # Convert value to integer
    value = int(inputs.application_input.contract_input.function_inputs.transfer.value, 16)


    # Create output object containing proposed transactions
    output = versatus_python.ComputeOutputs()

    # Write the smart contract results/transactions to stdout
    # output.commit()

def main():

    parse_json()
    my_token_smart_contract()

if __name__ == "__main__":
    main()
