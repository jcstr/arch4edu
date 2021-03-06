#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}, {'github': 'torch/trepl'}]
build_prefix = 'extra-x86_64'
repo_depends = ['lua51-penlight', 'torch7-cwrap-git', 'torch7-git', 'torch7-paths-git']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
