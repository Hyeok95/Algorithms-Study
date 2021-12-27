def solution(s):
    answer = []
    nums = {0: "zero",
            1:	"one",
            2:	"two",
            3:	"three",
            4:	"four",
            5:	"five",
            6:	"six",
            7:	"seven",
            8:  "eight",
            9:	"nine"}
    for i in range(10):
        s = s.replace(nums[i], str(i))
    return int(s)


print(solution("one4seveneight"))