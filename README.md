# Path Observer

Observe directory on Windows. Notify listeners on directory changes.

## Installation

`python3 -m pip install directory-observer`

## Usage Examples

```python

from directory_observer import DirectoryObservable


def update(path: str):
    # Handle change in path

observable = DirectoryObservable(path)
observable.add_observer(update)
observable.start()  # Start observable thread

observable.stop()  # Stop observable thread
```