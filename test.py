# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
#
# class Foo(object):
#
#     def __iter__(self):
#         yield 1
#         yield 2
#
#
#
# for i in Foo():
#     print(i)

import re

path_info = "/arya/arya/permission/1/change"

pattern = "/arya/arya/peission/\d+/change"

v = re.match(pattern,path_info)
print(v)