import dictionary
import wordle_game

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

class solver:
    def __init__(self):
        self.words = dictionary.sized_words.copy()
        self.map_letters()
        self.best = self.pick_word()

    def map_letters(self):
        self.letter_map = {c:0 for c in char_range('a', 'z')}
        for word in self.words:
            for c in word:
                self.letter_map[c] += 1
    
    def filter_words(self, res, test):
        remove_filter = []
        existense_filter = []
        positional_filter = []
        for i, e in enumerate(test):
            if res[i]==0:
                remove_filter.append(e)
            elif res[i]==1:
                existense_filter.append((i, e))
            elif res[i]==2:
                positional_filter.append((i, e))
        
        # remove words that does have the letter that the pick does not have
        def rem_filter(match_list, word):
            for c in match_list:
                if c in word:
                    return False
            return True
        
        # remove words that does not have the letter that the pick do have
        # unless it in the correct position
        def exist_filter(match_list, word):
            for i, c in match_list:
                if c not in word:
                    return False
                elif c == word[i]:
                    return False
            return True

        # remove words that does not have the letter that the pick do have
        # in the same spot
        def posit_filter(match_list, word):
            for i, c in match_list:
                if c != word[i]:
                    return False
            return True

        self.words = list(filter(lambda k: rem_filter(remove_filter, k), self.words))
        self.words = list(filter(lambda k: exist_filter(existense_filter, k), self.words))
        self.words = list(filter(lambda k: posit_filter(positional_filter, k), self.words))

    def pick_word(self):
        word_map = {}
        for w in self.words:
            word_map[w] = 0
            for c in set(w):
                word_map[w] += self.letter_map[c]
        
        word_map = list(word_map.items())
        r = sorted(word_map, key=lambda k: k[1], reverse=True)[0][0]
        return r

if __name__ == "__main__":
    solver = solver()
    solver.filter_words([], '')
    game = wordle_game.wordle()
    game.play(solver.filter_words, solver.pick_word)
