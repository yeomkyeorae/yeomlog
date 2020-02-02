<template>
 <div class="cv">
    <v-toolbar flat color="blue-grey" dark>
			<v-toolbar-title>Cover Letter</v-toolbar-title>
    </v-toolbar>

		<v-divider class="my-2"></v-divider>

		<h1>Name</h1>
		Kyeorae Yeom

		<v-divider class="my-2"></v-divider>
      
			<h1>Education</h1>
			<v-list>
				<v-list-item>- Ajou Univ, Major: Economics & ICT convergence, 11.03 ~ 17.02</v-list-item>
				<v-list-item>- NCIA's class for data scientist using IoT, 17.01 ~ 17.06</v-list-item>
				<v-list-item>- Samsung Software Academy for Youth(SSAFY), 19.07 ~ ing</v-list-item>
			</v-list>
      
			<v-divider class="my-2"></v-divider>

			<h1>skills</h1>
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

			<h1>Interests</h1>
			<v-list>
				<v-list-item>- Web Service(SPA)</v-list-item>
				<v-list-item>- Data Analysis(prediction of time series)</v-list-item>
				<v-list-item>- Deep learning(Object detection, NLP)</v-list-item>
			</v-list>

			<v-divider class="my-2"></v-divider>

			<h1>Projects</h1>
			<v-list>
				<v-list-item>- Project 1</v-list-item>
				<pre>Kospi200 주식 종목 클러스터링 및 예측(차세대 융합콘텐츠 산업협회)
(2017.04 ~ 2017.06)
설명 :코스피200 주식 종목들의 1개월 틱 단위 데이터를 확보하여
 
1. Scikit-learn을 활용해 동일한 추세를 보이는 종목 클러스터링(Kmeans, AP(Affiny Propagation 사용).
2. HMM(Hidden Markov Model)을 활용해 개별 종목 추이 단순 예측.

성과
• 데이터 가공을 위한 Python의 Numpy, Pandas 라이브러리 활용.
• Python 머신러닝 라이브러리Scikit-learn 활용.
• Hidden Markov 개념 학습.
• 데이터분석을 위한 전체 파이프라인 구축 경험(데이터 수집 – 데이터 전처리 – 분석 – 시각화).</pre>
				<v-list-item>- Project 2</v-list-item>
				<pre>제지 공장 에너지 절감을 위한 데이터 분석 프로젝트(전자부품연구원)
(2017.07 ~ 진행 중)
설명 : 제지 공장에서 발생하는 다양한 데이터(Plant Information data, 실시간 전력 data, MES data 등)로 머신러닝 기법을 활용해 에너지 절감 포인트들을 찾는 프로젝트.   


성과
• 시계열 데이터 전처리(resampling, moving average) 및 핸들링.
• 시계열 데이터베이스 InfluxDB 활용.
• 논문
• feature selection을 위한 Lasso, SVM, Random Forest 등 활용.
• 시계열 예측을 위한 RNN(LSTM) 활용.
• etc.</pre>
			</v-list>

			<v-divider class="my-2"></v-divider>
  </div>
</template>

<script>
export default {
	name: 'Cv',
	data() {
		return {
			fullName: 'Kyeorae Yeom'
		}
	}
}
</script>
<style>
.cv {
	text-align: left;
}
</style>