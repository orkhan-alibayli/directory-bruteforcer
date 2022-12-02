import argparser
import sys


args_from_console  = sys.argv


args = {'-t':'timeout', '-w':'wordlist', '-h':'header'}

parser = argparser.ArgParser(args)

#parser.print_help()
parsed_args = parser.parse_arguments(args_from_console)


print(parsed_args)
