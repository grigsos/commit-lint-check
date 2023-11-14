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
    ("docs: updated documentation", 1),  # Missing new line after header
    ("feat(scope): this is a very long message that exceeds the maximum allowed length for a commit message header, which should result in an error", 1),
    # Add more test cases here
])
def test_commit_message(message, expected):
    file_name = create_temp_commit_message(message)
    assert check_commit_message(file_name) == expected