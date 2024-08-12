from openai import OpenAI

client = OpenAI(
    api_key="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"
)


completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)