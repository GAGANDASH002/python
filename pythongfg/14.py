#Dictionary and counter in Python to find winner of election

from collections import Counter
#Counter-Elements are stored as dictionary keys and their counts are stored as dictionary values.
votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john'] 
 
vote_count=Counter(votes)

max_votes=max(vote_count.values())#values() is a method in the Counter class which returns the count of keys

list=[i for i in vote_count if vote_count[i]==max_votes]

print(sorted(list)[0])

#Key with maximum unique values

test_dict = {"Python": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}

max_val=0
max_key=None

for sub in test_dict:
    if len(set(test_dict.get(sub)))>max_val:
        max_val=len(set(test_dict.get(sub)))
        max_key=sub

print("key with maximum unique values is",max_key)
 