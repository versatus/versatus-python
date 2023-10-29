import json
import sys

# Read JSON data from stdin
json_data = sys.stdin.read()

try:
    # Attempt to parse the JSON data
    parsed_data = json.loads(json_data)

    # Print the raw JSON data
    print("Raw JSON Data:")
    print(json_data)

    # Print the parsed JSON data
    print("\nParsed JSON Data:")
    print(json.dumps(parsed_data, indent=4))

    # Access specific fields in the JSON data
    print("Account Info:")
    print(f"Account Address: {parsed_data['accountInfo']['accountAddress']}")
    print(f"Account Balance: {parsed_data['accountInfo']['accountBalance']}")

    print("\nProtocol Input:")
    print(f"Version: {parsed_data['protocolInput']['version']}")
    print(f"Block Height: {parsed_data['protocolInput']['blockHeight']}")
    print(f"Block Time: {parsed_data['protocolInput']['blockTime']}")

    print("\nApplication Input:")
    print(f"Contract Function: {parsed_data['applicationInput']['contractFn']}")
    print(f"Amount: {parsed_data['applicationInput']['amount']}")
    print("Recipients:")
    for recipient in parsed_data['applicationInput']['recipients']:
        print(f" - {recipient}")

except json.JSONDecodeError as e:
    print("\nJSON Decode Error:", e)
except Exception as e:
    print("An error occurred:", e)
