<template>
	<div class="cv">
		<v-toolbar flat color="blue-grey" dark>
			<v-toolbar-title>Cover Letter</v-toolbar-title>
		</v-toolbar>
		<v-divider class="my-2"></v-divider>

		<h1>Name</h1>
		Kyeorae Yeom
		<v-divider class="my-2"></v-divider>

		<h1>PROFILE</h1>
		<v-list>
			<v-list-item>- Ajou Univ, Major: Economics & ICT convergence, 11.03 ~ 17.02</v-list-item>
			<v-list-item>- NCIA's class for data scientist using IoT, 17.01 ~ 17.06</v-list-item>
			<v-list-item>- Korea Electric Technology Institute(KETI), 17.07 ~ 18.06</v-list-item>
			<v-list-item>- Samsung Software Academy for Youth(SSAFY), 19.07 ~ ing</v-list-item>
		</v-list>
		<v-divider class="my-2"></v-divider>

		<h1>ACCOUNTS</h1>
		<v-list>
			<v-list-item><pre>- </pre><a target="_blank" @click="mail">duarufp06@naver.com</a></v-list-item>
			<v-list-item><pre>- </pre><a href="https://github.com/yeomkyeorae" target="_blank">Github</a></v-list-item>
			<v-list-item><pre>- </pre><a target="_blank">LinkedIn</a></v-list-item>
			<v-list-item><pre>- </pre><a target="_blank">Rocket Punch</a></v-list-item>
			<v-list-item><pre>- </pre><a target="_blank">Programmers</a></v-list-item>
		</v-list>
		<v-divider class="my-2"></v-divider>

		<h1>CERTIFICATE</h1>
		<v-list>
			<v-list-item>- 정보처리기사</v-list-item>
			<v-list-item>- 데이터분석준전문가(ADsP)</v-list-item>
			<v-list-item>- OPIc IM2</v-list-item>
		</v-list>
		<v-divider class="my-2"></v-divider>

		<h1>SKILLS</h1>
		<v-list>
			<v-list-item>- Python</v-list-item>
			<v-list-item>- Django</v-list-item>
			<v-list-item>- Javascript</v-list-item>
			<v-list-item>- Vue.js</v-list-item>
			<v-list-item>- Pandas, Numpy</v-list-item>
			<v-list-item>- InfluxDB, Grafana</v-list-item>
			<v-list-item>- Elastic Search, Kibana</v-list-item>
			<v-list-item>- SQL</v-list-item>
		</v-list>
		<v-divider class="my-2"></v-divider>

		<h1>INTERESTS</h1>
		<v-list>
			<v-list-item>- Web Service(SPA)</v-list-item>
			<v-list-item>- Data Analysis(prediction of time series)</v-list-item>
			<v-list-item>- Deep learning(Object detection, NLP)</v-list-item>
		</v-list>
		<v-divider class="my-2"></v-divider>

		<h1>PROJECTS</h1>
		<div class="mb-5">
			<VueMarkdown>## 1. 푸드코트 어플리케이션 설계(아주대학교 도메인분석및SW설계)</VueMarkdown>
			<VueMarkdown>(2016.09 ~ 2016.12)</VueMarkdown>
			<VueMarkdown>설명 : UML(Unified Modeling Language)기법을 사용하여 푸드코트 서비스를 설계함과 동시에 안드로이드로 구현하는 프로젝트</VueMarkdown>
			<VueMarkdown>### [성과]</VueMarkdown>
			<VueMarkdown>#### 1. UML기법을 익히고, 도메인 설계를 하는 것의 중요성을 인지</VueMarkdown>
			<VueMarkdown>#### 2. 어플리케이션의 구현 이전에 유스케이스(Usecase)를 정립하는 것이 중요성 파악</VueMarkdown>
			<VueMarkdown>#### 3. 협업 능력 향상</VueMarkdown>
		</div>
		<v-divider></v-divider>
		<div class="mb-5">
			<VueMarkdown>## 2. 공모전 팀 빌딩을 위한 웹서비스 구현(아주대학교 ICT융합캡스톤디자인)</VueMarkdown>
			<VueMarkdown>(2016.09 ~ 2016.12)</VueMarkdown>
			<VueMarkdown>설명 : 공모전에 참가하려는 사람들에게 협업필터링 추천 알고리즘을 통해 팀원을 추천해주는 웹서비스 기획 및 구현</VueMarkdown>
			<VueMarkdown>### [성과]</VueMarkdown>
			<VueMarkdown>#### 1. 파이썬 학습</VueMarkdown>
			<VueMarkdown>#### 2. Djanog 백엔드 프레임워크에 대한 이해</VueMarkdown>
			<VueMarkdown>#### 3. 추천 알고리즘 중 하나인 협업필터링 알고리즘에 대한 이해</VueMarkdown>
			<VueMarkdown>#### 4. HTML, CSS 등 웹 기술에 대한 이해</VueMarkdown>
		</div>
		<v-divider></v-divider>
		<div class="mb-5">
			<VueMarkdown>## 3. Kospi200 주식 종목 클러스터링 및 예측(차세대 융합콘텐츠 산업협회)</VueMarkdown>
			<VueMarkdown>(2017.04 ~ 2017.06)</VueMarkdown>
			<VueMarkdown>설명 :코스피200 주식 종목들의 1개월 틱 단위 데이터를 확보하여</VueMarkdown>
			<VueMarkdown>1. Scikit-learn을 활용해 동일한 추세를 보이는 종목 클러스터링(Kmeans, AP(Affiny Propagation 사용).</VueMarkdown>
			<VueMarkdown>2. HMM(Hidden Markov Model)을 활용해 개별 종목 추이 단순 예측.</VueMarkdown>
			<VueMarkdown>### [성과]</VueMarkdown>
			<VueMarkdown>#### 1. 데이터 가공을 위한 Python의 Numpy, Pandas 라이브러리 활용.</VueMarkdown>
			<VueMarkdown>#### 2. Python 머신러닝 라이브러리Scikit-learn 활용.</VueMarkdown>
			<VueMarkdown>#### 3. Hidden Markov 개념 학습.</VueMarkdown>
			<VueMarkdown>#### 4. 데이터분석을 위한 전체 파이프라인 구축 경험(데이터 수집 – 데이터 전처리 – 분석 – 시각화).</VueMarkdown>
		</div>
		<v-divider></v-divider>
		<div class="mb-5">
			<VueMarkdown>## 4. 제지 공장 에너지 절감을 위한 데이터 분석 프로젝트(전자부품연구원)</VueMarkdown>
			<VueMarkdown>(2017.07 ~ 2018.06)</VueMarkdown>
			<VueMarkdown>설명 : 제지 공장에서 발생하는 다양한 데이터(Plant Information data, 실시간 전력 data, MES data 등)로 머신러닝 기법을 활용해 에너지 절감
				포인트들을 찾는 프로젝트.</VueMarkdown>
			<VueMarkdown>### [성과]</VueMarkdown>
			<VueMarkdown>#### 1. 시계열 데이터 전처리(resampling, moving average) 및 핸들링.</VueMarkdown>
			<VueMarkdown>#### 2. 시계열 데이터베이스 InfluxDB 활용.</VueMarkdown>
			<VueMarkdown>#### 3. 논문</VueMarkdown>
			<VueMarkdown>#### 4. feature selection을 위한 Lasso, SVM, Random Forest 등 활용.</VueMarkdown>
			<VueMarkdown>#### 5. 시계열 예측을 위한 RNN(LSTM) 활용.</VueMarkdown>
		</div>
		<v-divider></v-divider>
	</div>
</template>

<script>
	import VueMarkdown from 'vue-markdown'

	export default {
		name: 'Cv',
		components: {
			VueMarkdown
		},
		data() {
			return {
				fullName: 'Kyeorae Yeom'
			}
		},
		methods: {
			mail() {
				window.open('mailto:duarufp06@gmail.com');
			}
		}
	}
</script>
<style>
	.cv {
		text-align: left;
	}
</style>