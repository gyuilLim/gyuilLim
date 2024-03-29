## update_blogPost.py
import feedparser

blog_url = "https://mvcv.tistory.com/rss"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
# 👋 안녕하세요. 임규일입니다.
- (현)SSU Vision Lab
- (현)숭실대학교 AI융합학부

## 📪 Contact

- `Email` | swea76019059@gmail.com
- `TechBlog` | <a href="https://stg0123.github.io/" target="_blank">https://mvcv.tistory.com/</a>

## 🏁 AI challenge
- 2023 SW중심대학 공동 AI 경진대회 SW중심대학협의회장상
- 2023 2023 Samsung AI Challenge : Camera-Invariant Domain Adaptation 10등

## ⌚ 연혁<br/>
|활동|기간|비고|
|---|---|---|
|숭실대학교 AI융합학부|2019.03~ | 숭실대학교 AI융합학부 소속|
|공군 군사경찰 |2021.01~2022.10|공군 병장 만기제대|
|숭실대학교 Vision Lab | 2023.06~ | Computer Vision |

"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
