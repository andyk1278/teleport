#!/usr/bin/env python3

### python 3 - teleport!                                              2017.11.17
### author: supadood,jwcha

import os
import argparse

def main():
    ### init arg parser
    ### query is mandatory, --verbose --depth is optional
    parser = argparse.ArgumentParser()
    parser.add_argument('query', help='directory to begin recursive sort of most recent files')
    parser.add_argument('--verbose', '-v', help='output more information')
    parser.add_argument('--depth', '-d', help='specify a max depth to recurse')
    parser.add_argument('--number', '-n', help='number of files in list. default is 10.', default=10)
    args = parser.parse_args()

    if args.verbose:
        print("verbose mode activate!")
    if args.depth:
        print("depth specified to: {}".format(args.depth))

    ### debug check: does query hold anything?
    print("QUERY IS: {}".format(args.query))

    if query[0] == '.':
        query = rel_to_abs(query)



def rel_to_abs(query):
    path = os.getcwd()
    if query[0] == '.':
        if query[1] == '.':
            path = path[:path.rfind('/')]
    return path


def take_a_walk(query):
    os.chdir(query)
    d, s, f = [], [], []
    dir_files_dict = {}
    for dirs, subs, files in os.walk(query):
        d.appends(dirs)


if __name__ == '__main__':
    main()
