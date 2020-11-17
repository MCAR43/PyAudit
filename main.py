#!/usr/bin/python3
import argparse
import sys
from app.parser.device import Device
def parseInputArgs(argv):
    parser = argparse.ArgumentParser(description="Python Cisco CIS Auditor")
    parser.add_argument('config', help='Path to the config file')
    parser.add_argument('benchmark', help='Path to the benchmark JSON you wish to execute')
    args = parser.parse_args()
    return args

def exec(inputArgs):
    config_file = ""
    parsed_args = parseInputArgs(inputArgs)

    if parsed_args.config:
        deviceParser = Device(parsed_args.config, parsed_args.benchmark)
        deviceParser.performAudit()
        deviceParser.output()

def main():
    exec(sys.argv[1:])

if __name__ == "__main__":
    main()

