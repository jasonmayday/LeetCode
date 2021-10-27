paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
for c in "!?',;.":
    paragraph = paragraph.replace(c, " ")

print(paragraph)