#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def main():

    target_dir = "프로야구생존기"
    start_idx, end_idx = 0, 190

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for i in range(start_idx, end_idx):
        filename = os.path.join(target_dir, f'{i+1:03d}') + '.md'
        open(filename, 'x')

if __name__ == "__main__":
    main()