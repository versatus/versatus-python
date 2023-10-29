# Build RustPython first

git clone https://github.com/RustPython/RustPython

cd RustPython

cargo build --target wasm32-wasi --no-default-features --features freeze-stdlib,stdlib --release

ls  target/wasm32-wasi/release/rustpython.wasm

# Run the main.py locally

❯ ./main.py < sample-contract-input.json
{"transactions": [{"recipient": "wallet_id_1", "amount": 33}, {"recipient": "wallet_id_2", "amount": 33}, {"recipient": "wallet_id_3", "amount": 33}]}

# Run the python code in wasmer using rustpython.wasm interpreter

❯ wasmer run --dir . ~/RustPython/target/wasm32-wasi/release/rustpython.wasm main.py < sample-contract-input.json
{"transactions": [{"recipient": "wallet_id_1", "amount": 33}, {"recipient": "wallet_id_2", "amount": 33}, {"recipient": "wallet_id_3", "amount": 33}]}

