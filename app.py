
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': '元宵',
    'last_name' : '许',
    'address' : '湖北省',
    'job': 'Web开发',
    'tel': '156****0734',
    'email': 'xyx15629760734@outlook.com',
    'description' : '认为大数据是这个高科技时代的产物，研究大数据，最重要的意义是预测探究。因为数据从根本上讲，是对过去和现在的归纳和总结，其本身不具备趋势和方向性的特征，但是我们可以应用大数据去了解事物发展的客观规律、了解人类行为，并且能够帮助我们改变过去的思维方式，建立新的数据思维模型，从而对未来进行预测和推测',
    'hobbies':'爱好编程，喜欢新鲜食物，勤于动手',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/yuanxiao9',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/b.jpg',
    'experiences' : [
        {
            'title' : 'Web Developer',
            'company': '飞机购票系统',
            'description' : '查询航班时间出发点等及信息供用户选择购票',
            'timeframe' : 'July 2018 - November 2019'
        },
        {
            'title' : 'Freelance Web Developer',
            'company': '购物商城',
            'description' : '用户登录注册购物商城，添加商品到购物车进行支付 ',
            'timeframe' : 'February 2019 - Present'
        },
        {
            'title' : 'Android Studio',
            'company': '音乐APP',
            'description' : '实现一个在线搜索并可以下载音乐的播放器',
            'timeframe' : 'October 2021 - October 2021'
        }
    ],
    'education' : [
        {
            'university': '湖北师范大学',
            'degree': '计算机与信息工程学院',
            'description' : '软件工程',
            'mention' : 'Bien',
            'timeframe' : '2018 - 2022'
        }
        # {
        #     'university': 'Paris Dauphine',
        #     'degree': 'Master en Management global',
        #     'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
        #     'mention' : 'Bien',
        #     'timeframe' : '2015'
        # },
        # {
        #     'university': 'Lycée Turgot - Paris Sorbonne',
        #     'degree': 'CPGE Economie & Gestion',
        #     'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
        #     'mention' : 'N/A',
        #     'timeframe' : '2010 - 2012'
        # }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('resume.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))
   
@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON=gm())

def gm(country='United Kingdom'):
	df = pd.DataFrame(px.data.gapminder())

	fig = px.line(df[df['country']==country], x="year", y="gdpPercap")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON


@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
