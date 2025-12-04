def translate(text):
    global translated_text
    letters = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    punct = ",.-"
    result = []
    filtered_text = ''.join(i for i in text if i not in punct)
    words = filtered_text.split()
    for word in words:
        translated_word = ''.join(i for i in word if i not in letters)
        if translated_word:
            result.append(translated_word)

    translated_text = ' '.join(result)