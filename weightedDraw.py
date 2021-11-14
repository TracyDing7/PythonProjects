from numpy.random import choice

samplelist = [ 1, 2, 3, 4, 10]
randomNumberList = choice( samplelist, 1, p=[0.05,0.1,0.15,0.2,0.5])
print(randomNumberList)