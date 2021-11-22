#!/usr/bin/env python3

import argparse


def get_args():
    parser = argparse.ArgumentParser( description='sample' )

    parser.add_argument( 'arg', help='sample', type=str )

    return parser.parse_args()



if __name__ == '__main__':
    args = get_args()
    print( args.arg )

