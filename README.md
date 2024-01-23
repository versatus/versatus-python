# Build RustPython first

git clone https://github.com/RustPython/RustPython

cd RustPython

cargo build --target wasm32-wasi --no-default-features --features freeze-stdlib,stdlib --release

ls  target/wasm32-wasi/release/rustpython.wasm

brew install openssl
export CFLAGS="-I/opt/homebrew/Cellar/openssl@3/3.2.0_1/include"
export LDFLAGS="-L/opt/homebrew/Cellar/openssl@3/3.2.0_1/lib"

# Install pycryptodome and web3
pip3 install pycryptodome web3 
opt/homebrew/Cellar/openssl@3/3.2.0_1/include

# Run the main.py locally

❯ ./main.py < sample-contract-input.json
{"transactions": [{"recipient": "wallet_id_1", "amount": 33}, {"recipient": "wallet_id_2", "amount": 33}, {"recipient": "wallet_id_3", "amount": 33}]}

# Run the python code in wasmer using rustpython.wasm interpreter

❯ wasmer run --dir . ~/RustPython/target/wasm32-wasi/release/rustpython.wasm main.py < sample-contract-input.json
{"transactions": [{"recipient": "wallet_id_1", "amount": 33}, {"recipient": "wallet_id_2", "amount": 33}, {"recipient": "wallet_id_3", "amount": 33}]}
