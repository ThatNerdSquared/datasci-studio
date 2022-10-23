distances_sum = 0
crests = [0.1666, 0.7083, 1.271, 1.813, 2.375, 2.938, 3.469, 4.042, 4.604, 5.146]

for idx, crest in enumerate(crests):
    if idx == 0:
        continue
    try:
        distance = crest - crests[idx-1]
        distances_sum += distance
    except IndexError:
        pass

print(distances_sum)
final_total = (distances_sum / 9)
print(final_total)
