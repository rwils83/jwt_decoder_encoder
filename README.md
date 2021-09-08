# JWT Decoder and Encoder
## What is it?
A simple JWT token encoder, decoder. 
## How to use it?
Encode and Decode jwt tokens, pretty simple

optional arguments:  
  -h, --help            show this help message and exit  
  -d, --decode          Use to decode token. Returns payload section. For header information, use -g/--getheader  
  -e, --encode          Use to encode a token  
  -t TOKEN, --token TOKEN Enter token to decode  
  -s SECRET, --secret SECRET Enter secret for encoding. Enter as string, ex: 'secret'
  -p PAYLOAD, --payload PAYLOAD Enter token payload file. File must be valid json.  
  -a ALGORITHM, --algorithm ALGORITHM Enter algorithm to use for encoding. Enter as ex: ['HS256']  
  -g, --getheader       Enter token, get algorithm used for encoding

## What's to come?
:shrug: If there are any ideas, I welcome them

## How to contribute?

Read CONTRIBUTIONS.md
