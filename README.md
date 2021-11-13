# Fuck Kakao Page

> 한번해보자 씨발
> 2021/11/12 (금), 병신같은 카카오 페이지의 컨텐츠 소유권 규정과 IP BAN에 분노하며, 나

카카오 페이지의 공개 웹툰을 웹 크롤러를 사용해서 받아오는 프로젝트

## Progress

- [X] 1. create_dir_for_md.py
- [X] 2. add_file_nav.py
- [ ] 3. git_init.py
- [ ] 4. write_img_html_to_md.py
- [ ] 5. html_cleanup.py
- [ ] 6. git_deploy_md.py
- [X] 7. github_crawl.py
- [ ] 8. generate_epub.py

## 순서

```console 
usr@machine:~$ python ./script/create_dir_for_md.py && python ./script/add_file_nav.py

usr@machine:~$ python ./script/git_init.py

usr@machine:~$ python ./script/write_img_html_to_md.py

usr@machine:~$ python ./script/html_cleanup.py

usr@machine:~$ python ./script/git_deploy_md.py

usr@machine:~$ python ./script/github_crawl.py

```