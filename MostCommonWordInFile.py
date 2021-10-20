while True:
  name = input('Enter file:\n')
  handle = open(name)

  counts = dict()
  for line in handle:
    words = line.split()
    for word in words:
      counts[word] = counts.get(word, 0) + 1

  bigcount = None
  bigword = None
  for word,count in counts.items():
    if bigcount is None or count > bigcount:
      bigword = word
      bigcount = count

  print(bigword,'is the most common word and it was reapeatedly used a whole', bigcount,'times.\n')