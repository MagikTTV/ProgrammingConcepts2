"""
Spam email scanner with keyword scoring.

Program asks the user to enter an email message, scans it for common spam
keywords/phrases, and assigns a point based on how many times the terms used. Tally and rates
potential spam based on number of points received.
"""


def build_spam_terms() -> List[str]:
    """Return a list of 30 common spam words and phrases."""
    return [
        "act now",
        "urgent",
        "limited time",
        "offer expires",
        "last chance",
        "risk-free",
        "no hidden fees",
        "free money",
        "cash bonus",
        "get paid",
        "earn extra cash",
        "make money",
        "work from home",
        "financial freedom",
        "pre-approved loan",
        "consolidate your debt",
        "unclaimed funds",
        "you've won",
        "winner",
        "claim your prize",
        "congratulations",
        "exclusive offer",
        "free gift",
        "100% free",
        "guaranteed",
        "click here",
        "verify your account",
        "password expires",
        "unusual activity",
        "update now",
    ]


def count_term_occurrences(message: str, term: str) -> int:
    """Count occurrences of a term in a message.
    """
    if " " not in term:
        pattern = rf"\b{re.escape(term)}\b"
        return len(re.findall(pattern, message))

    pattern = rf"(?={re.escape(term)})"
    return len(re.findall(pattern, message))


def analyze_message_for_spam(
        message: str, terms: List[str]
) -> Tuple[int, Dict[str, int], str]:
    """Analyze message and return spam score, matched terms, and rating."""
    matched: Dict[str, int] = {}
    score = 0

    for term in terms:
        occurrences = count_term_occurrences(message, term)
        if occurrences > 0:
            matched[term] = occurrences
            score += occurrences

    rating = rate_spam_likelihood(score)
    return score, matched, rating


def rate_spam_likelihood(score: int) -> str:
    """Convert spam score to likelihood rating."""
    if score == 0:
        return "Very unlikely to be spam."
    if 1 <= score <= 2:
        return "Unlikely to be spam."
    if 3 <= score <= 6:
        return "Possibly spam."
    if 7 <= score <= 11:
        return "Likely spam."
    return "Very likely spam."


def format_matched_terms(matched: Dict[str, int]) -> str:
    """Format matched terms for display."""
    if not matched:
        return "None"

    sorted_items = sorted(matched.items(), key=lambda item: (-item[1], item[0]))
    lines = [f"- {term} ({count})" for term, count in sorted_items]
    return "\n".join(lines)


def main() -> None:
    """Run the spam scanner application."""
    print("Spam Scanner (Case-Sensitive Version)")
    print("Enter your email message below. Press Enter on a blank line to finish.\n")

    lines: List[str] = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    message = "\n".join(lines).strip()

    if not message:
        print("\nNo message entered. Please run the program again.")
        return

    terms = build_spam_terms()
    score, matched, rating = analyze_message_for_spam(message, terms)

    print("\nResults")
    print("-" * 60)
    print(f"Spam score: {score}")
    print(f"Likelihood: {rating}")
    print("\nWords/phrases that increased the score:")
    print(format_matched_terms(matched))


if __name__ == "__main__":
    main()
