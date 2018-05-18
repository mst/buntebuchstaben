from ansiescapes import *
import readchar
from sys import stdout as out
from colored import fg
from random import randint
import re

navi = re.compile("\\x1b\[[ABCD]")

def output(char): out.write(fg(randint(17,255)) + char)

def left(char):
    output(char)
    out.write(cursorBackward(2))
def up(char):
    output(char)
    out.write(cursorUp())
    out.write(cursorBackward(1))
def down(char):
    output(char)
    out.write(cursorMove(0,1))
    out.write(cursorBackward(1))
right = output

mode = right

out.write(clearScreen)

last_char = ''

try:
    while True:
        char = readchar.readkey()
        #out.write(cursorSavePosition + cursorTo(0,0) + repr(char) +
        #          cursorRestorePosition)

        if (char=='\r'):
            pass
        if char == last_char and navi.match(char):
            out.write(char)
        elif char=='\x1b[D':
            mode=left
        elif char=='\x1b[C':
            mode=right
        elif char=='\x1b[B':
            mode=down
        elif char=='\x1b[A':
            mode=up
        elif (char=='\x03'):
            break
        elif (char=='\x7f'):
            out.write(cursorBackward(1) + ' ' + cursorBackward(1))
        else:
            mode(char)
        last_char=char
#        sys.stdout.write(ansiescapes.cursorRight(1))
except KeyboardInterrupt:
    pass


