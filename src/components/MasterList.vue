<template>
  <v-list two-line subheader>
    <v-subheader inset>Master List</v-subheader>
    <v-divider inset></v-divider>
    <ListItem
      v-for="(item, index) in items"
      v-bind:item="item"
      v-bind:index="index"
      v-bind:key="item.id"
      avatar
    ></ListItem>
  </v-list>
</template>

<script>
import axios from 'axios';
import ListItem from './ListItem';

export default {
  components: {
    ListItem,
  },
  data() {
    return {
      items: [{ description: 'ni', pub_id: 'nno', due_date: 'caca' }],
    };
  },
  beforeMount() {
    this.getMasterList();
  },
  methods: {
    getMasterList() {
      axios.get('/api/lists')
        .then((response) => {
          this.items = response.data;
        });
    },
  },
};
</script>

<style>

</style>
