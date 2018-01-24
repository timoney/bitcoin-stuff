from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import config
import logging

logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

# rpc_user and rpc_password are set in the bitcoin.conf file
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(config.rpcuser, config.rpcpassword))
block_hash = rpc_connection.getblockhash(1)
print(block_hash)
block = rpc_connection.getblock(block_hash)
print(block)

#// get the first block

#//get raw data

#// convert it to hex

#// convert to ascii

#// print output

#// check if it has any english words