<template>
	<div class="cv">
		<nav class="flex items-center justify-between flex-wrap bg-pink-400 p-2">
			<span class="flex items-center flex-no-shrink text-white mr-6">Cover Letter</span>
		</nav>
	</div>
</template>

<script>
	export default {
		name: 'Cv',
		components: {

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