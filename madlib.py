# mad lib game
import time
from sty import Style,RgbFg,ef,rs,fg

fg.dark_orange_red=Style(RgbFg(255,69,0))
fg.lime=Style(RgbFg(0,255,0))
fg.aqua=Style(RgbFg(0,255,255))

with open("story.txt","r")as f:
    story=f.read()
    # print(story)
words=set()
start_of_word=0
target_start="<"
target_end=">"
for i, chr in enumerate(story):
    if chr==target_start:
        start_of_word=i
    if chr==target_end:
        word=story[start_of_word:i+1]
        # start_of_word=-1
        # print(word)
        words.add(word)
# print(words)
answer={}
for word in words:
    answers=input(f"{fg.aqua}{ef.b} Enter Your answer {word} : {rs.all}")
    # print(answers)
    answer[word]=answers
for word in words:
    story=story.replace(word,answer[word])
print(f"{fg.lime}{ef.b}Loding....{rs.all}")
time.sleep(2)
print(f"{fg.dark_orange_red}{ef.i}-------------{rs.all}")
print(f"{fg.aqua}{ef.i}{story}{rs.all}")
print(f"{fg.lime}{ef.b}Loding....{rs.all}")
time.sleep(2)
print(f"{fg.lime}{ef.b} The End!{rs.all}")
print(f"{fg.dark_orange_red}{ef.i}................{rs.all}")
