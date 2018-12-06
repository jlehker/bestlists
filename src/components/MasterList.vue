<template>
  <v-list two-line subheader>
    <v-subheader inset>Master List</v-subheader>
    <v-divider inset></v-divider>

    <v-list-tile
      v-for="item in items"
      :key="item.title"
      avatar
      @click=""
    >
      <v-list-tile-avatar>
        <v-icon :class="[item.iconClass]">label_important</v-icon>
      </v-list-tile-avatar>

      <v-list-tile-content>
        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
        <v-list-tile-sub-title>{{ item.subtitle }}</v-list-tile-sub-title>
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
export default {
  data() {
    return {
      items: [
        {icon: 'folder', iconClass: 'red lighten-1', title: 'Take out the trash', subtitle: 'Jan 9, 2014'},
        {icon: 'folder', iconClass: 'blue lighten-1', title: 'Pay utility bill', subtitle: 'Jan 17, 2014'},
        {icon: 'folder', iconClass: 'green lighten-1', title: 'Profit', subtitle: 'Jan 28, 2014'},
      ],
    }
  }
};
</script>

<style>

</style>
