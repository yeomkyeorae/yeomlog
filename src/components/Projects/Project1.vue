<template>
	<div>
		<DropdownBtn/>
		<br>
		<h1>Project 1</h1>
		<br>
		<div style="width:800px; margin: 0 auto;">
			<v-carousel>
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