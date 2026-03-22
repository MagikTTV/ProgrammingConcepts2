"""Paragraph Sentence Counter

Allow a user to enter a paragraph, display each individual sentence,
and display the total number of sentences found in the paragraph.
The program accepts sentences that begin with words or numbers.
"""

from __future__ import annotations

import re


SENTENCE_END_PATTERN = re.compile(
    r"(?<=[.!?])\s+(?=(?:['\"“”‘’\(\[])*[A-Z0-9])"
)


def get_paragraph() -> str:
    """Collect a paragraph from the user.

    Parameters:
        None.

    Variables:
        lines (list[str]): Stores each line typed by the user.
        line (str): One line of user input.

    Steps:
        1. Explain how the user should enter the paragraph.
        2. Accept one or more lines of text.
        3. Stop when the user presses Enter on a blank line.
        4. Join the lines into one paragraph string.

    Returns:
        str: The completed paragraph entered by the user.
    """
    lines: list[str] = []

    print("Enter your paragraph below.")
    print("Press Enter on a blank line when you are finished.\n")

    while True:
        line = input()

        if line == "":
            if lines:
                break

            print("Please enter at least one sentence before finishing.")
            continue

        lines.append(line.strip())

    return " ".join(lines)


def split_into_sentences(paragraph: str) -> list[str]:
    """Split a paragraph into individual sentences.

    Parameters:
        paragraph (str): The paragraph entered by the user.

    Variables:
        cleaned_paragraph (str): Paragraph with extra whitespace removed.
        pieces (list[str]): Rough sentence pieces from the split operation.
        sentences (list[str]): Final cleaned list of sentences.

    Steps:
        1. Normalize repeated whitespace inside the paragraph.
        2. Split after sentence-ending punctuation.
        3. Allow the next sentence to begin with a letter or a number.
        4. Remove empty results and trim extra spaces.

    Returns:
        list[str]: A list containing each sentence found in the paragraph.
    """
    cleaned_paragraph = re.sub(r"\s+", " ", paragraph).strip()

    if not cleaned_paragraph:
        return []

    pieces = SENTENCE_END_PATTERN.split(cleaned_paragraph)
    sentences = [piece.strip() for piece in pieces if piece.strip()]

    return sentences


def display_sentences(sentences: list[str]) -> None:
    """Display each sentence and the total count.

    Parameters:
        sentences (list[str]): The list of extracted sentences.

    Variables:
        index (int): Position number for each sentence.
        sentence (str): The current sentence being displayed.

    Steps:
        1. Print a heading for the results.
        2. Display each sentence on its own numbered line.
        3. Print the total number of sentences.

    Returns:
        None.
    """
    print("\nIndividual sentences:")

    for index, sentence in enumerate(sentences, start=1):
        print(f"{index}. {sentence}")

    print(f"\nSentence count: {len(sentences)}")


def main() -> None:
    """Run the paragraph sentence counter program.

    Parameters:
        None.

    Variables:
        paragraph (str): User-entered paragraph.
        sentences (list[str]): Sentences extracted from the paragraph.

    Steps:
        1. Get the paragraph from the user.
        2. Split the paragraph into sentences.
        3. Display each sentence and the count.

    Returns:
        None.
    """
    paragraph = get_paragraph()
    sentences = split_into_sentences(paragraph)
    display_sentences(sentences)


if __name__ == "__main__":
    main()
