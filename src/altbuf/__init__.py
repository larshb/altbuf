#!/usr/bin/env python3

import sys

__ESC = "\033"
__CSI = __ESC + "["

def __altbuf(on):
  return __CSI + "?1049" + ('h' if on else 'l')

def enable():
  sys.stdout.write(__altbuf(True))


def disable():
  sys.stdout.write(__altbuf(False))
