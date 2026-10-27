\[← Back to README](../../../README.md) | \[Contributing Guide](../../../CONTRIBUTING.md)



\---



| Field               | Value                         |

| ------------------- | ----------------------------- |

| \*\*Title\*\*           | Run Your First Django Project |

| \*\*Section\*\*         | docs                          |

| \*\*Category\*\*        | programming-dev/frameworks    |

| \*\*Difficulty\*\*      | Beginner                      |

| \*\*Last verified\*\*   | 2026-10-27                    |

| \*\*Prerequisites\*\*   | Python, pip, and a terminal   |

| \*\*Has screenshots\*\* | No                            |



\---



\# Run Your First Django Project



\## Overview



This guide helps beginners create and run their first Django project. You will install Django, start a project, run the development server, and open Django's welcome page in a browser.



\## Before You Start



\* Python 3 installed on your computer.

\* pip available to install Python packages.

\* A terminal or command prompt.



Check that Python and pip are available:



```bash

python --version

python -m pip --version

```



\## Steps



\### 1. Create a project folder and virtual environment



Create a folder for your project and enter it:



```bash

mkdir my-django-project

cd my-django-project

```



Create a virtual environment:



```bash

python -m venv .venv

```



Activate it on Windows:



```bash

.venv\\Scripts\\activate

```



On macOS or Linux, use:



```bash

source .venv/bin/activate

```



A virtual environment keeps this project's Python packages separate from other projects.



\### 2. Install Django



Install Django using pip:



```bash

python -m pip install Django

```



Verify the installation:



```bash

python -m django --version

```



The command should display the installed Django version.



\### 3. Create a Django project



Create a project named `mysite` in the current directory:



```bash

django-admin startproject mysite .

```



The final dot tells Django to create the project in the current directory rather than creating another nested folder.



\### 4. Run the development server



Start Django's local development server:



```bash

python manage.py runserver

```



The terminal should display a message indicating that the development server is running, usually at `http://127.0.0.1:8000/`.



Keep the terminal open while using the server.



\### 5. Open the welcome page



Open the following address in your web browser:



`http://127.0.0.1:8000/`



You should see Django's default welcome page, confirming that your first project is running.



To stop the server, return to the terminal and press `Ctrl+C`.



\## Verification



Run the development server:



```bash

python manage.py runserver

```



Open `http://127.0.0.1:8000/` in your browser.



Expected result: Django's default welcome page appears without an error.



\## Common Errors



\* `python is not recognized` → Python may not be installed or added to PATH. Install Python and ensure it is available from your terminal.

\* `No module named django` → Activate the virtual environment and run `python -m pip install Django`.

\* `That port is already in use` → Another process is using port 8000. Stop that process or run `python manage.py runserver 8001`.

\* `CommandError: Destination directory ... does not exist` → Check that you created and entered the project folder before running `django-admin startproject`.

\* The browser cannot connect → Make sure the development server is running and open the address shown in the terminal.



