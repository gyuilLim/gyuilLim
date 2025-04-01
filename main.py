import feedparser, time

URL = "https://mvcv.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 2

markdown_text = """

## ✍️ Recent Post 
"""  # list of blog posts will be appended here

preREADME1 = """
# 👋 Hello. I'm GYUIL LIM

- M.S. Student in AI at Soongsil University, Major of AI Convergence


## 📪 Contact

- `Email` | swea76019059@gmail.com
- `TechBlog` | <a href="https://stg0123.github.io/" target="_blank">https://mvcv.tistory.com/</a>
"""

preREADME2 = """

## 🏁 AI challenge
- 2023 University National Center of Excellence in Software Joint AI Competition - Chairman’s Award
- 2023 Samsung AI Challenge - 10th Place in Camera-Invariant Domain Adaptation

## 🌟 Relevant Experience
- 2024 SW DONGHANG Hackathon - University Mentor, Hosted by the Ministry of Science and ICT

## 📜 Publications
- Small Object Detection Method Based on Cross Attention of Heterogeneous Feature Maps, Korean Institute of Intelligent Systems(KIIS) Fall Conference, 2024

## 🗂️ Project
- [Satellite Image Building Area Segmentation(2023)](https://github.com/gyuilLim/Satellite_Image_Building_Area_Segmentation)
- [Camera Invariant Domain Adaptation(2023)](https://github.com/gyuilLim/Camera_Invariant_Domain_Adaptation)
- [Youtube Scene Search With Text(2024)](https://github.com/gyuilLim/Youtube-scene-search-with-text)
- [Scene Search Video Player(2024)](https://github.com/gyuilLim/Scene-search-video-player)

## ⌚ History<br/>
|Activity|Period|Note|
|:---:|:---:|:---:|
|Soongsil University, School of AI Convergence|2019.03~2025.02 |-|
|Republic of Korea Air Force, Military Police|2021.01~2022.10|Honorable Discharge as Air Force Sergeant|
|M.S. Student in AI at Soongsil University|2025.03~|Computer Vision Research| 

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
