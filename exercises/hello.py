#!/usr/bin/python

def hello():
  print "Hello world"
  return

def square(x):
  y = x*x
  return y
  
def main():
  hello()
  print square(2.5)

if __name__ == '__main__':
  main()

