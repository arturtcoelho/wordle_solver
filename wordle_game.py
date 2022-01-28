import dictionary
import random

num_letters=10
TURNS=8

class wordle:
    def __init__(self):
        self.KEY = dictionary.sized_words[random.randrange(0, len(dictionary.sized_words))]

    def test_word(self, test):
        res = [0 for _ in range(num_letters)]
        for i, c in enumerate(test):
            if c in self.KEY:
                res[i] += 1
            if c == self.KEY[i]:
                res[i] += 1
        
        status = len(list(filter(lambda k: k==2, res))) == num_letters

        return res, status

    def play(self, call_ret, call_resp):

        for _ in range(TURNS):
        
            pick = call_resp()
            print(pick)

            while len(pick) != num_letters or pick not in dictionary.sized_words:
                if len(pick) != num_letters:
                    print('Wrong word lenght')
                else:
                    print('word not in dictionary')
                pick = call_resp()
            
            resp, status = self.test_word(pick)

            print(resp)

            call_ret(resp, pick)

            if status:
                print('GAME WON!')
                print('You found the word', self.KEY)
                exit(0)

        print('You lose :(')
        print('KEY: ', self.KEY)

if __name__ == '__main__':
    pass
