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
				<v-list-item>- Javascript</v-list-item>
				<v-list-item>- Pandas, Numpy</v-list-item>
				<v-list-item>- InfluxDB, Grafana</v-list-item>
				<v-list-item>- Elastic Search, Kibana</v-list-item>
				<v-list-item>- SQL</v-list-item>
			</v-list>

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