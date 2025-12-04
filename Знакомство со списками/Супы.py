soups = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]

for i in range(int(input())):
    print(soups[i % 5])