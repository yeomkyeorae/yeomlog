<template>
	<div>
		<div>
			<title>
				<h1>Project 1</h1>
			</title>
		</div>
		<br>
			<v-carousel :height="1000" hide-delimiters v-model="currentIndex">
				<v-carousel-item v-for="(item, i) in items[projectId]" :key="i">
					<v-img :src="item.src" aspect-ratio="1.77"></v-img>
				</v-carousel-item>
			</v-carousel>
		</div>
</template>

<script>
	// import axios from 'axios'

	export default {
		name: 'project',
		components: {
			// axios
		},
		props: {
			projectId: {
				type: Number
			},
			title: {
				type: String
			},
		},
		watch: {
			projectId() {
				this.currentIndex = 0
			}
		},
		data() {
			return {
				currentIndex: 0,
				items: {
					0: [
						{ src: require('@/assets/Projects/Project1/1-01.jpg')},
						{ src: require('@/assets/Projects/Project1/1-02.jpg')},
						{ src: require('@/assets/Projects/Project1/1-03.jpg')},
						{ src: require('@/assets/Projects/Project1/1-04.jpg')},
						{ src: require('@/assets/Projects/Project1/1-05.jpg')},
						{ src: require('@/assets/Projects/Project1/1-06.jpg')},
						{ src: require('@/assets/Projects/Project1/1-07.jpg')},
						{ src: require('@/assets/Projects/Project1/1-08.jpg')},
						{ src: require('@/assets/Projects/Project1/1-09.jpg')},
						{ src: require('@/assets/Projects/Project1/1-10.jpg')},
						{ src: require('@/assets/Projects/Project1/1-11.jpg')},
					],
					1: [
						{ src: require('@/assets/Projects/Project2/2-01.jpg')},
						{ src: require('@/assets/Projects/Project2/2-02.jpg')},
						{ src: require('@/assets/Projects/Project2/2-03.jpg')},
						{ src: require('@/assets/Projects/Project2/2-04.jpg')},
						{ src: require('@/assets/Projects/Project2/2-05.jpg')},
						{ src: require('@/assets/Projects/Project2/2-06.jpg')},
						{ src: require('@/assets/Projects/Project2/2-07.jpg')},
						{ src: require('@/assets/Projects/Project2/2-08.jpg')},
						{ src: require('@/assets/Projects/Project2/2-09.jpg')},
						{ src: require('@/assets/Projects/Project2/2-10.jpg')},
						{ src: require('@/assets/Projects/Project2/2-11.jpg')},
						{ src: require('@/assets/Projects/Project2/2-12.jpg')},
						{ src: require('@/assets/Projects/Project2/2-13.jpg')},
						{ src: require('@/assets/Projects/Project2/2-14.jpg')},
						{ src: require('@/assets/Projects/Project2/2-15.jpg')},
						{ src: require('@/assets/Projects/Project2/2-16.jpg')},
					],
					2: [
						{ src: require('@/assets/Projects/Project3/3-01.jpg')},
						{ src: require('@/assets/Projects/Project3/3-02.jpg')},
						{ src: require('@/assets/Projects/Project3/3-03.jpg')},
						{ src: require('@/assets/Projects/Project3/3-04.jpg')},
						{ src: require('@/assets/Projects/Project3/3-05.jpg')},
						{ src: require('@/assets/Projects/Project3/3-06.jpg')},
						{ src: require('@/assets/Projects/Project3/3-07.jpg')},
						{ src: require('@/assets/Projects/Project3/3-08.jpg')},
						{ src: require('@/assets/Projects/Project3/3-09.jpg')},
						{ src: require('@/assets/Projects/Project3/3-10.jpg')},
						{ src: require('@/assets/Projects/Project3/3-11.jpg')},
						{ src: require('@/assets/Projects/Project3/3-12.jpg')},
					],
				3: [
					{ src: require('@/assets/Projects/Project4/4-01.jpg')},
					{ src: require('@/assets/Projects/Project4/4-02.jpg')},
					{ src: require('@/assets/Projects/Project4/4-03.jpg')},
					{ src: require('@/assets/Projects/Project4/4-04.jpg')},
					{ src: require('@/assets/Projects/Project4/4-05.jpg')},
					{ src: require('@/assets/Projects/Project4/4-06.jpg')},
					{ src: require('@/assets/Projects/Project4/4-07.jpg')},
					{ src: require('@/assets/Projects/Project4/4-08.jpg')},
					{ src: require('@/assets/Projects/Project4/4-09.jpg')},
					{ src: require('@/assets/Projects/Project4/4-10.jpg')},
					{ src: require('@/assets/Projects/Project4/4-11.jpg')},
					{ src: require('@/assets/Projects/Project4/4-12.jpg')},
				]
				}
			}
		},
	}
</script>

<style>

</style>