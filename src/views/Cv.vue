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
			<ol>
				<li>asdf</li>
				<li>qwer</li>
			</ol>
      
			<v-divider class="my-2"></v-divider>

			<h1>skills</h1>
			<ol>
				<li>asdf</li>
				<li>qwer</li>
			</ol>

			<v-divider class="my-2"></v-divider>

			<h1>Interests</h1>
			<ol>
				<li>asdf</li>
				<li>qwer</li>
			</ol>

			<v-divider class="my-2"></v-divider>

			<h1>Projects</h1>
			<ol>
				<li>asdf</li>
				<li>qwer</li>
			</ol>

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