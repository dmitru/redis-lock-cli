# Relock - CLI for Redis locks
Command line interface around python-redis-lock project.
 
Provides CLI interface for named locks implemented with Redis storage.

# Installation
```sh
pip install -r ./requirements.txt
```

# Usage
## Acquiring a named lock (blocking mode):
```sh
python relock.py lock <lock_name>
```

This will block until the lock is acquired.

## Trying to acquire a lock in non-blocking mode:

```sh
python relock.py try <lock_name>
```

## Releasing a lock:
```sh
python relock.py release <lock_name>
```

