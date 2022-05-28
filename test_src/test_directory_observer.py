from pathlib import Path
from tempfile import TemporaryDirectory

import win32con
import win32event

from directory_observer import DirectoryObservable


def assert_error(function: callable, error):
    try:
        function()
    except error:
        assert True
        return
    assert False


def test___init__(
        timeout: int = win32event.INFINITE,
        watch_sub_directories: bool = False,
        change_flags=win32con.FILE_NOTIFY_CHANGE_LAST_WRITE):
    """
    :param observers: List of observer functions
    :param timeout: Timeout for event; Infinity by default
    :param path: File or directory to observe
    :param watch_sub_directories: True if changes in sub directories should be observed
    :param self.change_flags: Flags specifying what changes to watch
    """

    def update(_path: str):
        assert new_file == _path

    assert_error(lambda: DirectoryObservable('invalid_path'), FileNotFoundError)
    with TemporaryDirectory() as path:
        observable = DirectoryObservable(path, observers=[update])
        observable.start()
        new_file = Path(path, 'new_file').touch()


def test_add_observer(update_function: callable):
    """
    Add observer function. The function is called on detected directory change with path as argument.
    :param update_function: Callback function
    """
    pass


def test_remove_observer(update_function: callable) -> bool:
    """
    Observe path, and call function on change
    :param update_function: Callback function
    """
    pass


def test__notify_observers(self):
    """
    Notify all observers about directory change
    """
    pass


def test_stop(timeout: float = None) -> None:
    """
    Stop the active thread
    :param timeout: Timeout for joining the thread
    """
    pass


def test_run(self) -> None:
    """
    run() function is started on Thread.start().
    """
    pass
