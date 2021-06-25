
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np

from tqdm import tqdm_notebook
import sys
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt11
import matplotlib.pyplot as plt12
import matplotlib.pyplot as plt13
import matplotlib.pyplot as plt14
import seaborn as sns
import seaborn as sns1
import seaborn as sns2
import seaborn as sns3
import seaborn as sns4
import seaborn as sns11
import seaborn as sns12

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
    'description' : '大数据是这个高科技时代的产物，研究大数据，最重要的意义是预测探究。因为数据从根本上讲，是对过去和现在的归纳和总结，其本身不具备趋势和方向性的特征，但是我们可以应用大数据去了解事物发展的客观规律、了解人类行为，并且能够帮助我们改变过去的思维方式，建立新的数据思维模型，从而对未来进行预测和推测',
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
            'timeframe' : '2018.12-2019-1'
        },
        {
            'title' : 'Freelance Web Developer',
            'company': '购物商城',
            'description' : '用户登录注册购物商城，添加商品到购物车进行支付 ',
            'timeframe' : '2020.11-2020.12'
        },
        {
            'title' : 'Android Studio',
            'company': '音乐APP',
            'description' : '实现一个在线搜索并可以下载音乐的播放器',
            'timeframe' : '2021.4-2021.6'
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
    return render_template('index123.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))#前端页面传输来的
   
@app.route('/chart')
def index():
	return render_template('chartsajax.html')
@app.route('/water')
def index1():
    return render_template('water.html')
def gm(country='United Kingdom'):
    df = pd.read_csv(r'C:\Users\苏苏\Desktop\shuju\test_scores.csv', encoding='utf-8')
    df.drop('student_id', axis=1, inplace=True)
    plt.figure(figsize=(10, 5))
    sns.kdeplot(data=df['pretest'], shade=True, label='Pre-test')
    sns.kdeplot(data=df['posttest'], shade=True, label='Post-test')
    plt.title('Distribution of Pre Test and Post Test')
    plt.legend()
    plt.savefig('前后测试分数比较.png')

    fig = plt1.figure(figsize=(30, 10))
    sns1.boxplot(x='classroom', y='posttest', data=df.sort_values('posttest'))
    plt1.savefig('每个教室的分数分布.png')

    fig, ax = plt2.subplots(1, 2, figsize=(10, 5))
    sns2.boxplot(x='lunch', y='posttest', data=df, ax=ax[0])
    sns2.boxplot(x='gender', y='posttest', data=df, ax=ax[1])
    plt2.savefig('学生特征.png')

    sns3.regplot(data=df, x='n_student', y='posttest')
    plt3.savefig('后测分数与人数关系.png')

    f, axes = plt4.subplots(1, 3, figsize=(10, 5))
    sns4.boxplot(data=df, x='teaching_method', y='posttest', ax=axes[0])
    sns4.boxplot(data=df, x='school_type', y='posttest', ax=axes[1])
    sns4.boxplot(data=df, x='school_setting', y='posttest', ax=axes[2])
    plt4.tight_layout()
    plt4.savefig('影响后测分数因素.png')

    df1 = pd.DataFrame(px.data.gapminder())
    fig = px.line(df1[df1['country'] == country], x="year", y="gdpPercap")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def bm():
    df = pd.read_csv(r'C:\Users\苏苏\Desktop\shuju\water_potability.csv', encoding='utf-8')
    df.dropna(inplace=True)

    plt11.figure(figsize=(12, 6))
    sns11.countplot(x="Potability", data=df, palette='husl')
    plt11.savefig('可饮用性和不可饮性样本数量对比.png')

    pieChartPlotter(df, 'Potability')
    plt12.savefig('可饮用性和不可饮性占比.png')

    plot_data = df.drop(['Potability'], axis=1)
    distributionPlot(plot_data)
    plt13.savefig('水中物质影响可饮用性.png')

    sns12.pairplot(df, hue="Potability", palette="husl");
    plt14.savefig('水中物质相关性.png')
def distributionPlot(dataset):
    """
    Creates distribution plot.
    """
    fig = plt.figure(figsize=(20, 20))
    for i in tqdm_notebook(range(0, len(dataset.columns)), desc = 'Your plots are being ready'):
        fig.add_subplot(np.ceil(len(dataset.columns)/3), 3, i+1)
        sns.distplot(
            dataset.iloc[:, i], color="lightcoral", rug=True)
        fig.tight_layout(pad=3.0)

def pieChartPlotter(dataset, columnName):
    values = dataset[columnName].value_counts()
    labels = dataset[columnName].unique()
    pie, ax = plt.subplots(figsize=[10, 6])
    patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.2f%%', shadow=True, pctdistance=.5,explode=[0.06]*dataset[columnName].unique()
                                       )
    plt.legend(patches, labels, loc="best")
    plt.title(columnName, color='white', fontsize=14)
    plt.setp(texts, color='white', fontsize=20)
    plt.setp(autotexts, size=10, color='black')
    autotexts[1].set_color('black')
    plt.axis('equal')
    plt.tight_layout()
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
