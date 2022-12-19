
#coding=utf-8
import os
if not os.path.exists('output'):
    os.mkdir('output')
if not os.path.exists('output/different_word_in_all'):
    os.mkdir('output/different_word_in_all')
if not os.path.exists('output/different_word_in_likes_or_shares_or_comments'):
    os.mkdir('output/different_word_in_likes_or_shares_or_comments')
if not os.path.exists('output/same_word'):
    os.mkdir('output/same_word')


#获取all_text的top50词放进数组
# Get the top50 words of all_text and put them into an array
all_txt = open('top50_word/top50_word_for_all_texts.txt','r',errors='ignore').read()
all_txt.replace("(","",50).replace(")","",50)
# print(all_txt.replace("(","",50).replace(")","",50))
all_list = all_txt.replace("(","",50).replace(")","",50).replace("\'","",100).replace("\"","",100).split(',')
all_list='\n'.join(all_list)
all_list=all_list.split('\n')
# print(all_list)
cnt = 0
all=[]
for i in all_list:
   cnt = cnt+1
   if(cnt%2==1):
      all.append(i)
# print(all)





#求按likes排行的top50text中的top50个词 与 all_text的top50词 中相同的词和不同的词
# Find the top50 words in the top50text ranked by likes and the same words and different words in the top50words of all_text
likes_txt = open('top50_word/top50_word_for_sort_by_likes_texts.txt','r',errors='ignore').read()
likes_txt.replace("(","",50).replace(")","",50)
# print(likes_txt.replace("(","",50).replace(")","",50))
likes_list = likes_txt.replace("(","",50).replace(")","",50).replace("\'","",100).replace("\"","",100).split(',')
likes_list='\n'.join(likes_list)
likes_list=likes_list.split('\n')
# print(likes_list)
cnt = 0
likes=[]
for i in likes_list:
   cnt = cnt+1
   if(cnt%2==1):
      likes.append(i)
# print(likes)
# for i in all:
#     for j in likes:
#         if(i==j):
#             print(i)
same_like = []
with open('output/same_word/same_word_like_all.txt', 'w+', encoding='utf-8') as f:
    for i in all:
        for j in likes:
            if (i == j):
                f.write((str(i) + '\n'))
                same_like.append(str(i))

with open('output/different_word_in_likes_or_shares_or_comments/different_word_in_like_all.txt', 'w+', encoding='utf-8') as f:
    for i in likes:
        if i not in same_like:
            f.write((str(i) + '\n'))

with open('output/different_word_in_all/different_word_like_in_all.txt', 'w+', encoding='utf-8') as f:
    for i in all:
        if i not in same_like:
            f.write((str(i) + '\n'))









#求按shares排行的top50text中的top50个词 与 all_text的top50词 中相同的词和不同的词
#find the top50 words in the top50text ranked by shares and the same words and different words in the top50words of all_text
shares_txt = open('top50_word/top50_word_for_sort_by_shares_texts.txt','r',errors='ignore').read()
shares_txt.replace("(","",50).replace(")","",50)
# print(shares_txt.replace("(","",50).replace(")","",50))
shares_list = shares_txt.replace("(","",50).replace(")","",50).replace("\'","",100).replace("\"","",100).split(',')
shares_list='\n'.join(shares_list)
shares_list=shares_list.split('\n')
# print(shares_list)
cnt = 0
shares=[]
for i in shares_list:
   cnt = cnt+1
   if(cnt%2==1):
      shares.append(i)
# print(shares)
# for i in all:
#     for j in shares:
#         if(i==j):
#             print(i)


same_shares = []
with open('output/same_word/same_word_shares_all.txt', 'w+', encoding='utf-8') as f:
    for i in all:
        for j in shares:
            if (i == j):
                f.write((str(i) + '\n'))
                same_shares.append(str(i))

with open('output/different_word_in_likes_or_shares_or_comments/different_word_in_shares_all.txt', 'w+', encoding='utf-8') as f:
    for i in shares:
        if i not in same_shares:
            f.write((str(i) + '\n'))
with open('output/different_word_in_all/different_word_shares_in_all.txt', 'w+', encoding='utf-8') as f:
    for i in all:
        if i not in same_shares:
            f.write((str(i) + '\n'))








#求按comments排行的top50text中的top50个词 与 all_text的top50词 中相同的词和不同的词
#find the top50 words in the top50text ranked by comments with the same words and different words in the top50words of all_text
comments_txt = open('top50_word/top50_word_for_sort_by_comments_texts.txt','r',errors='ignore').read()
comments_txt.replace("(","",50).replace(")","",50)
# print(comments_txt.replace("(","",50).replace(")","",50))
comments_list = comments_txt.replace("(","",50).replace(")","",50).replace("\'","",100).replace("\"","",100).split(',')
comments_list='\n'.join(comments_list)
comments_list=comments_list.split('\n')
# print(comments_list)
cnt = 0
comments=[]
for i in comments_list:
   cnt = cnt+1
   if(cnt%2==1):
      comments.append(i)
# print(comments)
# for i in all:
#     for j in comments:
#         if(i==j):
#             print(i)

same_comments = []
with open('output/same_word/same_word_comments_all.txt', 'w+', encoding='utf-8') as f:
    for i in all:
        for j in comments:
            if (i == j):
                f.write((str(i) + '\n'))
                same_comments.append(str(i))

with open('output/different_word_in_likes_or_shares_or_comments/different_word_in_comments_all.txt', 'w+', encoding='utf-8') as f:
    for i in comments:
        if i not in same_comments:
            f.write((str(i) + '\n'))

with open('output/different_word_in_all/different_word_comments_in_all.txt', 'w+', encoding='utf-8') as f:
    for i in all:
        if i not in same_comments:
            f.write((str(i) + '\n'))
