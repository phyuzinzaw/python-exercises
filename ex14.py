from sys import argv

script,name=argv
prompt='>'
print(f"hi {name}, i'm the {script} script.")
print("i'd like to ask you a few questions.")
print(f"do you like me{name}?")
likes=input(prompt)
print(f"where do you live {name}?")
lives=input(prompt)
print(f"what kind of ocmpuer do you have?")
computer=input(prompt)
print(f"""
        alright, so you said {likes} about liking me.
        you live in{lives} . not sure where that is.
        and you have a {computer}computer.Nice.
        """)

