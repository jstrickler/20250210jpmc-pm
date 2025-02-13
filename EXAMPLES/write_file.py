
states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt", "w") as states_file: # "w" opens for writing, "a" for append
    for state_to_write in states:
        states_file.write(state_to_write + "\n")  # write() does not automatically add newline
