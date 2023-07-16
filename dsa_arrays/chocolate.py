def solution(packets, students):
    sorted_packets = sorted(packets)
    i = 0
    j =  i + students - 1
    min_diff_overall = 10000
    while j < len(sorted_packets):
        min_chocolates = sorted_packets[i]
        max_chocolates = sorted_packets[j]
        min_diff_until_now = max_chocolates - min_chocolates

        if min_diff_until_now < min_diff_overall:
            min_diff_overall = min_diff_until_now

        i+=1
        j+=1

    return min_diff_overall



packets = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50] 
students = 7

print(solution(packets,students)) 