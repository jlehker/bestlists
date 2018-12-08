<template>
  <v-list two-line subheader>
    <v-subheader inset>Master List</v-subheader>
    <v-divider inset></v-divider>

    <v-list-tile
      v-for="item in items"
      :key="item.pub_id"
      avatar
      @click=""
    >
      <v-list-tile-avatar>
        <v-icon class="blue lighten-1">label_important</v-icon>
        <!--<v-icon :class="[item.iconClass]">label_important</v-icon>-->
      </v-list-tile-avatar>

      <v-list-tile-content>
        <v-list-tile-title>{{ item.description }}</v-list-tile-title>
        <v-list-tile-sub-title>{{ item.due_date }}</v-list-tile-sub-title>
      </v-list-tile-content>

      <v-list-tile-action>
        <v-btn icon ripple>
          <v-icon color="yellow darken-3">watch_later</v-icon>
        </v-btn>
      </v-list-tile-action>
      <v-list-tile-action>
        <v-btn icon ripple>
          <v-icon color="blue lighten-1">check_circle</v-icon>
        </v-btn>
      </v-list-tile-action>
    </v-list-tile>
  </v-list>
</template>
<script>
import axios from 'axios';

export default {
  data() {
    return {
      items: [{'description': 'ni', 'pub_id': 'nno', "due_date": 'caca'}],
    }
  },
 mounted(){
    this.getMasterList();
 },
  methods: {
    getMasterList: function () {
      axios.get("/api/lists")
        .then((response) => {
          this.items = response.data;
        })
    }
  }
};
</script>

<style>

</style>
