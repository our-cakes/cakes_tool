# main.py

import argparse
import subprocess
print('''
              _                 _                  _ 
  ___   __ _ | | __  ___  ___  | |_   ___    ___  | |
 / __| / _` || |/ / / _ \/ __| | __| / _ \  / _ \ | |
| (__ | (_| ||   < |  __/\__ \ | |_ | (_) || (_) || |
 \___| \__,_||_|\_\ \___||___/  \__| \___/  \___/ |_|
                                        @auther:羔子
                                        version:1.0
Please enter 'python3 cakes.py -c' to view help''')
def call_module(script_name, args):
    """
    调用指定的脚本，并传递参数。

    参数:
    script_name (str): 要调用的脚本名称
    args (list): 要传递给脚本的参数
    """
    cmd = ['python3', script_name] + args
    subprocess.run(cmd)


def main():
    """
    主函数，解析命令行参数并根据参数决定是否调用模块功能。
    """
    # 创建 ArgumentParser 对象，用于解析命令行参数
    parser = argparse.ArgumentParser(description="Main script to trigger some functionality.",add_help=False)

    # 定义参数和对应脚本的映射

    #在此添加自定义模块：'test(--test调用)':(文件路径,帮助)'
    #
    features = {
        'passwd_collect': ('passwd_collect/Password_set.py','密码整合模块'),
        'redis_master': ('redis_copy/redis_rogue_server.py','redis主从复制exp')
        #'example':('example/example.py','help')
    }

    # 动态添加参数
    # for feature, (short_opt, _) in features.items():
    #     parser.add_argument(short_opt, f'--{feature}', action='store_true', help=f'Enable {feature} function')

    #
    # for feature, (_,_,hme) in features.items():
    #     parser.add_argument(f'--{feature}', action='store_true', help=f'Enable {feature} function')
    for feature, (_,hme) in features.items():
        parser.add_argument(f'--{feature}', action='store_true', help=f'{hme}')

    parser.add_argument('-c', action='help', help='show this help message')
    # 解析命令行参数
    args, unknown = parser.parse_known_args()

    # 动态调用对应的脚本
    for feature, (script,_) in features.items():
        if getattr(args, feature):
            call_module(script, unknown)


if __name__ == "__main__":
    # 调用主函数
    main()
