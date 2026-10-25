"""
Module: github_actions_guide

This module provides a plain-English explanation of GitHub Actions,
suitable for inclusion in the Huerte/Vault-of-Forbidden-Knowledge repository.

No external dependencies are required.

Author: [Your Name]
Source: https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues/42
"""

from typing import List


def get_github_actions_guide() -> str:
    """
    Returns a plain-English guide explaining GitHub Actions.

    Returns:
        str: The explanation of GitHub Actions.
    """
    guide_lines: List[str] = [
        "# GitHub Actions: A Plain-English Guide",
        "",
        "## What is GitHub Actions?",
        "",
        "GitHub Actions is a feature built into GitHub that lets you automate tasks for your code repository.",
        "You can use it to automatically run tests, build your code, deploy your app, or do almost anything else you can script.",
        "",
        "## How Does It Work?",
        "",
        "GitHub Actions works by running 'workflows'. A workflow is a set of instructions (steps) that GitHub runs for you.",
        "You define these workflows in special files (YAML files) inside a `.github/workflows/` folder in your repository.",
        "",
        "## When Does a Workflow Run?",
        "",
        "You can tell GitHub when to run a workflow. For example, you can run workflows:",
        "- When someone pushes code",
        "- When someone opens a pull request",
        "- On a schedule (like every night)",
        "- Or even manually",
        "",
        "## What Can a Workflow Do?",
        "",
        "A workflow is made up of 'jobs', and each job has 'steps'. Each step can run a command or use a reusable 'action'.",
        "Some common things people do with workflows:",
        "- Run tests automatically when code changes",
        "- Build and deploy websites or apps",
        "- Check code for style or security problems",
        "",
        "## What is an Action?",
        "",
        "An 'action' is a reusable script that does one thing, like checking out code, setting up Python, or uploading files.",
        "You can use actions made by GitHub, the community, or write your own.",
        "",
        "## Example: Simple Workflow",
        "",
        "Here's what a simple workflow file might look like:",
        "",
        "```yaml",
        "name: Run Tests",
        "on: [push]",
        "jobs:",
        "  test:",
        "    runs-on: ubuntu-latest",
        "    steps:",
        "      - uses: actions/checkout@v3",
        "      - uses: actions/setup-python@v4",
        "        with:",
        "          python-version: '3.10'",
        "      - run: python -m unittest discover",
        "```",
        "",
        "This workflow runs every time someone pushes code. It checks out the code, sets up Python, and runs the tests.",
        "",
        "## Why Use GitHub Actions?",
        "",
        "- **Automation:** Save time by letting GitHub do repetitive tasks.",
        "- **Consistency:** Make sure tests and builds run the same way every time.",
        "- **Integration:** It works right inside GitHub, so you don't need extra tools.",
        "",
        "## Where to Learn More?",
        "",
        "- [GitHub Actions Documentation](https://docs.github.com/en/actions)",
        "- [Awesome Actions (community list)](https://github.com/sdras/awesome-actions)",
        "",
        "---",
        "GitHub Actions helps you automate and improve your development workflow, right where your code lives.",
    ]
    return "\n".join(guide_lines)


def save_guide_to_file(filename: str) -> None:
    """
    Saves the GitHub Actions guide to a file.

    Args:
        filename (str): The path to the file where the guide will be saved.
    """
    guide = get_github_actions_guide()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(guide)


def _test_get_github_actions_guide() -> None:
    """
    Simple test to verify the guide contains key sections.
    """
    guide = get_github_actions_guide()
    assert "What is GitHub Actions?" in guide
    assert "How Does It Work?" in guide
    assert "Example: Simple Workflow" in guide
    assert "Why Use GitHub Actions?" in guide
    assert "GitHub Actions Documentation" in guide
    print("All tests passed.")


if __name__ == "__main__":
    # Run tests
    _test_get_github_actions_guide()
    # Optionally save the guide to a file
    save_guide_to_file("GitHub_Actions_Plain_English_Guide.md")