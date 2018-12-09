<template>
    <v-list-tile>

      <v-list-tile-avatar>
        <v-icon class="blue lighten-1">label_important</v-icon>
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
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
    },
  },
};
</script>

<style scoped>

</style>
