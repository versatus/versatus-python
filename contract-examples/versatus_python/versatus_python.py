import json
import sys

class ApplicationInputs:
    def __init__(self):
        self.contract_input = ContractInput()

class ProtocolInputs:
    def __init__(self):
        self.version = 0
        self.block_height = 0
        self.block_time = 0

class AccountInfo:
    def __init__(self):
        self.account_address = ""
        self.account_balance = 0

class ContractInput:
    def __init__(self):
        self.contract_fn = ""
        self.function_inputs = ERC20FunctionInputs()

class ERC20FunctionInputs:
    def __init__(self):
        self.transfer = ERC20TransferInputs()

class ERC20TransferInputs:
    def __init__(self):
        self.value = 0
        self.address = ""

versionStr = "version"
accountInfoStr = "accountInfo"
accountAddressStr = "accountAddress"
accountBalanceStr = "accountBalance"
protocolInputStr = "protocolInput"
blockHeightStr = "blockHeight"
blockTimeStr = "blockTime"
contractInputStr = "contractInput"
contractFnStr = "contractFn"
functionInputsStr = "functionInputs"
erc20Str = "erc20"
transferStr = "transfer"
valueStr = "value"
addressStr = "address"

class ComputeInputs:
    def __init__(self):
        self.version = 0
        self.account_info = AccountInfo()
        self.protocol_input = ProtocolInputs()
        self.application_input = ApplicationInputs()

    @staticmethod
    def from_json(json_obj):
        inputs = ComputeInputs()

        inputs.version = json_obj[versionStr]
        inputs.account_info.account_address = json_obj[accountInfoStr][accountAddressStr]
        inputs.account_info.account_balance = json_obj[accountInfoStr][accountBalanceStr]
        inputs.protocol_input.version = json_obj[protocolInputStr][versionStr]
        inputs.protocol_input.block_height = json_obj[protocolInputStr][blockHeightStr]
        inputs.protocol_input.block_time = json_obj[protocolInputStr][blockTimeStr]

        contract_input = json_obj[contractInputStr]
        inputs.application_input.contract_input.contract_fn = contract_input[contractFnStr]
        erc20_function_inputs = contract_input[functionInputsStr][erc20Str][transferStr]
        inputs.application_input.contract_input.function_inputs.transfer.value = erc20_function_inputs[valueStr]
        inputs.application_input.contract_input.function_inputs.transfer.address = erc20_function_inputs[addressStr]

        return inputs

    @staticmethod
    def gather():
        json_data = sys.stdin.read()
        json_obj = json.loads(json_data)

        inputs = ComputeInputs.from_json(json_obj)

        return inputs

    def to_json(self):
        return {
            versionStr: self.version,
            accountInfoStr: {
                accountAddressStr: self.account_info.account_address,
                accountBalanceStr: self.account_info.account_balance
            },
            protocolInputStr: {
                versionStr: self.protocol_input.version,
                blockHeightStr: self.protocol_input.block_height,
                blockTimeStr: self.protocol_input.block_time
            },
            contractInputStr: {
                contractFnStr: self.application_input.contract_input.contract_fn,
                functionInputsStr: {
                    erc20Str: {
                        transferStr: {
                            valueStr: self.application_input.contract_input.function_inputs.transfer.value,
                            addressStr: self.application_input.contract_input.function_inputs.transfer.address
                        }
                    }
                }
            }
        }
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