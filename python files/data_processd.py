import pandas as pd
import os
#停用词表 stopwords list
txt = open('stopwords list.txt','r',errors='ignore').read()
txt = txt.lower()
stoplist = txt.split('\n')

#处理数据，留下text,likes,shares,comments这四列，其余列都删掉
#process the data, leaving the four columns text,likes,shares,comments and deleting the rest
data = pd.read_csv('fb_scrapped_bbc.csv', encoding='utf-8')
# print(data.columns)
data.drop(columns=['Unnamed: 0', 'post_id', 'post_text', 'shared_text',
       'original_text', 'time', 'timestamp', 'image', 'image_lowquality',
       'images', 'images_description', 'images_lowquality',
       'images_lowquality_description', 'video', 'video_duration_seconds',
       'video_height', 'video_id', 'video_quality', 'video_size_MB',
       'video_thumbnail', 'video_watches', 'video_width',  'post_url', 'link', 'links', 'user_id', 'username',
       'user_url', 'is_live', 'factcheck', 'shared_post_id', 'shared_time',
       'shared_user_id', 'shared_username', 'shared_post_url', 'available',
       'comments_full', 'reactors', 'w3_fb_url', 'reactions', 'reaction_count',
       'with', 'page_id', 'sharers', 'image_id', 'image_ids', 'was_live',
                   # 'shares','likes','comments',
       'fetched_time'],inplace = True)


#生成top50的test的csv文件
# Generate csv file of test for top50
data.to_csv("sort_by_likes_or_shares_or_comments/all_texts.csv",index=True,sep=',')

data=data.sort_values('likes',ascending = False)
data.head(49).to_csv("sort_by_likes_or_shares_or_comments/sort_by_likes_top50.csv",index=True,sep=',')

data=data.sort_values('shares',ascending = False)
data.head(49).to_csv("sort_by_likes_or_shares_or_comments/sort_by_shares_top50.csv",index=True,sep=',')

ata=data.sort_values('comments',ascending = False)
data.head(49).to_csv("sort_by_likes_or_shares_or_comments/sort_by_comments_top50.csv",index=True,sep=',')






#生成top50的test的txt文件
# Generate txt file of test for top50
data.to_csv("sort_by_likes_or_shares_or_comments/all_texts.csv",index=True,sep=',')
data = pd.read_csv('sort_by_likes_or_shares_or_comments/all_texts.csv', encoding='utf-8')
with open('sort_by_likes_or_shares_or_comments/all_texts.txt', 'w+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[1]) + '\n'))

data.to_csv("sort_by_likes_or_shares_or_comments/sort_by_likes_top50.csv",index=True,sep=',')
data = pd.read_csv('sort_by_likes_or_shares_or_comments/sort_by_likes_top50.csv', encoding='utf-8')
with open('sort_by_likes_or_shares_or_comments/sort_by_likes_top50.txt', 'w+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[2]) + '\n'))

data.to_csv("sort_by_likes_or_shares_or_comments/sort_by_shares_top50.csv",index=True,sep=',')
data = pd.read_csv('sort_by_likes_or_shares_or_comments/sort_by_shares_top50.csv', encoding='utf-8')
with open('sort_by_likes_or_shares_or_comments/sort_by_shares_top50.txt', 'w+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[3]) + '\n'))

data.to_csv("sort_by_likes_or_shares_or_comments/sort_by_comments_top50.csv",index=True,sep=',')
data = pd.read_csv('sort_by_likes_or_shares_or_comments/sort_by_comments_top50.csv', encoding='utf-8')
with open('sort_by_likes_or_shares_or_comments/sort_by_comments_top50.txt', 'w+', encoding='utf-8') as f:
    for line in data.values:
        f.write((str(line[4]) + '\n'))





#去除text里面的停用词
# Remove deactivated words from text
data_size=data.shape[0]-1
# print(data.iat[0,1])
for i in range(data_size):
    data.iat[i, 1]=str(data.iat[i, 1])
    data.iat[i, 1].replace("'","")
    tmp = str(data.iat[i, 1].replace("\"","",100).replace("\'","",100).replace(".","",100).replace("“","",100).replace("”","",100))
   # print(tmp)
    words = tmp.split()
    str_= ""
    for word in words:
        if word not in stoplist:
            str_=str_+" "+word
    data.iat[i, 1]=str_
# data.to_csv("news_.csv", index=0)

