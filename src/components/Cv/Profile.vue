<template>
	<div class="body">
		<section class="section">
			<article>
				<h1 class="h1">Profile</h1>
				<hr>
			</article>
		</section>
		<section class="section">
			<img :src="require('../../assets/yeom.jpeg')" alt="" style="border-radius: 50%;">
		</section>
		<section class="section">
			<article>
				<h2 class="h2">Name</h2>
				<p class="p">염겨레, Kyeorae Yeom</p>
			</article>
		</section>
		<hr>
		<section class="section">
			<article>
				<h2 class="h2">Address</h2>
				<p class="p">대한민국 세종특별자치시, Sejong, Republic of Korea</p>
			</article>
		</section>
		<hr>
		<section class="section">
			<article>
				<h2 class="h2">Background</h2>
				<p class="p">- SSAFY(Samsung Software Academy For Youth) Trainee, 19.07 ~ ing</p>
				<p class="p">- KETI(Korea Electronics Technology Institute) Researcher, 17.07 ~ 18.06</p>
				<p class="p">- NCIA(차세대융합콘텐츠산업협회) IoT데이터분석을 위한 데이터사이언티스트 양성과정 Trainee, 17.01 ~ 17.06</p>
				<p class="p">- Ajou University(아주대학교) Economics & ICTconvergence Student, 11.03 ~ 17.02</p>
			</article>
		</section>
	</div>
</template>

<script>
	export default {
		name: 'Profile'
	}
</script>

<style>

</style>