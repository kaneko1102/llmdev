import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    authenticator = Authenticator()
    yield authenticator

@pytest.mark.parametrize("username, password", [
    ("user1", "password"),
    ("taro", "pass"),
    ("yamada123", "qwerty"),
    ("abc", "12345"),
])
def test_register(authenticator, username, password):
    authenticator.register(username, password)
    assert authenticator.users[username] == password

@pytest.mark.parametrize("username1, password1, username2, password2", [
    ("user1", "password", "user1", "password"),
    ("taro", "pass", "taro", "pass"),
    ("yamada123", "qwerty", "yamada123", "asdfg"),
    ("abc", "12345", "abc", "67890"),
])
def test_register_duplicate(authenticator, username1, password1, username2, password2):
    authenticator.register(username1, password1)
    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register(username2, password2)

@pytest.mark.parametrize("username, password", [
    ("user1", "password"),
    ("taro", "pass"),
    ("yamada123", "qwerty"),
    ("abc", "12345"),
])
def test_login(authenticator, username, password):
    authenticator.register(username, password)
    assert authenticator.login(username, password) == "ログイン成功"


@pytest.mark.parametrize("username1, password1, username2, password2", [
    ("user1", "password", "user1", "password2"),
    ("taro", "pass", "hanako", "pass"),
    ("yamada123", "qwerty", "yamada", "asdfg"),
    ("abc", "12345", "abc", "67890"),
])
def test_login_fail(authenticator, username1, password1, username2, password2):
    authenticator.register(username1, password1)
    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login(username2, password2)