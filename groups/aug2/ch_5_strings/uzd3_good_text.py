# 2. uzdevums (teksta pārveidošana) 1. versija
 
user_text = input("Ievadi tekstu: ")
 
# Print user's original text
print("Tavs oriģinālais teksts:", user_text)
 
# Find all occurrences of phrases to modify and replace them
# start_index = 0
# while start_index < len(user_text):
#     start_nav = user_text.find("nav", start_index)
#     if start_nav == -1:
#         break
    
#     end_slikts = user_text.find("slikts", start_nav)
#     end_slikta = user_text.find("slikta", start_nav)
    
#     if end_slikts == -1 and end_slikta == -1:
#         break
    
#     if end_slikts == -1:
#         end_slikts = len(user_text)
#     if end_slikta == -1:
#         end_slikta = len(user_text)
    
#     if end_slikts < end_slikta:
#         end_phrase = end_slikts + len("slikts")
#         phrase_to_modify = user_text[start_nav:end_phrase]
#         user_text = user_text.replace(phrase_to_modify, "ir labs", 1)
#     else:
#         end_phrase = end_slikta + len("slikta")
#         phrase_to_modify = user_text[start_nav:end_phrase]
#         user_text = user_text.replace(phrase_to_modify, "ir laba", 1)
    
#     start_index = end_phrase
 
# # Print modified text
# print("Labotais teksts:", user_text)

# 2nd version
needle_nav = "nav"
needle_slikt = "slikt" # we will use this to find both slikts and slikta, and sliktie

nav_index = user_text.find(needle_nav)
slikt_index = user_text.find(needle_slikt)

corrected_text = user_text # we need some default value, else we would get error if nothing to correct
if nav_index != -1 and slikt_index != -1 and nav_index < slikt_index:
    corrected_text = user_text[:nav_index] + "ir lab" + user_text[slikt_index + len(needle_slikt):]
    # idea is we replace text from nav_index to nav_index + len(needle_nav) with "ir labs"
    # this means also removing some text

print("Labotais teksts:", corrected_text)