import json
import sys
from typing import List

class ApplicationInputs:
    def __init__(self):
        self.contract_fn = ""
        self.amount = 0
        self.recipients = []

class ProtocolInputs:
    def __init__(self):
        self.version = 0
        self.block_height = 0
        self.block_time = 0

class AccountInfo:
    def __init__(self):
        self.account_address = ""
        self.account_balance = 0

versionStr = "version"
accountInfoStr = "accountInfo"
accountAddressStr = "accountAddress"
accountBalanceStr = "accountBalance"
protocolInputStr = "protocolInput"
blockHeightStr = "blockHeight"
blockTimeStr = "blockTime"
applicationInputStr = "applicationInput"
contractFnStr = "contractFn"
amountStr = "amount"
recipientsStr = "recipients"

class ComputeInputs:
    def __init__(self):
        self.version = 0
        self.account_info = AccountInfo()
        self.protocol_input = ProtocolInputs()
        self.application_input = ApplicationInputs()

    @staticmethod
    def gather():
        json_data = sys.stdin.read()
        json_obj = json.loads(json_data)

        # print(json_obj)

        inputs = ComputeInputs()

        inputs.version = json_obj[versionStr]
        inputs.account_info.account_address = json_obj[accountInfoStr][accountAddressStr]
        inputs.account_info.account_balance = json_obj[accountInfoStr][accountBalanceStr]
        inputs.protocol_input.version = json_obj[protocolInputStr][versionStr]
        inputs.protocol_input.block_height = json_obj[protocolInputStr][blockHeightStr]
        inputs.protocol_input.block_time = json_obj[protocolInputStr][blockTimeStr]
        inputs.application_input.contract_fn = json_obj[applicationInputStr][contractFnStr]
        inputs.application_input.amount = json_obj[applicationInputStr][amountStr]
        inputs.application_input.recipients = json_obj[applicationInputStr][recipientsStr]

        # print("inputs.application_input.amount:", inputs.application_input.amount)

        return inputs

class ComputeTransaction:
    def __init__(self):
        self.recipient = ""
        self.amount = 0

    def to_json(self):
        return {"recipient": self.recipient, "amount": self.amount}

    def from_json(self, j):
        self.recipient = j["recipient"]
        self.amount = j["amount"]

class ComputeOutputs:
    def __init__(self):
        self.transactions = []

    def to_json(self):
        return {"transactions": [transaction.to_json() for transaction in self.transactions]}

    def commit(self):
        print(json.dumps(self.to_json()))
