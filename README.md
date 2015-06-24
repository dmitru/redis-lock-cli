# Relock - CLI for Redis locks
Command line interface around python-redis-lock project. Might be useful when using locks in bash scripts.

For predictable behaviour you should automatically generate lock names so that each lock name is used only once in 
lock/try-release call sequence.

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

