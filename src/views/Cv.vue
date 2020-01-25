<template>
 <v-card>
    <v-toolbar flat color="blue-grey" dark>
			<v-toolbar-title>Cover Letter</v-toolbar-title>
    </v-toolbar>

    <v-card-text>
			<v-divider class="my-2"></v-divider>
      <v-text-field filled label="Name" value="asdfasdf"></v-text-field>

			<v-divider class="my-2"></v-divider>
      <v-textarea
        filled
        label="Education"
        value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
      >
			</v-textarea>

      <v-divider class="my-2"></v-divider>
			<v-textarea
        filled
        label="Interests"
        value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
      >
			</v-textarea>

			<v-divider class="my-2"></v-divider>
			<v-textarea
        filled
        label="Projects list"
        value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt."
      >
			</v-textarea>
    </v-card-text>




  </v-card>
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