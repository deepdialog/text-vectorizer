
from text_vectorizer import TextVectorizer

if __name__ == '__main__':
    docs = [
        'I love you',
        'I hate you very much',
        'I need you',
    ]
    tv = TextVectorizer()
    tv.fit(docs)
    embs = tv.transform(docs)
    print(embs)
    iembs = tv.inverse_transform(embs)
    print(iembs)

    tv = TextVectorizer(verbose=1, max_len=5)
    tv.fit(docs)
    embs = tv.transform(docs)
    print(embs)
    iembs = tv.inverse_transform(embs)
    print(iembs)

    tv = TextVectorizer(verbose=1, max_len=5, max_features=2)
    tv.fit(docs)

    for i, x in enumerate(tv.transform_generator(docs, batch_size=2)):
        print(x)
        if i >= 2:
            break
