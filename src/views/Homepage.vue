<template>
  <div>
    <ClickMeModal class="mt-3" />
    <v-row>
      <v-col cols="12">
        <v-card>
          <v-container fluid>
            <v-row>
              <v-col v-for="n in 9" :key="n" class="d-flex child-flex" cols="12" md="4" sm="6" xs="12">
                <v-card flat tile class="d-flex">
                  <v-img :src="require(`../assets/Profile/${n}.jpeg`)"
                    :lazy-src="require(`../assets/Profile/${n}.jpeg`)" aspect-ratio="1"
                    class="grey lighten-2">
                    <template v-slot:placeholder>
                      <v-row class="fill-height ma-0" align="center" justify="center">
                        <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script>
  import ClickMeModal from '../components/ClickMeModal'

  export default {
    name: 'Homepage',
    components: {
      ClickMeModal
    },
    data() {
      return {

      }
    },
    props: {
      msg: String
    },
  }
</script>