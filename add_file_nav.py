#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
깃헙에서 에피소드간의 네비게이션을 쉽게 하기 위해서 relative path를 이용해 파일들의 전/후로 보내줄 마크다운 링크를 파일에 더한다.
"""

import os, argparse

# Global Flag
NEW_EPISODE = True

def main():
    # 마크다운 파일이 있는 디렉토리
    target_dir = "[md] 프로야구 생존기"
    # 해당 디렉토리의 모든 파일
    dirs = os.listdir(target_dir)
    # 가장 최근 에피소드
    latest = 192

    # For New
    if NEW_EPISODE:
        prev = "[" + f'{latest-1:03d}' + "](./" + f'{latest-1:03d}' + ".md)"
        next = "[" + f'{latest+1:03d}' + "](./" + f'{latest+1:03d}' + ".md)"
        with open(os.path.join(target_dir, str(latest) + ".md"), 'a') as f:
            f.write("\n\n" + prev + "    |    " + next)
            f.close()

    else:
        # 모든 파일을 스캔해서 전/후 에피소드의 상대 url을 구함
        for idx, filename in enumerate(dirs):
            prev = "[" + f'{idx:03d}' + "](./" + f'{idx:03d}' + ".md)"
            next = "[" + f'{idx+2:03d}' + "](./" + f'{idx+2:03d}' + ".md)"
            # 첫 에피는 후 링크, 막 에피는 전 링크만 달아둔다.
            with open(os.path.join(target_dir, filename), 'a') as f:
                if idx == 0:
                    f.write("\n\n" + next)
                else:
                    f.write("\n\n" + prev + "    |    " + next)
                f.close()

if __name__ == "__main__":
    main()