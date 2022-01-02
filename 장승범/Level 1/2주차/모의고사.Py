def solution(answers):

    supo1 = [1, 2, 3, 4, 5] * 5000
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5] * 5000
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 5000

    supo = [supo1, supo2, supo3]

    count = [0, 0, 0]

    for i in range(len(answers)):
        for j in range(len(supo)):
            if answers[i] == supo[j][i]:
                count[j] += 1

    result = []

    for i in range(len(supo)):
        if count[i] == max(count):
            result.append(i + 1)


    return result