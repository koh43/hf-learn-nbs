from huggingface_hub import InferenceClient

# Use base_url only for chat completion (which works perfectly)
client = InferenceClient(
    base_url="http://localhost:8080",
    token="sk-no-key-required",
)

print("=== Chat Completion (with system prompt) ===")
try:
    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a story"},
        ],
        max_tokens=100,
        temperature=0.7,
        top_p=0.95,
    )
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*50 + "\n")

print("=== Chat Completion (user only - simulates text generation) ===")
try:
    response = client.chat_completion(
        messages=[
            {"role": "user", "content": "Tell me a story about a magical forest"},
        ],
        max_tokens=100,
        temperature=0.7,
        top_p=0.95,
    )
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*50 + "\n")

print("=== Chat Completion (creative writing prompt) ===")
try:
    response = client.chat_completion(
        messages=[
            {"role": "system", "content": "You are a creative storyteller."},
            {"role": "user", "content": "Write a short story about time travel"},
        ],
        max_tokens=100,
        temperature=0.8,
        top_p=0.95,
    )
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")