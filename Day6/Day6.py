banks = [4, 10, 4, 1, 8, 4, 9, 14, 5, 1, 14, 15, 0, 15, 3, 5]
# banks = [0, 2, 7, 0]
prev_states = []
def next_states(state):
    mx = max(state)
    ind = state.index(mx)
    state[ind] = 0
    for i in range(1, mx+1):
        state[(ind+i)%len(state)] += 1
    return state
def run(banks):
    cycles = 0
    while banks not in prev_states:
        prev_states.append(banks.copy())
        banks = next_states(banks)
        cycles += 1
    print(cycles) #pt2
    print(cycles - prev_states.index(banks)) #pt2
    

run(banks.copy())



