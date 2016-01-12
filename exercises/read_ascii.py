#!/usr/bin/python
"""Reads the content of a 2 column ascii file
"""


def main():
  for a, b in zip(depth, temp):
    print str(a) + '____' + str(b)


if __name__ == '__main__':
  main()
