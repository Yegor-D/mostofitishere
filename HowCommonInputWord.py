while True:
  counts = dict()
  print('\nEnter a line of text:')
  line = input('')

  words = line.split()

  print('Words:', words)

  print('Counting...\n')
  for word in words:
    counts[word] = counts.get(word, 0) + 1
  print('Counts:', counts)