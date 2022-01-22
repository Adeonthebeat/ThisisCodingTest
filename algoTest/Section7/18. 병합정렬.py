# 병합정렬

def Dsort(lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2
        Dsort(lt, mid)
        Dsort(mid + 1, rt)

        # 병합 해주기
        p1 = lt
        p2 = mid + 1
        temp = []
        while p1 <= mid and p2 <= rt:
            if arr[p1] < arr[p2]:
                temp.append(arr[p1])
                p1 += 1
            else:
                temp.append(arr[p2])
                p2 += 1

        if p1 <= mid:
            temp = temp + arr[p1:mid + 1]

        if p2 <= rt:
            temp = temp + arr[p2:rt + 1]

        for i in range(len(temp)):
            arr[lt + i] = temp[i]  # 마지막으로 합병


if __name__ == "__main__":
    arr = [23, 11, 45, 36, 15, 67, 33, 21]
    print("Before Sort : ", end=" ")
    print(arr)
    Dsort(0, 7)
    print()
    print("After Sort : ", end=" ")
    print(arr)
