import argparser
import bruteforcer
import sys



def main():

    #define arguments usage, get arguments form console, and parse according definition

    args = {'-t':'timeout', '-w':'wordlist', '-u':'http://url:port/'}
    args_from_console  = sys.argv   

    #create argparser object with argument definition
    parser = argparser.ArgParser(args)

    #parse arguments form console based on definition in previous line
    parsed_args = parser.parse_arguments(args_from_console)
    print(parsed_args)

    #create Bruteforcer object
    bf = bruteforcer.Bruteforcer(parsed_args['-u'], parsed_args['-w'], parsed_args['-t'])
    bf.run_bruteforcer()


if __name__ == '__main__':
    main()