SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my "

def main():
    adjective = input("Type an adjective: ")
    noun = input("Type a noun: ")
    verb = input("Type a verb: ")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + ".")
if __name__ == '__main__':
    main()