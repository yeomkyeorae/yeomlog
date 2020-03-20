<template>
  <v-container>
    <div class="text-center mt-5">
      <v-menu open-on-hover bottom offset-y>
        <template v-slot:activator="{ on }">
          <v-btn style="background-color:#F9ACAA" dark v-on="on" :rounded=true>
            Projects
          </v-btn>
        </template>
        <v-list>
          <v-list-item v-for="(item, index) in items" :key="index" continuous="false">
            <v-list-item @click="setProjectId(item.index, item.title)">{{item.title}}</v-list-item>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
    <Project :projectId="index" :title="title" :currentIndex="currentIndex" />
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
        title: '1. 제지공장 데이터 파이프라인 구축 및 LSTM 예측',
        currentIndex : 0,
        items: [{
            index: 0,
            title: '1. 제지공장 데이터 파이프라인 구축 및 LSTM 예측'
          },
          {
            index: 1,
            title: '2. 파이썬을 활용한 주식 코스피200 클러스터링 및 예측'
          },
          {
            index: 2,
            title: '3. 공모전 팀 빌딩을 위한 웹서비스'
          },
          {
            index: 3,
            title: '4. 푸트코트 도메인 분석 및 설계'
          },
          // {
          //   index: 4,
          //   title: '5. SSAFY 인도 델리 해외연수 단기 프로젝트'
          // },
          // {
          //   index: 5,
          //   title: '5. SSAFY 커뮤니티 싸파리'
          // },
        ],
      }
    },
    methods: {
      setProjectId(titleIndex, title) {
        this.index = titleIndex
        this.title = title
      }
    }
  }
</script>