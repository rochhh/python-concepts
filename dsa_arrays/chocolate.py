def solution(packets, students):
    sorted_packets = sorted(packets)
    i = 0
    j = i + students - 1
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



packets = [3, 4, 1, 9, 56, 7, 9, 12] 
students = 5

print(solution(packets,students)) 