[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)

# PostgreSQL psql Commands Cheatsheet (Quick Reference)

A simple, practical reference sheet for connecting to PostgreSQL and using essential `psql` interactive prompt slash commands.

## 1. Connecting to PostgreSQL

```bash
psql -U postgres                                 # Connect to local PostgreSQL as postgres user
psql -U username -d mydatabase                   # Connect to a specific database with a username
psql -h localhost -p 5432 -U username -d mydatabase # Connect to a specific host and port
psql "postgresql://user:password@localhost:5432/mydatabase" # Connect using a full connection URI
```

## 2. Navigating Databases and Connections

```text
\l                                               # List all databases on the server
\c dbname                                        # Connect / switch to another database
\c dbname username                               # Connect to a database as a different user
\conninfo                                        # Display current connection details (host, port, user)
```

## 3. Inspecting Tables, Views, and Schema

```text
\dt                                              # List all tables in current schema
\dt+                                             # List tables with size, persistence, and description
\dv                                              # List all views
\d table_name                                    # Describe columns, types, and modifiers of a table
\d+ table_name                                   # Describe table with indexes, constraints, and storage
\dn                                              # List all schemas
\du                                              # List all database users and roles
```

## 4. Query Formatting and Session Controls

```text
\x                                               # Toggle expanded display (auto/on/off for wide columns)
\timing                                          # Toggle query execution timing on or off
\e                                               # Open current query buffer in external text editor
\s                                               # View psql command history
```

## 5. Running Files and Output Redirection

```text
\i path/to/script.sql                            # Execute SQL commands from a file
\o query_output.txt                              # Redirect query results to a file
\o                                               # Reset query output back to terminal screen
```

## 6. Help and Exiting

```text
\?                                               # Show help on psql slash commands
\h SELECT                                        # Show SQL syntax help for a specific SQL command
\q                                               # Quit and exit the psql prompt
```
