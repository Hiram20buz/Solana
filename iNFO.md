### Install the Solana Tool Suite
https://docs.solana.com/es/cli/install-solana-cli-tools

### Send and Receive Tokens
https://docs.solana.com/es/cli/transfer-tokens

### How to use your Phantom wallet with CLI [Solana Tutorial] - Jun 2nd '22
https://www.youtube.com/watch?v=9up-j1dmiGs

### How to export a private key from Phantom to a Keypair file
https://edulanasca.hashnode.dev/how-to-export-a-private-key-from-phantom-to-a-keypair-file

### How do I export a wallet to a json file from a wallet provider like phantom or solflare to use in the Solana CLI?
https://solana.stackexchange.com/questions/1018/how-do-i-export-a-wallet-to-a-json-file-from-a-wallet-provider-like-phantom-or-s

### pip install base58
https://pypi.org/project/base58/

## How get a .json file from your Secret key
```
import base58
a = [i for i in base58.b58decode('secret key')]
print(a)
```
You save the result in a .json file, for example...
```
>>> import base58
>>> [i for i in base58.b58decode('<PRIVATE_KEY_BASE58>')]
[1, 2, 3, ...]
```
key.json contains ...
```
[1, 2, 3, ...]
```
Once you have installed Solana CLI and run the following command to verify successful installation ...
```
solana --version
```
You can run the next command to check what is the public key from the private key ...
```
solana address -k key.json
```
This must return your public key

