text = input().strip()
words = text.split()

robot_voice_words = ['-'.join(word.upper()) for word in words]

print(' '.join(robot_voice_words))
