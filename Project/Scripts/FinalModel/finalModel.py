from tipGenerator import Tips

dirpath = '/Users/deepanshparab/Desktop/Projects/Bia-660/Project/ExtractedReviews/'
filename = '3.DilliJunction.txt'
path = dirpath + filename

tip = Tips(path, filename)  # creating instance of class Tips

tip.model(path, filename)  # calling the run method to run the code

