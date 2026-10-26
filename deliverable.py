"""
Guide: Run your first Django project

This guide walks you through running your first Django project for the
Huerte/Vault-of-Forbidden-Knowledge repository.

Source: https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues/41

Constraints:
- Pure Python
- No external dependencies
- No subprocess, ctypes, socket, sys.exit, os.system, or eval

Author: [Your Name]
"""

from typing import List


def print_section(title: str) -> None:
    """Prints a formatted section title."""
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title) + "\n")


def guide_run_django_project() -> None:
    """
    Prints a step-by-step guide to run your first Django project
    for Huerte/Vault-of-Forbidden-Knowledge.
    """
    print_section("Guide: Run Your First Django Project")

    steps: List[str] = [
        "1. Clone the repository:",
        "   git clone https://github.com/Huerte/Vault-of-Forbidden-Knowledge.git",
        "",
        "2. Change into the project directory:",
        "   cd Vault-of-Forbidden-Knowledge",
        "",
        "3. (Optional but recommended) Create and activate a Python virtual environment:",
        "   python3 -m venv venv",
        "   # On Linux/macOS:",
        "   source venv/bin/activate",
        "   # On Windows:",
        "   venv\\Scripts\\activate",
        "",
        "4. Install Django and project dependencies:",
        "   pip install -r requirements.txt",
        "",
        "5. Apply database migrations:",
        "   python manage.py migrate",
        "",
        "6. (Optional) Create a superuser for the admin site:",
        "   python manage.py createsuperuser",
        "",
        "7. Run the development server:",
        "   python manage.py runserver",
        "",
        "8. Open your web browser and go to:",
        "   http://127.0.0.1:8000/",
        "",
        "9. (Optional) Access the Django admin site at:",
        "   http://127.0.0.1:8000/admin/",
        "",
        "You're now running your first Django project!",
    ]

    for line in steps:
        print(line)

    print_section("Troubleshooting")
    troubleshooting: List[str] = [
        "- If you see 'ModuleNotFoundError', ensure you installed dependencies with pip.",
        "- If you see 'Permission denied', check your Python and pip permissions.",
        "- For further help, see the Django documentation: https://docs.djangoproject.com/",
    ]
    for line in troubleshooting:
        print(line)


if __name__ == "__main__":
    guide_run_django_project()