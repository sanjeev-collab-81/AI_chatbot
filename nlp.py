import re


# These common words add little meaning to many searches. Keep "not" out so
# that important meanings such as "is not" are preserved.
STOP_WORDS = {
	"a", "an", "and", "are", "can", "could", "did", "do", "does",
	"for", "in", "is", "of", "on", "please", "the", "to", "was",
	"were", "what", "which", "who", "would",
}


def preprocess_text(text: str) -> str:
	"""Lowercase text and normalize punctuation and whitespace."""
	text = text.lower()
	# Replace punctuation with spaces so separate words stay separate.
	text = re.sub(r"[^\w\s]", " ", text)
	# Turn repeated spaces, tabs, and newlines into single spaces.
	return re.sub(r"\s+", " ", text).strip()


def tokenize_text(text: str) -> list[str]:
	"""Return the cleaned text as a list of words."""
	return preprocess_text(text).split()


def remove_stopwords(tokens: list[str]) -> list[str]:
	"""Return tokens after removing common words with little search value."""
	return [token for token in tokens if token not in STOP_WORDS]
