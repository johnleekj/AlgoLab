# -*- coding: utf-8 -*-
"""
Algo lab proj 1
"""

def main():
    filename = input("Please input file location\n")
    filename = filename[1:len(filename)-2]
    print(filename)
    genome_file = open(filename)
    genome_string = genome_file.read()
    genome_string = genome_string[genome_string.find('\n'):]
    print(genome_string)
    
    
if __name__ == '__main__':
    main()