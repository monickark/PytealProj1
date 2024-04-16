
# Run Single File
// compile 
python counter.py
// run and deploy
    ~~~> https://app.dappflow.org/
    ~~~> Change to AlgoTestnet. DevWAllet -> Create Wallet -> Connect the account
    ~~~> Get algos for the account from https://bank.testnet.algorand.network/
    ~~~> ABI Studio -> upload contract.json  -> Cretae App -> Set 0 0 1 0 0 for Application Storage
    ~~~> Upload Approval.teal and clear.teal from artifacts folder under Application logic -> App created
    ~~~> Execute functions and check result



# Manage Venv
=> python -m venv .venv    //  .venv folder created
=> cd .venv/Scripts
=> activate     // .venv shell open
    Add rquirements.txt
=> pip freeze > requirements.txt // copy dependency in requirements 
    start docker
=> algokit localnet start


