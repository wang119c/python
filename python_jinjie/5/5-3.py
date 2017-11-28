# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 如何设置文件的缓冲?
# 实际案例:将文件内容写入d到硬盘时,使用系统调用,这类i/o操作的时间很长,为了减少i/o操作的次数,文件通常使用缓冲区,如何设置python中的缓冲行为?  缓冲区的大小是4096
# 全缓冲 buffering设置大于1的任何整数,
# 行缓冲 buffering设置为1
# 无缓冲 buffering设置为0


# f = open('demo.txt','w')
# f.write('abc')
# f.write('+'*4093)
# f = open('demo.txt','w',buffering=2048)


# 如何将文件映射到内存?
# 实际案例:
# 1.在访问某些二进制文件时,希望能把文件映射到内存当中,可以实现随机访问(framebuffer设备文件)
# 2.某些嵌入式设备,j寄存地址到内存地址空间,w我们可以映射/dev/mem范围去访问这些寄存器
# 3.如果多个进程映射到一个文件,可以实现进程相互通信

import mmap

f = open('demo.bin','r+b')
f.fileno()
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
print type(m)

