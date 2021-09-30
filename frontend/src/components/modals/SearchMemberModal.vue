<template>
  <q-card style="min-width: 350px">
    <q-card-section>
      <div class="text-h6">Member ID</div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <q-input type="number" dense v-model="queryID" autofocus />
    </q-card-section>

    <q-card-actions align="right" class="text-primary">
      <q-btn flat label="Cancel" v-close-popup />
      <q-btn
        @click="$emit('search', queryID)"
        flat
        label="Search"
        v-close-popup
      />
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  data() {
    return {
      queryID: null,
    };
  },
};
</script>

<style scoped lang="scss">
</style>