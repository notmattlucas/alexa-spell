import logging
import sys
import words
import names
from flask import Flask
from flask_ask import Ask, question, session, statement

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
ch.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)

root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(ch)

logger = logging.getLogger("alexa-spell")
logger.setLevel(logging.DEBUG)
logger.info("Init ...")

app = Flask(__name__)
ask = Ask(app, "/")

test_set = words.gen()
name_set = names.gen()

@ask.launch
def new_spelling_test():
    word = next(test_set)
    session.attributes['word'] = word
    logger.info("Chosen word: %s", word)
    return question("How do you spell, %s?" % word)

@ask.intent("AnswerIntent")
def answer(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth):
    letters = [first, second, third, fourth, fifth,sixth, seventh, eighth, ninth, tenth]
    letters = [letter for letter in letters if letter]
    actual = "".join(letters).replace(".", "").lower()
    expected = session.attributes['word']
    logger.info("Expected '%s', Actual '%s'", expected, actual)
    if actual in expected:
        return statement("Well done, you got it right! You %s" % next(name_set))
    else:
        return statement("Oh bobbins! You spelt %s, you're a %s" % (actual, next(name_set)))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)