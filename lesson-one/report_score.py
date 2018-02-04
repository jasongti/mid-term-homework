
def calculate_total_score(score_list):
    total_score = 0
    for s in score_list:
        total_score += int(s)
    return total_score


def calculate_average_score(score_list):
    average_score = calculate_total_score(score_list) / len(score_list)
    return str(round(average_score, 2))


if __name__ == '__main__':
    original_scores = []
    final_title = []
    with open('report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        final_title = lines[0:1][0].split()
        original_scores = lines[1:]
    computed_scores = []
    for line in original_scores:
        scores = line.split()
        average = calculate_average_score(scores[1:])
        total = calculate_total_score(scores[1:])

        scores.append(average)
        scores.append(total)
        computed_scores.append(scores)
    computed_scores = sorted(computed_scores, key=lambda x: x[-1], reverse=True)
    [scores.insert(1, index + 1) for index, scores in enumerate(computed_scores)]
    final_title.insert(1, '名次')
    final_title.append('平均分')
    final_title.append('总分')

    subject_average_scores = ['平均', ' ']
    score_list_len = len(computed_scores)
    for i in range(2, len(final_title) - 2):
        score_sum = float(0)

        def subject_score_sum(score, score_list):
            return score + float(score_list[i])

        for scores in computed_scores:
            score_sum = subject_score_sum(score_sum, scores)
        score_avg = round(score_sum / score_list_len, 2)
        subject_average_scores.append(score_avg)

    with open('answer_report.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(final_title))
        f.write('\n')
        for sources in computed_scores:
            f.write(' '.join([str(c) for c in sources]))
            f.write('\n')
        f.write(' '.join([str(c) for c in subject_average_scores]))
