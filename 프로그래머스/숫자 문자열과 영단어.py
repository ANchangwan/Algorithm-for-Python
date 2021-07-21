# 1
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

#2
keys = ["zero","one","two","three","four","five","six","seven","eight","nine"]
values = [str(i) for i in range(10)]
number_dict = dict(zip(keys, values))

def solution(s):
    word = ""
    answer
    for st in s:
        if st.isdigit():
            answer += st
        else:
            word += st
            if word in keys:
                answer += number_dict[word]
                word = ""

    return int(answer)

