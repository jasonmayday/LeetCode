

s = "A man, a plan, a canal: Panama"

sgood = "".join(ch.lower() for ch in s if ch.isalnum())

print (sgood)