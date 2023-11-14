#!/usr/bin/env python3
import sys
import re

def check_commit_message(commit_msg_file):
    # Define the patterns and rules
    max_header_length = 100
    max_line_length = 100

    with open(commit_msg_file, 'r') as file:
        lines = file.readlines()
        header = lines[0].strip()

        type_scope_regex = r"^(feat|fix|docs|style|refactor|perf|test|chore|build|ci|revert)(\([a-z0-9]+\))?:"
        type_scope_match = re.match(type_scope_regex, header)

        # Regular expression for subject
        subject_regex = r".*:\s[a-z0-9].*[^\.]$"

        subject_match = re.match(subject_regex, header)

        # Check for type and scope validity
        if not type_scope_match or type_scope_match.group(1).lower() != type_scope_match.group(1):
            print("Error: Commit type and scope are invalid, not in lower case, or empty.")
            return 1
        elif not subject_match:
        # Check for subject validity
            print("Error: Commit subject is invalid.")
            return 1
        else:
            print("Commit message is valid.")

        # Check header-max-length
        if len(header) > max_header_length:
            print(f"Error: Commit header is longer than {max_header_length} characters.")
            return 1

        # Check body-leading-blank, body-max-line-length
        if len(lines) > 1:
            if not lines[1].strip() == "":
                print("Error: No blank line after header.")
                return 1
            for line in lines[2:]:
                if len(line.strip()) > max_line_length:
                    print(f"Error: Line in commit body is longer than {max_line_length} characters.")
                    return 1

        # Check footer-leading-blank, footer-max-line-length
        if 'BREAKING CHANGE:' in header:
            footer_index = lines.index('BREAKING CHANGE:')
            if not lines[footer_index - 1].strip() == "":
                print("Error: No blank line before footer.")
                return 1
            for line in lines[footer_index:]:
                if len(line.strip()) > max_line_length:
                    print(f"Error: Line in footer is longer than {max_line_length} characters.")
                    return 1

    return 0

if __name__ == "__main__":
    exit_code = check_commit_message(sys.argv[1])
    sys.exit(exit_code)
 