class Game:

    # Initialize internal variables, method automatically called on g = Game()
    def __init__(self):
        self._exit = False

        # Array of known commands, used in run, basically maps commands
            # to function and it says: if will get 'go' execute self._go
        self._commands = {
            'go': self._go,
            'quit': self._quit
        }

        # Array of go sub commands, used by _go
        self._commands_go = {
            'north': self._go_north
            # ...
        }

    # Mathod for parsing command, if it gets "comamnd" returns ("command",None)
    # if "command arg1 arg2" returns ("command", "arg1 arg2")
    @staticmethod
    def parse_command(string):
        string = str(string)
        index = string.find(' ')
        if index < 0:
            return (string, None)

        return (string[:index], string[index+1:])

    # This is main method; the only one which should be called from outside
    # It will just read data from input in never ending loop and parse commands
    def run(self):
        while not self._exit:
            src = input('> ')
            (command,args) = Game.parse_command( src)

            # Do we have this command, execute it
            if command in self._commands:
                self._commands[command](args)
            else:
                print( 'I\'m sorry I don\'t known command {}, try one of these:'.format(command))
                print( '\n'.join( self._commands.keys()))

    #######################################################
    # All game commands go here
    #######################################################
    def _quit(self,args):
        self._exit = True
        print( 'Bye bye')

    # Movement handling, will get executed when user types 'go ...' nad '...' will be in arg
    def _go(self,args):
        # No argument
        if args is None:
            print( 'Go excepts one of these:', '; '.join( self._commands_go.keys()))
            return False

        # Split sub command anr arguments
        (command,args) = Game.parse_command(args)
        if command not in self._commands_go:
            print( 'Go excepts one of these:', '; '.join( self._commands_go.keys()))
            return False

        if args is not None:
            print( 'Too many arguments for go')
            return False

        self._commands_go[command](args)
        return True

    # Go north
    def _go_north(self, args):
        print( 'Going north')


game = Game()
game.run()