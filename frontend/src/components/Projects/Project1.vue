<template>
	<div>
		<DropdownBtn/>
		<br>
		<div>
		<title><h1>Project 1</h1></title>
		</div>
		<div>
			<v-content>{{ intro }}</v-content>
		</div>
		<br>
		<div style="width:1000px; margin: 0 auto;">
			<v-carousel :height="600" hide-delimiters>
			<v-carousel-item
				v-for="(item,i) in items"
				:key="i"
				:src="item.src"
				reverse-transition="fade-transition"
				transition="fade-transition"
			></v-carousel-item>
			</v-carousel>
		</div>
	</div>
</template>

<script>
import DropdownBtn from '@/components/DropdownBtn.vue'

export default {
    name: 'project1',
    components: {
        DropdownBtn
		},
		data () {
      return {
				intro: '해당 프로젝트는...',
        items: [
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/squirrel.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/sky.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/bird.jpg',
          },
          {
            src: 'https://cdn.vuetifyjs.com/images/carousel/planet.jpg',
          },
        ],
      }
    },
}
</script>

<style>

</style>