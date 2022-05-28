# Directory Observer

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

observable.remove_observer(update) # Remove observer
observable.add_observer(update) # Add new observer

observable.stop()  # Stop observable thread
```


```python
# Use "with" statement to call start() and stop()
with DirectoryObservable(path, observers=[update]) as observable:
    # Observe directory in this section
```

