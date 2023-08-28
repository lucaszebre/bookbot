




with open('./books/frankenstein.txt') as f:
    file_contents = f.read()

    # print(file_contents)
    words=file_contents.split()
    print(len(words))

    dict = {}
    for a in words:
        for i in a.lower():
            if dict[i]==0 :
                dict[i]=1
            else:
                dict[i]=dict[i]+1
    print(dict)

def count_word(text):
    print(len(text.split()))

def count_letter(text):
    dict={}
    for a in text:
        for b in a:
            lowered = b.lower()
            if lowered in dict:
                dict[lowered]+=1
            else:
                dict[lowered]=1
    print(dict)
    return dict

