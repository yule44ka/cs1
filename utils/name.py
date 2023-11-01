import argparse

def get_name():
    parser = argparse.ArgumentParser(description="Example of argparse")
    parser.add_argument("--name", help="store name", required=True)
    args = parser.parse_args()
    return args.name