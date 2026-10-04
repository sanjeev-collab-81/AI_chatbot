import gradio as gr

from chatbot import TraditionalAIChatbot


chatbot_engine = TraditionalAIChatbot()


def respond(message: str, history: list[dict]) -> tuple[list[dict], str]:
	"""Add the user's message and the chatbot's reply to the conversation."""
	if not message or not message.strip():
		return history or [], ""

	updated_history = history or []
	updated_history = updated_history + [
		{"role": "user", "content": message},
		{"role": "assistant", "content": chatbot_engine.get_response(message)},
	]
	return updated_history, ""


with gr.Blocks(title="Traditional AI Rule-Based Chatbot") as demo:
	gr.Markdown("# Traditional AI Rule-Based Chatbot")
	gr.Markdown(
		"Ask beginner-friendly questions about AI, programming, and computer "
		"science. Answers come from local rules and classical text similarity."
	)

	chat_window = gr.Chatbot(height=440, show_label=False)
	message_input = gr.Textbox(
		placeholder="Ask a computer science question...",
		show_label=False,
		lines=1,
		max_lines=3,
	)

	with gr.Row():
		send_button = gr.Button("Send", variant="primary")
		clear_button = gr.Button("Clear")

	gr.Examples(
		examples=[
			"What is artificial intelligence?",
			"Explain a rule-based system",
			"What is a Python dictionary?",
			"How should I prepare for a viva?",
		],
		inputs=message_input,
		label="Example questions",
	)

	send_button.click(
		fn=respond,
		inputs=[message_input, chat_window],
		outputs=[chat_window, message_input],
	)
	message_input.submit(
		fn=respond,
		inputs=[message_input, chat_window],
		outputs=[chat_window, message_input],
	)
	clear_button.click(
		fn=lambda: ([], ""),
		outputs=[chat_window, message_input],
	)


if __name__ == "__main__":
	demo.launch(theme=gr.themes.Soft(primary_hue="teal", secondary_hue="orange"))
