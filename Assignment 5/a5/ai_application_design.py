def sentiment_score(text):
    text = text.lower()
    pos = {'good': 1, 'clean': 1, 'excellent': 2}
    neg = {'bad': -1, 'smell': -1, 'awful': -2}
    words = text.split()
    score = 0
    for i, word in enumerate(words):
        if word in pos:
            score += pos[word]
        elif word in neg:
            score += neg[word]
        if i > 0 and words[i-1] in {'not', 'never'}:
            score *= -1
    return score

for sample in ['good air quality', 'not bad air quality', 'awful smell', 'excellent and clean']:
    print(sample, '->', sentiment_score(sample))
print('A simple lexicon based scorer is explainable and easy to debug, but a trained model is better for subtle sentiment and sarcasm.')
