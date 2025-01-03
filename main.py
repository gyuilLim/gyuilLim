import feedparser, time

URL = "https://mvcv.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 2

markdown_text = """

## ✍️ Recent Post 
"""  # list of blog posts will be appended here

preREADME1 = """
# 👋 안녕하세요. 임규일입니다.
- (현)숭실대학교 Vision system laboratory
- (현)숭실대학교 AI융합학부


## 📪 Contact

- `Email` | swea76019059@gmail.com
- `TechBlog` | <a href="https://stg0123.github.io/" target="_blank">https://mvcv.tistory.com/</a>
"""

preREADME2 = """

## 🏁 AI challenge
- 2023 SW중심대학 공동 AI 경진대회 SW중심대학협의회장상
- 2023 2023 Samsung AI Challenge : Camera-Invariant Domain Adaptation 10등

## 🌟 Relevant Experience
- 2024 SW 동행 해커톤 대학생 멘토

## 📜 Publications
- 이종 특징 맵을 이용한 교차 어텐션 기반 소형 객체 검출 기법, 한국인공지능시스템학회(KIIS) 추계학술대회, 2024

## ⌚ 연혁<br/>
|활동|기간|비고|
|:---:|:---:|:---:|
|숭실대학교 AI융합학부|2019.03~2025.02 |-|
|공군 군사경찰 |2021.01~2022.10|공군 병장 만기제대|
|숭실대학교 Vision System Lab | 2023.06~ | Computer Vision |

"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"- [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

resultREADME = f"{preREADME1}{markdown_text}{preREADME2}"
        
f = open("README.md", mode="w", encoding="utf-8")
f.write(resultREADME)
f.close()
