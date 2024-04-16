#
# pip install py-algorand-sdk
#
from algosdk.v2client import algod

# Replace these values with your node's address
# free service does not require tokens
algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

# Initialize the algod client
algod_client = algod.AlgodClient(algod_token, algod_address)

# Get the node status
try:
    status = algod_client.status()
    print("Node status:", status)
except Exception as e:
    print(f"Failed to get node status: {e}")