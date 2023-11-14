#!/usr/bin/env python3
import sys
import re

def check_commit_message(commit_msg_file):
    pattern = r"^(feat|fix|docs|style|refactor|perf|test|chore)(\(\w+\))?: .+"
    with open(commit_msg_file, 'r') as file:
        content = file.read().strip()

        # Check if commit message matches the pattern
        if not re.match(pattern, content, re.DOTALL):
            print("Commit message does not follow the specified format!")
            print("Expected format: <type>[optional scope]: <description>\n[optional body]\n[optional footer(s)]")
            return 1

    return 0

if __name__ == "__main__":
    exit_code = check_commit_message(sys.argv[1])
    sys.exit(exit_code)
