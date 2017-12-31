import re

def create_model1(trainX, trainY):
    # reformat text
    def reform(comment):
        spaced = re.sub('[^a-zA-Z]', ' ', comment)
        return spaced.split(' ')
    trainX['comment'].apply(reform)
    list_of_comments = trainX['comment'].tolist()
    vocabulary = [word for word in comment for comment in list_of_comments]
    for word in vocabulary:
        trainX[word] = trainX['comment'].apply(lambda x: x.count(word))
    print trainX