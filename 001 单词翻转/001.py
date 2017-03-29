#问题描述：单词翻转
#input:     "i am a student."
#output:    "student. a am i"
input_Str = "i am a sa student."

def reverse(Str):
    begin = 0
    end = len(Str)-1
    while(begin < end):
        if begin>0:
            Str = Str[:begin]+Str[end] + Str[begin+1:end] + Str[begin]+Str[end+1:]
        else:
            Str = Str[end] + Str[begin+1:end] + Str[begin]
        begin +=1
        end = end-1
    return Str

def handleStr(input):
    begin = 0
    end = 0
    next = 0
    while(next < len(input)):
        while next < len(input) and input[next] ==' ' :
              next +=1
        if next>=len(input):
           break;
        begin = next
        end = next
        while next < len(input) and input[next] !=' ' :
              next +=1

        if next >= len(input):
            input = input[:begin]+reverse(input[begin:next])
        else:
            input = input[:begin]+reverse(input[begin:next])+input[next:]
    return reverse(input)

print(handleStr(input_Str))

input()
