import pytest

from src.decorators import log


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    captured = capsys.readouterr()

    assert "my_function start" in captured.out
    assert "my_function ok" in captured.out


def test_log_bad(capsys):
    @log()
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(1, "L")

    captured = capsys.readouterr()

    assert "my_function error" in captured.out
    assert "TypeError" in captured.out
    assert "(1, 'L')" in captured.out


def test_log_file(tmp_path):

    target_file = tmp_path / "test_log.txt"

    @log(filename=str(target_file))
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    file_content = target_file.read_text()

    assert "my_function start" in file_content
    assert "my_function ok" in file_content


def test_log_file_bad(tmp_path):
    target_file = tmp_path / "test_log.txt"

    @log(filename=str(target_file))
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError):
        my_function(1, "L")

    file_content = target_file.read_text()
    assert "my_function error" in file_content
    assert "TypeError" in file_content
    assert "(1, 'L')" in file_content
