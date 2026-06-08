#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pre-commit 自定义校验脚本
校验规则：
  1. 禁止 .py 文件中存在调试输出语句
  2. 禁止文件中存在未完成标记（待办/待修复）
  3. 检查 .xml 文件是否格式合法
"""

import subprocess
import sys
import xml.etree.ElementTree as ET
import io

# 强制 stdout 使用 utf-8 输出
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def get_staged_files():
    """获取所有已暂存的文件列表"""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        capture_output=True, text=True
    )
    return result.stdout.strip().splitlines()


def check_no_print(filepath):
    """检查 Python 文件中是否含有 print() 调试语句"""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f, 1):
            if "print(" in line:
                print(f"  [FAIL] [{filepath}] 第 {i} 行包含 print() 语句，请删除后再提交")
                return False
    return True


def check_no_todo(filepath):
    """检查文件中是否含有 TODO / FIXME 标记"""
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f, 1):
            if "TODO" in line or "FIXME" in line:
                print(f"  [FAIL] [{filepath}] 第 {i} 行包含 TODO/FIXME，请处理后再提交")
                return False
    return True


def check_xml_valid(filepath):
    """检查 XML 文件格式是否合法"""
    try:
        ET.parse(filepath)
    except ET.ParseError as e:
        print(f"  [FAIL] [{filepath}] XML 格式错误: {e}")
        return False
    return True


def main():
    staged_files = get_staged_files()
    if not staged_files:
        print("[INFO] 没有暂存文件，校验跳过")
        sys.exit(0)

    print(f"[INFO] 开始校验 {len(staged_files)} 个暂存文件...\n")
    passed = True

    # 当前脚本自身路径，跳过对自身的检查
    this_script = "scripts/pre_commit_check.py"

    for filepath in staged_files:
        if filepath == this_script:
            print(f"  [SKIP] {filepath} （校验脚本自身，跳过检查）")
            continue
        try:
            if filepath.endswith(".py"):
                if not check_no_print(filepath):
                    passed = False
            if not check_no_todo(filepath):
                passed = False
            if filepath.endswith(".xml"):
                if not check_xml_valid(filepath):
                    passed = False
        except FileNotFoundError:
            pass  # 文件已删除，跳过

    if passed:
        print("[PASS] 所有校验通过，允许提交！")
        sys.exit(0)
    else:
        print("\n[BLOCKED] 校验未通过，提交已阻止，请修复以上问题后重试。")
        sys.exit(1)


if __name__ == "__main__":
    main()
