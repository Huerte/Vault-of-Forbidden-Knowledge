[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)

# Linux Terminal Basics Cheatsheet (Quick Reference)

A simple, practical reference sheet for navigating the filesystem, managing files, and running commands in the Linux terminal.

## 1. Navigating the Filesystem

```bash
pwd                                              # Print current working directory path
ls -la                                           # List all files (including hidden) with detailed permissions
cd /path/to/folder                               # Change directory to a specific path
cd ..                                            # Move up one directory level
cd ~                                             # Return to your home directory
```

## 2. Managing Files and Directories

```bash
mkdir my-folder                                  # Create a new directory
mkdir -p path/to/nested/folder                   # Create nested parent directories if they do not exist
touch file.txt                                   # Create an empty file or update timestamp
cp source.txt destination.txt                    # Copy a file to a new location
cp -r folder/ backup/                            # Copy an entire directory recursively
mv old-name.txt new-name.txt                     # Rename or move a file or directory
rm file.txt                                      # Delete a file
rm -rf folder/                                   # Delete a directory and all its contents recursively
```

## 3. Reading and Searching Files

```bash
cat file.txt                                     # Print entire file content to terminal
less file.txt                                    # View file page by page (q to exit)
head -n 20 file.txt                              # View the first 20 lines of a file
tail -n 20 -f app.log                            # View the last 20 lines and follow live updates
grep -rn "search_term" .                         # Recursively search for text across files with line numbers
find . -name "*.py"                              # Find files matching a pattern in the current folder
```

## 4. File Permissions and Ownership

```bash
chmod +x script.sh                               # Make a script executable
chmod 644 file.txt                               # Set read/write for owner, read-only for others
chmod 755 folder/                                # Standard executable directory permissions
sudo chown user:group file.txt                   # Change file owner and group
```

## 5. System, Disk, and Process Management

```bash
df -h                                            # Show available disk space in human-readable format
du -sh folder/                                   # Show total disk space used by a directory
ps aux | grep node                               # List active processes matching a name
top                                              # Monitor real-time system resource usage (q to exit)
kill 1234                                        # Terminate a process by its PID
kill -9 1234                                     # Forcefully kill an unresponsive process
```
