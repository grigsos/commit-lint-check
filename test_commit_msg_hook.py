import pytest
from scripts.commit_msg_checker import check_commit_message

# Simulate the commit messages in a dictionary
# Key: Commit message, Value: Expected result (0 for pass, 1 for fail)
TEST_COMMIT_MESSAGES = {
    "feat: add new user login feature": 0,
    "fix: correct minor typo in code": 0,
    "feat(database): implement new indexing strategy": 0,
    "chore(build): update build script for new dependencies": 0,
    "feat add user authentication system": 1,
    "fix:correct a bug in the API": 1,
    "update: modify README file": 1,
    ": add new logging functionality": 1,
    "refactor codebase: optimize database queries": 1,
}

@pytest.mark.parametrize("message, expected", TEST_COMMIT_MESSAGES.items())
def test_commit_message_format(message, expected, tmp_path):
    # Write the message to a temporary file
    tmp_file = tmp_path / "commit_msg"
    tmp_file.write_text(message)

    # Check the commit message
    result = check_commit_message(str(tmp_file))
    assert result == expected
