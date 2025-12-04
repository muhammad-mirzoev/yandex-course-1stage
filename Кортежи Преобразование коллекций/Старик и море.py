n = int(input())
waves = []

for i in range(n):
    *wave_name, excitement = input().split()
    wave_name = ' '.join(wave_name)
    excitement = int(excitement)
    waves.append((wave_name, excitement))

for i in range(n - 1):
    wave, excitement = waves[i]
    next_wave, next_excitement = waves[i + 1]

    if excitement < next_excitement:
        print(f"({i + 1}, '{wave}')")
