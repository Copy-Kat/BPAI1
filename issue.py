with open('compare.txt') as f:
    lines = f.readlines()
    
knobs = []
for idx, line in enumerate(lines):
    if 'knob' in line:
        knobs.append(idx)
        
filtered = []
        
for idx, line in enumerate(lines):
    if idx not in knobs:
        print(line)
        q = input('issue: (y for not in dict, m for multiple ingredients, o)')
        filtered.append(input)
    else:
        filtered.append(knobs[idx])