#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'oldratlee'

import psutil

# p = psutil.Process()
#
# print p.threads()
#
# for p in psutil.process_iter():
#     print "=" * 80
#     try:
#         print p
#         print "%s %s --> %s" % (p.name(), p.exe(), p.num_threads())
#
#         for t in p.threads():
#             print t
#
#         #p.threads()
#     except psutil.ZombieProcess:
#         pass
#     except psutil.AccessDenied:
#         print "!!!!!!!!!! AccessDenied %s, skip!" % (p)
#         pass

process = psutil.Process(97128)
for process.threads()
