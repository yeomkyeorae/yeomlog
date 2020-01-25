<template>
  <div class="text-center mt-5">
    <v-menu open-on-hover bottom offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          color="primary"
          dark
          v-on="on"
        >
          Projects
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
        >
					<router-link :to="`/projects/${ index }`">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
					</router-link>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
export default {
  name: 'DropdownBtn',
	data: () => ({
	items: [
			{ title: 'Project 1' },
			{ title: 'Project 2' },
		],
	}),
}
</script>