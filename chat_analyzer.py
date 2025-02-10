import string
from collections import Counter

# Function to read and parse chat logs
def parse_chat_log(filename):
    messages = []
    try:
        with open(filename, "r") as file:
            for line in file:
                if ": " in line:
                    sender, message = line.strip().split(": ", 1)
                    messages.append((sender, message))
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    return messages

# Function to count messages per user
def count_messages_per_user(messages):
    user_counts = {}
    for sender, _ in messages:
        user_counts[sender] = user_counts.get(sender, 0) + 1
    return user_counts

# Function to calculate average message length
def calculate_average_message_length(messages):
    total_length = sum(len(message) for _, message in messages)
    return total_length / len(messages) if messages else 0

# Function to find the most common words
def find_common_words(messages, top_n=5):
    all_words = []
    for _, message in messages:
        words = message.translate(str.maketrans("", "", string.punctuation)).lower().split()
        all_words.extend(words)
    return Counter(all_words).most_common(top_n)

# Main script
def analyze_chat_logs(filenames):
    all_messages = []
    for filename in filenames:
        all_messages.extend(parse_chat_log(filename))
    
    user_message_counts = count_messages_per_user(all_messages)
    avg_length = calculate_average_message_length(all_messages)
    common_words = find_common_words(all_messages)

    print("\n--- Chat Log Analysis ---")
    print("Messages per User:")
    for user, count in user_message_counts.items():
        print(f"{user}: {count} messages")

    print(f"\nAverage message length: {avg_length:.2f} characters")
    
    print("\nMost Common Words:")
    for word, count in common_words:
        print(f"{word}: {count} times")

# Example usage
filenames = ["chat_log_1.txt"]  # Add multiple filenames if needed
analyze_chat_logs(filenames)
