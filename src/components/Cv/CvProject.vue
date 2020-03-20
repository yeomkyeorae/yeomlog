<template>
	<div class="body">
		<section class="section">
			<article>
				<h1 class="h1">Projects</h1>
				<hr>
			</article>
		</section>
		<section class="section">
			<article>
				<h3 class="h3">17.07 ~ 18.06</h3>
				<h2 class="h2">제지 공장 에너지 절감을 위한 데이터 분석 프로젝트(전자부품연구원)</h2>
				<p class="p">제지 공장에서 발생하는 다양한 데이터(Plant Information data, 실시간 전력 data, MES data 등)로 머신러닝 기법을 활용해 에너지 절감
					포인트들을 찾는 프로젝트</p>
				<p class="p">1. 시계열 데이터 전처리(resampling, moving average) 및 핸들링<br>
					2. 시계열 데이터베이스 InfluxDB 활용 및 Grafana 대시보드 활용<br>
					3-1. (논문)전자공학회, 제조공장 원료 공정상 발생하는 고압 전력과 원료 공정 변수들의 상관관계 분석<br>
					3-2. (논문)ICUFN, Prediction of Manufacturing Plant's Electric Power Using Maching Learning<br>
					4. feature selection을 위한 Lasso, SVM, Random Forest 등 활용<br>
					5. 시계열 예측을 위한 RNN(LSTM) 활용
				</p>
			</article>
		</section>
		<hr>
		<section class="section">
			<article>
				<h3 class="h3">17.04 ~ 17.06</h3>
				<h2 class="h2">Kospi200 주식 종목 클러스터링 및 예측(차세대융합콘텐츠산업협회)</h2>
				<p class="p">코스피200 주식 종목들의 1개월 틱 단위 데이터를 확보하여<br>
					- Scikit-learn을 활용해 동일한 추세를 보이는 종목 클러스터링(Kmeans, AP(Affiny Propagation 사용)<br>
					- HMM(Hidden Markov Model)을 활용해 개별 종목 추이 단순 예측
				</p>
				<p class="p">1. 데이터 가공을 위한 Python의 Numpy, Pandas 라이브러리 활용<br>
					2. Python 머신러닝 라이브러리Scikit-learn 활용<br>
					3. Hidden Markov 개념 학습<br>
					4. 데이터분석을 위한 전체 파이프라인 구축 경험(데이터 수집 – 데이터 전처리 – 분석 – 시각화)
				</p>
			</article>
		</section>
		<hr>
		<section class="section">
			<article>
				<h3 class="h3">16.09 ~ 16.12</h3>
				<h2 class="h2">공모전 팀 빌딩을 위한 웹서비스 구현(아주대학교 ICT융합캡스톤디자인)</h2>
				<p class="p">공모전에 참가하려는 사람들에게 협업필터링 추천 알고리즘을 통해 팀원을 추천해주는 웹서비스 기획 및 구현</p>
				<p class="p">1. 파이썬 학습<br>
					2. Djanog 백엔드 프레임워크에 대한 이해<br>
					3. 추천 알고리즘 중 하나인 협업필터링 알고리즘에 대한 이해<br>
					4. HTML, CSS 등 웹 기술에 대한 이해<br>
				</p>
			</article>
		</section>
		<hr>
		<section class="section">
			<article>
				<h3 class="h3">16.09 ~ 16.12</h3>
				<h2 class="h2">푸드코트 어플리케이션 설계(아주대학교 도메인분석및SW설계)</h2>
				<p class="p">UML(Unified Modeling Language)기법을 사용하여 푸드코트 서비스를 설계함과 동시에 안드로이드로 구현하는 프로젝트</p>
				<p class="p">1. UML기법을 익히고, 도메인 설계를 하는 것의 중요성을 인지<br>
					2. 어플리케이션의 구현 이전에 유스케이스(Usecase)를 정립하는 것이 중요성 파악<br>
					3. 협업 능력 향상</p>
			</article>
		</section>

	</div>
</template>

<script>
	export default {
		name: 'CvProject'
	}
</script>

<style>

</style>