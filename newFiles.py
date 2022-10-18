#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

if __name__ == '__main__':

    args = sys.argv

    if len(args) < 2:
        raise Exception('缺少目录名称！\n示例：python newFiles.py dir_name')
    dir_name = args[1]

    with open("%s/files.txt" % dir_name, 'r+') as f:
        for line in f.readlines():
            file_name = line.replace("\n", "")
            with open("%s/%s.md" % (dir_name, file_name.replace(" ", "_")), 'w+') as md:
                md.writelines(("# %s\n" % file_name))
