h_1, m_1 = int(input()), int(input())
h_2, m_2 = int(input()), int(input())

minutes_start, minutes_end = h_1 * 60 + m_1, h_2 * 60 + m_2

for time_in_minutes in range(minutes_start, minutes_end + 1):
    hours, minutes = time_in_minutes // 60, time_in_minutes % 60
    if hours < 10:
        print(0, end="")
    print(hours, end=":")
    if minutes < 10:
        print(0, end="")
    print(minutes)
