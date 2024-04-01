# -*- Coding: Utf-8 -*- 
# -*- Imports -*- 
import sys
import time
import ctypes
import msvcrt
import logging
import colorama
from pystyle import *


colorama.init()

# -*- Variables -*- 
__tool__ = "test"
__version__ = "1.0.1"


# -*- Console logging -*- 

def log(message, **kwrgs):
    """ logger handler. """
    fm = f"{colorama.Fore.LIGHTBLACK_EX}[-( {colorama.Fore.LIGHTWHITE_EX}{time.strftime('%H:%M:%S', time.localtime())}{colorama.Fore.LIGHTBLACK_EX} )-]  {message} "
    if kwrgs:
        fm += f"» {', '.join([f'{key} > [{colorama.Fore.LIGHTBLACK_EX}{value}{colorama.Fore.LIGHTWHITE_EX}]' for key, value in kwrgs.items()])}"
    print(fm)

def title(title, **kwrgs):
    """ set console title. """
    message = f"{title}"
    if kwrgs:
        message += f"     |     {', '.join([f'{key} > [{value}]' for key, value in kwrgs.items()])}"
    ctypes.windll.kernel32.SetConsoleTitleW(f'Turbo {__tool__} >> ({__version__}) << | {message}')



def err(message, **kwrgs):
    """ error """
    log(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.RED}●{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.LIGHTWHITE_EX} {message}", **kwrgs)

def debug(message, **kwrgs):
    """ debug | success """
    log(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.LIGHTGREEN_EX}●{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.LIGHTWHITE_EX} {message}", **kwrgs)

def info(message, **kwrgs):
    """ info """
    log(f"{colorama.Fore.LIGHTBLACK_EX}[{colorama.Fore.LIGHTGREEN_EX}●{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.LIGHTGREEN_EX} {colorama.Fore.LIGHTWHITE_EX}{message}", **kwrgs)

def inpt(message):
    """ input """
    answer = input(f"{colorama.Fore.LIGHTBLACK_EX}[-( {colorama.Fore.LIGHTWHITE_EX}{time.strftime('%H:%M:%S', time.localtime())}{colorama.Fore.LIGHTBLACK_EX} )-]  [{colorama.Fore.BLUE}●{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.LIGHTWHITE_EX} {message} {colorama.Fore.LIGHTBLACK_EX}» ")
    return answer

def int_inpt(message):
    """ integer input """
    while True:
        try:
            answer = int(input(f"{colorama.Fore.LIGHTBLACK_EX}[-( {colorama.Fore.LIGHTWHITE_EX}{time.strftime('%H:%M:%S', time.localtime())}{colorama.Fore.LIGHTBLACK_EX} )-]  [{colorama.Fore.BLUE}●{colorama.Fore.LIGHTBLACK_EX}]{colorama.Fore.LIGHTWHITE_EX} {message} {colorama.Fore.LIGHTBLACK_EX}» "))
            return answer
        except:
            time.sleep(0.3)
            info("Please enter a valid integer")
            time.sleep(0.3)


def ext_input():
    """ exit input """
    try:
        info("Press any key") # u dont need to press enter here. any key is sufficient.
        msvcrt.getch()
    except:
        inpt("Press enter")
def asciiprint():
    """ ascii print """
    ascii = """

┌┬┐┌─┐┬┌─┌─┐┌┐┌  ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
 │ │ │├┴┐├┤ │││  │  ├─┤├┤ │  ├┴┐├┤ ├┬┘
 ┴ └─┘┴ ┴└─┘┘└┘  └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─
                              
    """

    ascii2 = """
(GG/POP)                      (V. 1.0.1)


    """
    print(Colorate.Vertical(Colors.cyan_to_green, (Center.XCenter(ascii)), 1))
    print(Colorate.Vertical(Colors.cyan_to_green, (Center.XCenter(ascii2)), 1))



# -*- Debugger -*- 
# ~ call function -> start debugger() to start debugging


class CustomStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  
            self.setFormatter(formatter)
            msg = self.format(record)
            stream = self.stream
            stream.write(msg + '\n')
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


class StdoutToLogger:
    def __init__(self, logger, level=logging.INFO):
        self.logger = logger
        self.level = level

    def write(self, message):
        if message.rstrip() != "":
            level = "INFO"
            if "DEBUG" in message:
                level = "DEBUG"
            elif "WARNING" in message:
                level = "WARNING"
            elif "ERROR" in message:
                level = "ERROR"
            elif "CRITICAL" in message:
                level = "CRITICAL"
            
            fm = f"{colorama.Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M:%S')}] @ {level} >>{colorama.Fore.LIGHTWHITE_EX} {message}"
            self.logger.log(getattr(logging, level), message.rstrip())
            #sys.__stdout__.write(fm + '\n')  

    def flush(self):
        pass

def start_debugger():
    logging.basicConfig(filename=f'{__tool__}.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('my_logger')
    stream_handler = CustomStreamHandler(sys.stdout)
    logger.addHandler(stream_handler)



# -*- Extras -*-

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit():
    sys.exit()
