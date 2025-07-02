import re

"""phone = "+91 987654321012"
pattern = r"^(\+91[-\s]?)?[0]?\d{10}$"

if re.match(pattern, phone):
    print("✅ Valid phone number")
else:
    print("❌ Invalid phone number")

tweet = "Loving the #Python and #AI revolution! #100DaysOfCode"
hashtags = re.findall(r"#\w+", tweet)
print("Hashtags:", hashtags)"""

sentence = "Alice went to Paris with John and met Mr. Smith."
capitalized_words = re.findall(r"\b[A-Z][a-z]*", sentence)
print("Capitalized Words:", capitalized_words)



