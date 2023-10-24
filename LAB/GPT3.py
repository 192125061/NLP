import openai

# Set your OpenAI API key
api_key = "YOUR_API_KEY"

# Your prompt for text generation
prompt = "Once upon a time,"

# Generate text using GPT-3
response = openai.Completion.create(
    engine="text-davinci-002",  # You can choose a different engine based on your needs
    prompt=prompt,
    max_tokens=50,  # Adjust the desired length of the generated text
    n = 1,  # Number of completions to generate
    stop=None  # You can specify an optional stop sequence
)

# Extract and print the generated text
generated_text = response.choices[0].text
print(generated_text)
