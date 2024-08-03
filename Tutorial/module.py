import pyjokes

# print("Printing Jokes...") // comment
# joke = pyjokes.get_joke()
# print(joke)

# this is a single line comment
'''
this is a multi line comment
'''


def myfunc():
    joke = pyjokes.get_joke()
    print(joke)

if __name__ == "__main__":
    print("we are directly running this code")
    myfunc()
    print(__name__)