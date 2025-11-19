import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "hey there, I am Ajinkya"

tokens = enc.encode(text)

print(tokens)
# [48467, 1354, 11, 357, 939, 28294, 881, 2090]

decodes = enc.decode([48467, 1354, 11, 357, 939, 28294, 881, 2090])

print(decodes)