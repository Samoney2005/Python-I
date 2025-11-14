# Problem 1: Cast Vote
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

# Problem 2: Keys in Common



# Problem 3: Frequency Count
# Problem 4: Highest Priority Task
# Problem 5: Find Majority Element
# Problem 6: Has Duplicates
# Problem 7: Make Pairs
