# Directory Observer

(Windows only) The package implements an observable to monitor directory changes, and to notify observers when a change is detected. 
The observable is running in a separate daemon thread, and is being locked while there are no changes (non-busy-waiting). 

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

