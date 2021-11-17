#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://camo.githubusercontent.com/ 를 이용해서 익명 URL 프록시를 만들기 위해서 마크다운을 만든다. 깃헙이 마크다운의 이미지 링크를 자동으로 camo를 사용해 익명 호스팅 해주기 때문에 selenium 등의 크롤러를 사용해도 IP Ban을 당하지 않는다.

만약 IP 차단을 먹었다고 해도 이 방식으로 우회가 가능하다. camo에 의한 프록시가 kakao에 이미지 파일을 요청할때 나의 IP를 사용하지 않기 때문이다.
"""

import os

def main():

    # 디렉토리 이름
    target_dir = "[md] 프로야구 생존기"

    new_ep = 191

    # 만들 총 에피소드 범위, 0 index
    start_idx, end_idx = new_ep - 1, new_ep

    # 이미 디렉토리가 있는지 확인
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # 마크다운 파일 생성
    for i in range(start_idx, end_idx):
        filename = os.path.join(target_dir, f'{i+1:03d}') + '.md'
        open(filename, 'x')
        # print(filename)

    

if __name__ == "__main__":
    main()