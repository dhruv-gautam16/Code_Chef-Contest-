# cook your dish here
def find_word(words, phrase_list):     
     string1 = ""
     for word in words:
          if word in phrase_list:
               string1 += "YES "
          else: 
               string1 += "NO "
     print(string1)
     return string1
T = int(input())
for i in range(T):
     x, y = map(int, input().split())
     words = list(input().strip().split())[:x]
     phrase_list = []
     for j in range(y):
          phrase = list(input().strip().split())
          phrase_list += phrase
     find_word(words, phrase_list)
          