test_list = ["effort", "circle", "yearly", "woolen", "accept", "lurker", "island", "faucet", "glossy", "evader"]

def is_abecedarian(input_word):
    index = 0
    for letter in input_word[0:-1]:
        if ord(input_word[index])> ord(input_word[index + 1]):
            return False
        else:
            index = index + 1
        return True
    
value_list =[]
for item in test_list:
    value = is_abecedarian(item)
    value_list.append(value)