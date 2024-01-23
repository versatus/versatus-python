from .ierc20 import IERC20

class ERC20(IERC20):
    def __init__(self, name, symbol, decimals, initial_supply, msg_sender):
        self._name = name
        self._symbol = symbol
        self._decimals = decimals
        self._totalSupply = initial_supply
        self._balances = {msg_sender: initial_supply}
        self._allowances = {}

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def decimals(self):
        return self._decimals

    @property
    def totalSupply(self):
        return self._totalSupply

    def balanceOf(self, account):
        return self._balances.get(account, 0)

    def transfer(self, from_, to, value):
        sender_balance = self.balanceOf(from_)
        require(sender_balance >= value, "Insufficient balance")

        self._balances[from_] = sender_balance - value
        self._balances[to] = self.balanceOf(to) + value

        return True

    def allowance(self, owner, spender):
        return self._allowances.get((owner, spender), 0)

    def approve(self, owner, spender, value):
        self._allowances[(owner, spender)] = value
        return True

    def transferFrom(self, from_, to, spender, value):
        owner_allowance = self.allowance(from_, spender)
        require(owner_allowance >= value, "Insufficient allowance")

        self._balances[from_] = self.balanceOf(from_) - value
        self._balances[to] = self.balanceOf(to) + value
        self._allowances[(from_, spender)] = owner_allowance - value

        return True


# Helper function for the 'require' statement
def require(condition, message):
    if not condition:
        raise Exception(f"Require failed: {message}")
