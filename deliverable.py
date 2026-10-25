"""
Short Notes Template Module

This module provides a clean, production-ready template for creating short notes
in the Vault-of-Forbidden-Knowledge project.

Source: https://github.com/Huerte/Vault-of-Forbidden-Knowledge/issues/48
"""

from typing import List, Optional


class ShortNote:
    """
    Represents a short note with a title, optional tags, and content.

    Attributes:
        title (str): The title of the note.
        content (str): The main content of the note.
        tags (List[str]): Optional list of tags for categorization.
    """

    def __init__(self, title: str, content: str, tags: Optional[List[str]] = None) -> None:
        """
        Initialize a ShortNote instance.

        Args:
            title (str): The title of the note.
            content (str): The main content of the note.
            tags (Optional[List[str]]): Optional list of tags.
        """
        self.title: str = title
        self.content: str = content
        self.tags: List[str] = tags if tags is not None else []

    def to_markdown(self) -> str:
        """
        Render the note as a Markdown-formatted string.

        Returns:
            str: The note in Markdown format.
        """
        lines = [f"# {self.title}", ""]
        if self.tags:
            lines.append(f"**Tags:** {', '.join(self.tags)}")
            lines.append("")
        lines.append(self.content.strip())
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"ShortNote(title={self.title!r}, tags={self.tags!r})"


def short_note_template(
    title: str = "Short Note Title",
    content: str = "Write your concise note here.",
    tags: Optional[List[str]] = None
) -> ShortNote:
    """
    Factory function to create a ShortNote with default template values.

    Args:
        title (str): The title of the note.
        content (str): The main content of the note.
        tags (Optional[List[str]]): Optional list of tags.

    Returns:
        ShortNote: A new ShortNote instance.
    """
    return ShortNote(title=title, content=content, tags=tags)


# Example usage and tests
def _test_short_note_template() -> None:
    note = short_note_template(
        title="Python List Comprehensions",
        content="List comprehensions provide a concise way to create lists.",
        tags=["python", "syntax", "lists"]
    )
    expected_md = (
        "# Python List Comprehensions\n\n"
        "**Tags:** python, syntax, lists\n\n"
        "List comprehensions provide a concise way to create lists."
    )
    assert note.title == "Python List Comprehensions"
    assert note.tags == ["python", "syntax", "lists"]
    assert note.content == "List comprehensions provide a concise way to create lists."
    assert note.to_markdown() == expected_md

    # Test with default values
    default_note = short_note_template()
    assert default_note.title == "Short Note Title"
    assert default_note.tags == []
    assert default_note.content == "Write your concise note here."
    assert "# Short Note Title" in default_note.to_markdown()

if __name__ == "__main__":
    _test_short_note_template()