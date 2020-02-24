<template>
	<div>
		<v-col cols="12" sm="6">
			<v-text-field label="Regular" single-line :value="title"></v-text-field>
		</v-col>
		<v-textarea name="input-7-1" filled label="Content" auto-grow :value="content">
			{{content}}
		</v-textarea>
	</div>
</template>

<script>
	export default {
		name: 'Post',
		props: {
			title: {
				type: String
			},
			content: {
				type: String
			}
		}
	}
</script>

<style>

</style>