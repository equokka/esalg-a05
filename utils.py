#!/usr/bin/env python

import yaml # pip install pyyaml
from random import randint

def yes_no(q) -> bool:
  while True:
    ans = input("{:.<44}(y/n) ".format(q)).lower()
    if len(ans) != 1: continue
    if   ans == "y": return True
    elif ans == "n": return False
  # else ask again

def is_int(str: str) -> bool:
  try: int(str)
  except ValueError: return False
  return True

def get_option(q: str, num: int, tab: int = 2) -> int:
  error_str = "%sNúmeros 1-%d, por favor." % (tab * " ", num)
  while True:
    i = input(q).strip()

    if is_int(i):
      i = int(i)
      if i in range(1, num + 1):
        return i

    print(error_str)
