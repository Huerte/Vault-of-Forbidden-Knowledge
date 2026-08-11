[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | TablePlus: How to View and Edit PostgreSQL Databases with a GUI |
| **Section** | apps |
| **Category** | developer |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | TablePlus installed, PostgreSQL installed and running |
| **Has screenshots** | No |

---

# TablePlus: How to View and Edit PostgreSQL Databases with a GUI

## What It Does

Instead of typing black-and-white SQL commands into a terminal, **TablePlus** gives you a clean visual interface with buttons and tables (like Microsoft Excel) to view your rows, edit data, and run database queries.

---

## Part 1: Connect to a Local Database on Your Own Computer

Follow these exact steps to connect to PostgreSQL running on your laptop:

### Step 1: Open TablePlus and Create a Connection
1. Launch the **TablePlus** app from your Start Menu.
2. In the center of the welcome window, click the text that says **Create a new connection...** (or press **Ctrl + N** on your keyboard).
3. A list of database icons appears. Click on **PostgreSQL** to select it.
4. Click the blue **Create** button at the bottom right.

---

### Step 2: Fill in the Connection Form
A settings window opens. Fill in each field as follows:

- **Name:** `Local PostgreSQL` (or any friendly name you like).
- **Host / Socket:** `127.0.0.1` (or `localhost`).
- **Port:** `5432` (this is the default PostgreSQL port).
- **User:** `postgres` (or your custom username).
- **Password:** Type the password you created when installing PostgreSQL.
- **Database:** Type the name of your database (or type `postgres` if you do not have one yet).
- **SSL mode:** Change this dropdown to `DISABLE` (for local development).

---

### Step 3: Test and Save
1. Click the **Test** button at the bottom left.
2. Look at the small dots next to each field:
   - **All green:** Your password and port are correct!
   - **Red dot:** Read the error message at the bottom. If it says `password authentication failed`, check your password spelling.
3. Click **Connect** (or press **Ctrl + S** to save).
4. TablePlus opens into your database workspace.

---

## Part 2: Connect to a Remote Cloud Database over SSH (Tunneling)

If your database is hosted on an online server (like AWS, DigitalOcean, or Ubuntu VPS) and does not accept direct public connections:

1. Create a new PostgreSQL connection in TablePlus as shown above.
2. Look at the tabs near the top and click on **Over SSH** (or **SSH** tab).
3. Fill in your remote server details:
   - **Server:** Your remote server IP address (for example: `165.22.100.50`).
   - **Port:** `22`
   - **User:** `ubuntu` or `root`
   - **Auth:** Click the dropdown and pick `Use Private Key`.
   - **Key:** Click the folder icon and choose your private SSH key file (`id_ed25519` inside `C:\Users\<YourName>\.ssh`).
4. Click **Test** and then **Connect**. TablePlus will automatically build an encrypted bridge to your remote database.

---

## Useful Keyboard Shortcuts

| What You Want to Do | Windows Shortcut |
|---|---|
| Open a new SQL Query Editor window | `Ctrl + E` |
| Run the SQL query under your cursor | `Ctrl + Enter` |
| Run ALL queries in the editor | `Ctrl + Shift + Enter` |
| Quick search tables and views | `Ctrl + P` |
| Refresh / reload table data | `Ctrl + R` |
| Save your edits to the database | `Ctrl + S` |
| Cancel your uncommitted edits | `Ctrl + Z` |

---

## Good Things to Know (Gotchas)

- **The 2-Tab Free Limit:** On the free version of TablePlus, you can only keep 2 tabs open at the same time. If you want to open a third table or query editor, close one of the older tabs first by clicking the small `x` on the tab.
- **Inline Editing:** You can double-click any cell in a table to change its value directly, just like an Excel spreadsheet. When finished, press **Ctrl + S** to save your changes to the real database.
