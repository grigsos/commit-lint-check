import pytest
import tempfile
from scripts.commit_msg_checker import check_commit_message


def create_temp_commit_message(content):
    temp_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    temp_file.write(content)
    temp_file.close()
    return temp_file.name

@pytest.mark.parametrize("message,expected", [
    ("feat(scope): initial commit\n\nDetailed explanation.", 0),
    ("fix: fix issue with regex\n\n- Fixed regex parsing error.", 0),
    ("docs: updated documentation", 0),  # Missing new line after header
    ("feat(scope): this is a very long message that exceeds the maximum allowed length for a commit message header, which should result in an error", 1),
    
    
    # Invalid type or scope
    ("unknown(scope): added new feature", 1),
    ("feat(123Scope): invalid scope format", 1),

    # Invalid subject
    ("feat: ", 1),
    ("fix: no lowercase subject.", 1),

    # Long header
    ("feat(scope): " + "a" * 90, 1),  # Header too long

    # Missing blank line after header
    ("feat(scope): subject\nDetailed explanation.", 1),

    # Long lines in body
    ("fix: short header\n\n" + "a" * 101, 1),  # Body line too long

    # Footer issues
    ("feat: short header\n\nBody content\nBREAKING CHANGE: " + "a" * 101, 1),  # Long line in footer
    ("feat: short header\nBREAKING CHANGE: footer content", 1)  # Missing blank line before footer
])
def test_commit_message(message, expected):
    file_name = create_temp_commit_message(message)
    assert check_commit_message(file_name) == expected