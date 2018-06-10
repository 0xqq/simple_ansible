# encoding: utf-8

import json
from ansible_api import MyRunner
# 传入inventory路径
ansible = MyRunner('./host')  # 指定host文件
# 获取服务器磁盘信息
module_name = 'shell'
module_args = 'cat /etc/redhat-release'
# ansible.run('all', 'setup', "filter='ansible_mounts'") # 获取磁盘数据
ansible.run('all', module_name, module_args)
#结果
result=ansible.get_result()
#成功
succ = result['success']
#失败
failed = result['failed']
#不可达
unreachable = result['unreachable']

print(succ)
print(failed)
print(unreachable)
s = json.dumps(succ, indent=4)  # 序列化为json数据
print(s)