from textblob import TextBlob

print("=" * 40)
print("      SENTIMENT ANALYSIS CHATBOT")
print("=" * 40)
print("Type a message to analyze its sentiment.")
print("Type 'exit' to quit.\n")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if not message.strip():
        print("Bot: Please type a message.\n")
        continue

    analysis = TextBlob(message)
    score = analysis.sentiment.polarity

    if score > 0:
        sentiment = "Positive 😊"
    elif score < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    print(f"Bot: Sentiment: {sentiment}")
    print(f"     Polarity score: {score:.2f}\n")
