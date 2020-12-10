#!python3
#coding:utf-8

'''
This module is coded by Yuning Ju

Copyright 2018 Yuning Ju

实现：大文件的MD5校验

'''
import hashlib,time


def md5_check(fh):
    '''
    Calculate the md5 of files
    将文件分块读入内存，防止内存溢出

    '''

    fp.seek(0)
    fr = fp.read(8096)
    while fr:
        yield fr
        fr = fp.read(8096)
    else:
        fp.seek(0)


if __name__ == '__main__':
    start = time.clock()
    filename = input('请输入文件路径：')
    m = hashlib.md5()
    with open(filename,'rb') as fp:
        for fr in md5_check(fp):
            m.update(fr)    #逐次更新校验值
    end = time.clock()
    print(m.hexdigest(),'\n用时: %.3f s' %(end-start))