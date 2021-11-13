#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def main():
    target_dir = "프로야구생존기"
    dirs = os.listdir(target_dir)
    latest = 190

    for idx, filename in enumerate(dirs):
        prev = "[" + f'{idx:03d}' + "](./" + f'{idx:03d}' + ".md)"
        next = "[" + f'{idx+2:03d}' + "](./" + f'{idx+2:03d}' + ".md)"
        with open(os.path.join(target_dir, filename), 'a') as f:
            if idx == 0:
                f.write("\n\n" + next)
            elif idx == latest-1:
                f.write("\n\n" + prev)
            else:
                f.write("\n\n" + prev + "    |    " + next)
            f.close()

if __name__ == "__main__":
    main()