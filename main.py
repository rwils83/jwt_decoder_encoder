import jwt
import argparse
import json


def encode_jwt(algorithm, payload, secret):
    assert (payload is not None), "You must provide a valid json file for the payload"
    with open(payload, "r") as f:
        to_json = json.load(f)
    encoded_jwt = jwt.encode(to_json, secret, algorithm)
    return encoded_jwt


def get_header(token):
    header = jwt.get_unverified_header(token)
    return header


def decode_jwt(token, algorithm):
    assert (token is not None), "You must provide a valid token"
    algorithms = []
    algorithms.append(algorithm)
    decoded_jwt = jwt.decode(token, algorithms=algorithms, options={"verify_signature":False})
    return decoded_jwt


def parse_args():
    description = "Encode and Decode jwt tokens, pretty simple"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-d", "--decode", action="store_true", help="Use to decode token. Returns payload section. "
                                                                    "For header information, use -g/--getheader")
    parser.add_argument("-e", "--encode", action="store_true", help="Use to encode a token")
    parser.add_argument("-t", "--token", action="store", help="Enter token to decode")
    parser.add_argument("-s", "--secret", action="store", help="Enter secret for encoding. Enter as string, ex: 'secret'")
    parser.add_argument("-p", "--payload", action="store", help='Enter token payload file. File must be valid json.')
    parser.add_argument("-a", "--algorithm", action="store", help="Enter algorithm to use for encoding. Enter as ex: ['HS256']")
    parser.add_argument("-g", "--getheader", action="store_true", help="Enter token, get algorithm used for encoding")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    if args.decode:
        print(decode_jwt(args.token, args.algorithm))
    if args.encode:
        try:
            print(encode_jwt(args.algorithm, args.payload, args.secret))
        except AssertionError as error:
            print(error)
    if args.getheader:
        print(get_header(args.token))