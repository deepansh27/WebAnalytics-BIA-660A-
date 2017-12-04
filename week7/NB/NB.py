"""
A simple script that demonstrates how we classify textual data with sklearn.

"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


#read the reviews and their polarities from a given file
def loadData(fname):
    reviews=[]
    labels=[]
    f=open(fname,'r')
   
    for line in f:
        print(line)
        review=line.strip().split('\t')  
#        reviews.append(review.lower()) 
#        print(reviews)
        labels.append(int(rating))
#        print(labels)
    f.close()
    return reviews,labels

rev_train,labels_train=loadData('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660A/WebAnalytics-BIA-660A-/week7/NB/reviews_train.txt')
rev_test,labels_test=loadData('/Users/deepanshparab/Desktop/Fall-2017-Cources/BIA-660A/WebAnalytics-BIA-660A-/week7/NB/reviews_test.txt')



print(type(rev_train[0]))


#
##Build a counter based on the training dataset
#counter = CountVectorizer()
#counter.fit(rev_train)
#
#
#
#
##count the number of times each term appears in a document and transform each doc into a count vector
#counts_train = counter.transform(rev_train)#transform the training data
#counts_test = counter.transform(rev_test)#transform the testing data
#
#
##train classifier
#clf = MultinomialNB()
#
##train all classifier on the same datasets
#clf.fit(counts_train,labels_train)
#
##use hard voting to predict (majority voting)
#pred=clf.predict(counts_test)
#
##print accuracy
#print (accuracy_score(pred,labels_test))


