# This the very simple program for parsing command line arguments


class ArgParser:

    def __init__(self, arguments) -> None:
        #arguments and their definitons which provided by programmer
        self.arguments = arguments

        #arguments after parsing
        self.parsed_arguments = {}


    def __print_help(self):
        '''In wrong syntax prints help message and exit'''

        print('EXAMPLE USAGE: python program.py -w wordlist -t timeout')

        for key in self.arguments.keys():
            print(f'{key}    {self.arguments[key]}')
        
        exit()


    def parse_arguments(self, args_from_console):
        '''If syntax is correct parses arguments and returns argument and its value as a dictionary.
        Else calls a function for printing help message.'''

        for arg in list(self.arguments.keys()):

            #catching IndexError exception
            try:
                index_of_arg = args_from_console.index(arg)

                #parses timeout value form string to integer
                if(arg== '-t'):
                    self.parsed_arguments[arg] = int(args_from_console[index_of_arg + 1])
                else:
                    self.parsed_arguments[arg] = args_from_console[index_of_arg + 1]
            except IndexError:
                self.__print_help()
            except ValueError:
                print('Timeout must be an integer')
                self.__print_help()
                
        return self.parsed_arguments

