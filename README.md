# backup-comparator

The program accepts three string arguments: 
```
- first backup folder path
- second backup folder path
- target backup path
```
It compares the contents of the source and target backup and produce a new backup with the same format containing only changes.
I decided that `source` has to be the newer one and that's why it is a standard.

## Instruction

It is highly recommended to pass `first backup folder path`, `second backup folder path` and `target backup path` 
as the command line arguments, using this syntax:

```bash
python3 app/main.py ../data/src/ ../data/tgt/ ../data/changes/
```

Though it might be more convinient to run `main.py` without command line arguments, 
but keep in mind that it will take much more time to pass the arguments in the `input()`.

**Note**: the command is correct if you are running it from the `backup-comparator` directory, 
otherwise replace `app/main.py` with the path to the `main.py` from the current directory.
