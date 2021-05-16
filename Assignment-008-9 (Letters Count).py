text =input("Write a sentence please: ")
set_text = set(text)
dict_text = {}
for i in set_text:
  count_letter = text.count(i)
  dict_text[i] = count_letter
print(dict_text)
