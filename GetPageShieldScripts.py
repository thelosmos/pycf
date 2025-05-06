import os
import argparse
import secrets_file
import logging
import json
from cloudflare import Cloudflare

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",  # Define log format
    filename="GetPageShieldScripts.py.log",  # Log file location
    filemode="a"  # Overwrite file on each run
)

parser = argparse.ArgumentParser(prog="GetPageShieldScripts.py")
parser.add_argument("-z", "--zone", required=True, help="Cloudflare Zone ID")

args = parser.parse_args()

client = Cloudflare(
    api_token=(secrets_file.API_TOKEN_READ),  # This is the default and can be omitted
)
page = client.page_shield.scripts.list(
    zone_id=args.zone
)

print(page.result)
