

def opener(file):
    with open(file,'r') as f:
        text = f.read()
        word_list = text.split()
    return word_list

def main():
    word_list = opener('alice_words.txt')
    
    word_counter = {}

    for word in word_list:
        word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
        word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", " ")
        word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
        word = word.replace(']', '').replace(';', '').replace(' ','')
        word = word.lower()

        if word in word_counter:
            word_counter[word]+=1
        else:
            word_counter[word]=1
    keys = word_counter.keys()
    sorted_keys = sorted(keys)
    with open('alice_words_final.txt','w') as f:
        f.write(f'Word\tCount\n')
        for word in sorted_keys:
            f.write(f'{word}\t{word_counter[word]}\n')

    hello = sorted_keys[0]
    for word in sorted_keys:
        if len(word)>len(hello):
            hello=word
    print(f'longest word: {hello}, with {len(hello)} characters.')
            

if __name__=='__main__':
    main()