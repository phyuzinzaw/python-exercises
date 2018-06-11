people =30
cars=40
trucks=15
if cars > people:
    print ("we should take the cars.")
elif cars < people:
    print("we should not take the cars.")
if trucks > cars:
    print("that's too many trunks.")
elif trucks < cars:
    print("maybe we could take the trunks.")
else:
    print("we still can't decide.")
if people > trucks:
    print("alright, let's just take the trunks.")
else:
    print("fine, let's stay home then.")

