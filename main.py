import feedparser, time

URL = "https://mvcv.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 2

markdown_text = """

## ✍️ Recent Post 
"""  # list of blog posts will be appended here

preREADME1 = """
# 👋 안녕하세요. 임규일입니다. Hello. I'm GYUIL LIM

- 숭실대학교 AI융합학과 석사과정
- M.S. Student in AI at Soongsil University, Major of AI Convergence


## 📪 Contact

- `Email` | swea76019059@gmail.com
- `TechBlog` | <a href="https://stg0123.github.io/" target="_blank">https://mvcv.tistory.com/</a>
"""

preREADME2 = """

## 🏁 AI challenge
- 2023 SW중심대학 공동 AI 경진대회 SW중심대학협의회장상
(2023 University National Center of Excellence in Software Joint AI Competition - Chairman’s Award)

- 2023 2023 Samsung AI Challenge : Camera-Invariant Domain Adaptation 10등
(2023 Samsung AI Challenge - 10th Place in Camera-Invariant Domain Adaptation)

## 🌟 Relevant Experience
- 2024 SW 동행 해커톤 대학생 멘토
(2024 SW DONGHANG Hackathon - University Mentor, Hosted by the Ministry of Science and ICT)

## 📜 Publications
- 이종 특징 맵을 이용한 교차 어텐션 기반 소형 객체 검출 기법, 한국지능시스템학회(KIIS) 추계학술대회, 2024
(Small Object Detection Method Based on Cross Attention of Heterogeneous Feature Maps, Korea Intelligent Information System Society (KIIS) Fall Conference, 2024)

## ⌚ 연혁<br/>
|활동|기간|비고|
|:---:|:---:|:---:|
|숭실대학교 AI융합학부(Soongsil University, School of AI Convergence)|2019.03~2025.02 |-|
|공군 군사경찰(Republic of Korea Air Force, Military Police) |2021.01~2022.10|공군 병장 만기제대(Honorable Discharge as Air Force Sergeant)|
|숭실대학원 AI융합학과 석사과정(M.S. Student in AI at Soongsil University) | 2025.03~ |Computer Vision Research| 

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
