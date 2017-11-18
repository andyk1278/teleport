import argparse
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help="directory to begin recursive sort of most recent files")
    parser.add_argument('--verbose', '-v', help="output more verbose information")
    parser.add_argument('--depth', '-d', help='specify depth of recursion')





if __name__ == '__main__':
	main()