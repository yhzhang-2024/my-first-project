s6 = "apple, banana, orange, grape"
lst6 = s6.split(",")
new_lst6 = [item.strip() for item in lst6]
out6 = "|".join(new_lst6)
print(out6)