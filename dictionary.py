import wordle_game

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

english_words = load_words()
sized_words = sorted(list(filter(lambda w: len(w)==wordle_game.num_letters, english_words)))    
