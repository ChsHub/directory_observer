# Path Observer

(Windows only) Observe directory changes, and notify observers when a change is detected.

## Installation

`python3 -m pip install directory-observer`

## Usage Examples

```python

from directory_observer import DirectoryObservable


def update(path: str):
    # Handle change in path

# Initialize Observable with update() as observer function
observable = DirectoryObservable(path, observers=[update])
observable.start()  # Start observable thread

observable.remove_observer(update)
observable.add_observer(update)

observable.stop()  # Stop observable thread
```