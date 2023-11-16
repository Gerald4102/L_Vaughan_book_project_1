def main():

    vowels = ('a', 'e', 'i', 'o', 'u')
    translation = ''

    phrase = input("Enter a phrase: ")

    phrase_list = phrase.split(' ')

    for word in phrase_list:
        if word[0] in vowels:
            translation += word + 'way '
        else:
            translation += word[1:] + word[0] + 'ay '

    return translation

if __name__ == "__main__":

    print(main())