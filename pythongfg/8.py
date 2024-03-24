#Sort a tuple by its float element

"""Input : tuple = [('lucky', '18.265'), ('nikhil', '14.107'), 
                  ('akash', '24.541'), ('anand', '4.256'), ('gaurav', '10.365')]
Output : [('akash', '24.541'), ('lucky', '18.265'), 
          ('nikhil', '14.107'), ('gaurav', '10.365'), ('anand', '4.256')]"""
def sorted(tup):
    tup.sort(key=lambda x:float(x[1]),reverse=True)#lambda is used as anonymous functions
    print(tup)
tuple = [('lucky', '18.265'), ('nikhil', '14.107'),('akash', '24.541'), ('anand', '4.256'), ('gaurav', '10.365')]
sorted(tuple)

# Accessing nth element from tuples in list
list_of_tuples=[(1,"Yo",2),(3,"here",4),(5,"we are",6),(7,"learning python",8)]
n=int(input("specify index to be accessed\n"))
for t in list_of_tuples:
    print(t[n])