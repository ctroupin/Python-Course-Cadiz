#!/usr/bin/python


def read_profile(datafile):
  depth = []
  temperature = []
  f = open(datafile, 'r')
  
  for lines in f:
    depth.append(lines.split(' ')[0])
    temperature.append(lines.split(' ')[1])
  f.close()

  return depth, temperature

def main():
  datafile = "../notebooks/data/depth_temperature1.dat"
  depth, temperature = read_profile(datafile)
  print depth
  print temperature

if __name__ == '__main__':
  main()


