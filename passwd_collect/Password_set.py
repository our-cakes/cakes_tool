# password_set.py

import argparse
import datetime
import os
from collections import Counter


def read_file_to_list(file_path):
    """
    读取文件内容并将每一行加载到一个列表中。

    参数:
    file_path (str): 文件的路径

    返回:
    list: 包含文件每一行内容的列表
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # 去除每行末尾的换行符
    lines = [line.strip() for line in lines]
    return lines


def save_password(output_path, lines):
    """
    将列表内容保存到指定的输出文件中。

    参数:
    output_path (str): 输出文件的路径
    lines (list): 要保存的内容列表
    """
    with open(output_path, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")


def count_duplicates(all_lines):
    """
    计算重复的行数。

    参数:
    all_lines (list): 包含所有行内容的列表

    返回:
    int: 重复行的数量
    """
    line_counts = Counter(all_lines)
    duplicates = [line for line, count in line_counts.items() if count > 1]
    return len(duplicates)


def print_help():
    """
    打印自定义的帮助信息。
    """
    help_text = """
    Load file content into a list, remove duplicates, and save to an output file.
    examople: python main.py -F -f passwd1.txt -f passwd2.txt -o pass.txt
    optional arguments:
      -h, --help            show this help message and exit
      -f FILE, --file FILE  Path to the input file(s)
      -o OUTPUT, --output OUTPUT
                            Path to the output file
        
    """
    print(help_text)


def main():
    """
    主函数，解析命令行参数并读取指定文件的内容，然后保存到输出文件中。
    """
    # 创建 ArgumentParser 对象，用于解析命令行参数
    parser = argparse.ArgumentParser(add_help=False)

    # 添加 -h/--help 参数，用于显示帮助信息
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    # 添加 -f/--file 参数，允许多次出现，用于指定多个文件路径
    parser.add_argument('-f', '--file', type=str, action='append', required=False, help='Path to the input file(s)')

    # 添加 -o/--output 参数，用于指定输出文件路径
    parser.add_argument('-o', '--output', type=str, help='Path to the output file')

    # 解析命令行参数
    args = parser.parse_args()

    # 如果用户请求帮助信息，则打印帮助信息并退出
    if args.help:
        print_help()
        return

    # 检查是否提供了文件路径
    if not args.file:
        print("Error: No input files specified. Use -f to specify input files.")
        print_help()
        return

    file_paths = args.file
    output_path = args.output

    # 如果没有指定输出文件路径，则使用当前时间生成默认文件名
    if not output_path:
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = f"output/passwd_collect{current_time}.txt"
    else:
        output_path = f"output/{output_path}"

    # 创建 output 目录（如果不存在）
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # 初始化一个空列表，用于存储所有文件的内容
    all_lines = []

    # 遍历所有指定的文件路径
    for file_path in file_paths:
        try:
            # 读取文件内容并将其添加到总列表中
            lines = read_file_to_list(file_path)
            all_lines.extend(lines)
        except Exception as e:
            # 捕获并打印读取文件时的异常
            print(f"Error reading file {file_path}: {e}")

    # 计算重复的行数
    duplicate_count = count_duplicates(all_lines)
    print(f"Number of duplicate lines: {duplicate_count}")

    # 对列表进行去重操作
    unique_lines = list(set(all_lines))

    # 打印去重后的行数
    print(f"Number of unique lines: {len(unique_lines)}")

    # 提示用户确认是否要保存到文件
    user_input = input("Do you want to save the unique lines to the output file? (yes/no): ").strip().lower()
    if user_input != 'no':
        # 将去重后的内容保存到输出文件中
        try:
            save_password(output_path, unique_lines)
            print(f"All file contents saved to {output_path}")
        except Exception as e:
            print(f"Error saving to file {output_path}: {e}")
    else:
        print("File not saved.")


if __name__ == "__main__":
    # 调用主函数
    main()
