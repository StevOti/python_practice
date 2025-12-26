# Python Practice — File I/O Demos

This small practice repository contains simple examples demonstrating basic file I/O operations in Python (read, write, append, create, delete) and a few sample text files.

**Files**
- `files.py`: Example script showing multiple file operations (read/append/write/create/delete). Contains a small bug in the last `with open(..., 'w')` block (see "Notes / Fix" below).
- `names.txt`: Sample names used by the script.
- `names_list.txt`: Another sample file created by the script.
- `more_names.txt`: Sample file with additional names.
- `unique_names.txt`: Created with exclusive-creation mode by the script.
- `context.txt`: Extra sample content.

How to run
- Ensure you have Python 3 installed.
- From the repository root run:

```powershell
python files.py
```

What the script does
- Prints the contents of `names.txt`.
- Appends `Stephen` to `names.txt` and prints contents again.
- Overwrites `names.txt` with a new list (`John`, `Doe`, `Jane`).
- Creates `names_list.txt` and writes three names into it.
- Attempts to create `unique_names.txt` using exclusive create (will not overwrite existing file).
- Attempts to delete `temp_file.txt` if present.
- Uses a `with open()` block for `more_names.txt` (intended to demonstrate safe file handling).

Important notes / Fix
- Warning: Running `files.py` will overwrite `names.txt` because the script uses write mode (`'w'`). Back up files if you want to preserve data before running.
- Bug: the final block opens `more_names.txt` with mode `'w'` and then calls `file.read()` which will raise an error because a file opened in write mode cannot be read. Replace that block with one of the following depending on intent:

To read `more_names.txt` safely:

```python
with open('more_names.txt', 'r') as file:
    content = file.read()
    print(content)
```

To write to `more_names.txt` safely (if the intent was to write):

```python
with open('more_names.txt', 'w') as file:
    file.write('Some\nNames')
```

Recommendations
- Prefer `with open(...)` for all file operations to ensure files are closed automatically.
- Avoid using hard-coded filenames if you want the script to be reusable; consider command-line args or a small CLI.
- Consider adding a small unit test or a dry-run flag that prevents destructive operations like overwriting or deleting files.

If you'd like, I can:
- Fix `files.py` to use `with` consistently and add a safe dry-run mode.
- Add a simple test or example runner.

--
Generated README for this workspace by the assistant.
