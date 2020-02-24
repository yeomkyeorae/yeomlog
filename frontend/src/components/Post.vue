<template>
  <div>
		{{title}}
		{{content}}
	</div>
</template>

<script>
export default {
	name: 'Post',
	props: {
		title: {type: String},
		content: {type: String}
	}
}
</script>

<style>

</style>