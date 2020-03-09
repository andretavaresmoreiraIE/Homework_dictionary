import Dictionary

print (Dictionary.d)

text = "I see one cat do Coding meanwhile a student was struggling to write hello world . Bogdan was saying it's easy guys"
translate = ""
words = text.split()
for w in words:
    translate = translate + " " + Dictionary.d[w]

print(translate)