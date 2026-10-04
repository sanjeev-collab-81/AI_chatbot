import re
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from nlp import preprocess_text, remove_stopwords, tokenize_text
from utils.helpers import load_json_file


class TraditionalAIChatbot:
	"""Answer questions with regex rules and TF-IDF similarity."""

	FALLBACK_RESPONSE = "Sorry, I don't understand that question yet."

	def __init__(
		self,
		knowledge_base_path: str | Path | None = None,
		similarity_threshold: float = 0.25,
	) -> None:
		self.similarity_threshold = similarity_threshold

		# Find the JSON file beside this Python file unless another path is given.
		if knowledge_base_path is None:
			knowledge_base_path = Path(__file__).with_name("knowledge_base.json")

		self.knowledge_base = load_json_file(knowledge_base_path)

		# Prepare the stored questions once so each new message can be compared quickly.
		self.search_questions = [
			self._prepare_for_similarity(entry["question"])
			for entry in self.knowledge_base
		]
		self.vectorizer = TfidfVectorizer()
		self.question_vectors = self.vectorizer.fit_transform(self.search_questions)

	@staticmethod
	def _prepare_for_similarity(text: str) -> str:
		"""Clean text and remove common words before comparing its meaning."""
		tokens = tokenize_text(text)
		return " ".join(remove_stopwords(tokens))

	def get_response(self, user_text: str) -> str:
		"""Return the first rule match, the closest similar answer, or a fallback."""
		cleaned_text = preprocess_text(user_text)
		if not cleaned_text:
			return self.FALLBACK_RESPONSE

		# Check the hand-written regex rules before using approximate matching.
		for entry in self.knowledge_base:
			for pattern in entry["patterns"]:
				if re.fullmatch(pattern, cleaned_text):
					return entry["response"]

		search_text = self._prepare_for_similarity(cleaned_text)
		if not search_text:
			return self.FALLBACK_RESPONSE

		user_vector = self.vectorizer.transform([search_text])
		scores = cosine_similarity(user_vector, self.question_vectors).flatten()
		best_index = int(scores.argmax())

		if scores[best_index] >= self.similarity_threshold:
			return self.knowledge_base[best_index]["response"]

		return self.FALLBACK_RESPONSE
