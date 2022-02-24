# import wikipedia

# wikipedia.set_lang('uz')

# print(wikipedia.search('Toshkent'))
# print(wikipedia.summary('Toshkent'))




# # python main.py


from uzwords import words
from difflib import get_close_matches


def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False #binday so'z mavjud emas
    
    if word in matches:
        available = True #mavjud
        matches = word
   
    elif 'h' in word:
        word = word. replace('h', 'x')
        matches.update(get_close_matches(word, words))
    elif 'x' in word:
        word = word. replace('x', 'h')
        matches.update(get_close_matches(word, words))
   
        
    return {'available': available, 'matches': matches}    
        
        
if __name__ == '__main__':
    print(checkWord("hato"))

    