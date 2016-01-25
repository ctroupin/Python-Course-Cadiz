#!/usr/bin/python
"""printname(name, surname)
Given 2 arguments 'name' and 'surname' written with both lowercase and uppercase,
returns the name with the first letter in uppercase 
and the surname with all letters in uppercase.

Example:
 printname(eRiC, clapTon)
will return
Eric CLAPTO
"""

import sys

def change_case(name, surname):
  name2 = name.capitalize()
  surname2 = surname.upper()
  return name2, surname2
  
def main():
  args = sys.argv[1:]
  name, surname = change_case(args[0], args[1])
  print name, surname

if __name__ == '__main__':
  main()

