import datetime

TIME_FORMAT = '%d.%m.%Y %H:%M'
akk_size_km = int(input())
charge_time_min = int(input())
v_km_per_h = int(input())
start_date_time_str = input()
start_date_time = datetime.datetime.strptime(start_date_time_str, TIME_FORMAT)
*distances_km, = map(int, input().split())
distances_km.insert(0, 0)
akk_cur_size_km = akk_size_km
charge_indexes = [0]
for i in range(len(distances_km) - 1):
    delta_km = distances_km[i + 1] - distances_km[i]
    if akk_cur_size_km < delta_km:
        akk_cur_size_km = akk_size_km
        charge_indexes.append(i)
    akk_cur_size_km -= delta_km

d = {}
cur_t = start_date_time
for i in range(1, len(charge_indexes)):
    ind = charge_indexes[i - 1]
    next_ind = charge_indexes[i]
    dist_km = distances_km[next_ind] - distances_km[ind]
    delta_min = dist_km / v_km_per_h * 60
    if i > 1:
        delta_min += charge_time_min
    t_delta = datetime.timedelta(minutes=delta_min)
    cur_t += t_delta
    d[next_ind] = cur_t
for k, v in d.items():
    print(f'{k} {v.strftime(TIME_FORMAT)}')
