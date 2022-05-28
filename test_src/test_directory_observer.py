from pathlib import Path
from tempfile import TemporaryDirectory

from directory_observer import DirectoryObservable


def assert_error(function: callable, error):
    try:
        function()
    except error:
        assert True
        return
    assert False


def test___init__():
    def update(_path: str):
        assert str(path) == _path

    assert_error(lambda: DirectoryObservable('invalid_path'), FileNotFoundError)
    with TemporaryDirectory() as path:
        observable = DirectoryObservable(path, observers=[update])
        observable.start()
        new_file = Path(path, 'new_file')
        new_file.touch()
        observable.stop()


def test_add_observer():
    def update(_path: str):
        pass

    with TemporaryDirectory() as path:
        observable = DirectoryObservable(path)
        observable.add_observer(update)
        assert update in observable._observers
        observable.stop()


def test_remove_observer():
    def update(_path: str):
        pass

    with TemporaryDirectory() as path:
        observable = DirectoryObservable(path, observers=[update])
        assert update in observable._observers
        observable.remove_observer(update)
        assert update not in observable._observers
        observable.stop()


def test__notify_observers():
    class TestNotify:
        called = False

        def _update(self, _path: str):
            self.called = True
            assert test_notify.called

    with TemporaryDirectory() as path:
        test_notify = TestNotify()
        observable = DirectoryObservable(path, observers=[test_notify._update])
        observable.start()
        assert not test_notify.called
        new_file = Path(path, 'new_file')
        new_file.touch()
        observable.stop()


def test_stop():
    def update(_path: str):
        pass

    with TemporaryDirectory() as path:
        observable = DirectoryObservable(str(path), observers=[update])
        observable.start()
        assert observable.is_alive()
        observable.stop()
        assert not observable.is_alive()


def test_run():
    def update(_path: str):
        assert False

    with TemporaryDirectory() as path:
        observable = DirectoryObservable(str(path), observers=[update])
        observable._active = False
        observable.run()


def test___enter__():
    def update(_path: str):
        assert str(path) == _path

    assert_error(lambda: DirectoryObservable('invalid_path'), FileNotFoundError)
    with TemporaryDirectory() as path:
        with DirectoryObservable(path, observers=[update]) as observable:
            assert observable.is_alive()
            new_file = Path(path, 'new_file')
            new_file.write_text('TEST')
        assert not observable.is_alive()
