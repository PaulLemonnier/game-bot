import json
import unicodedata

def save_json(data: dict, filename: str) -> None:
    """Save data to a JSON file"""
    with open(f"src/data/moves/{filename}", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def load_json(filename: str) -> dict:
    """Load data from a JSON file"""
    with open(f"src/data/moves/{filename}", "r") as f:
        data = json.load(f)
    print(f"Data loaded from {filename}")
    return data

def search_word_in_list(search_word: str, words_list: list[str]) -> bool:
    """Check whether a word contains the search string, ignoring case and accents.

    Args:
        search_word: Substring to search for.
        words_list: Words to inspect.

    Returns:
        True if at least one word contains the normalized search string,
        otherwise False.
    """
    def normalize(text: str) -> str:
        decomposed_text = unicodedata.normalize("NFKD", text)
        return "".join(
            character
            for character in decomposed_text
            if not unicodedata.combining(character)
        ).casefold()

    normalized_search_word = normalize(search_word)
    return any(normalized_search_word in normalize(word) for word in words_list)