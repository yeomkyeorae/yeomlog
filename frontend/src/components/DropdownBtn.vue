<template>
  <v-container>
    <div class="text-center mt-5">
      <v-menu open-on-hover bottom offset-y>
        <template v-slot:activator="{ on }">
          <v-btn color="primary" dark v-on="on">
            Projects
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in items" :key="index">
            <v-list-item @click="setProjectId(item.index)">{{item.title}}</v-list-item>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <Project :projectId="index"/>
  </v-container>
</template>

<script>
  import Project from './Project.vue'

  export default {
    name: 'DropdownBtn',
    components: {
      Project
    },
    data() {
      return {
        index: 0,
        items: [{
            index: 0,
            title: 'Project 1'
          },
          {
            index: 1,
            title: 'Project 2'
          },
        ],
      }
    },
    methods: {
      setProjectId(titleIndex) {
        this.index = titleIndex
      }
    }
  }
</script>