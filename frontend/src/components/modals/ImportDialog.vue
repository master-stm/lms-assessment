<template>
  <q-dialog persistent>
    <q-card class="my-card">
      <q-card-section>
        <q-input type="number" label="Quantity" min="0" />
      </q-card-section>
      <q-card-actions align="right" class="text-primary">
        <q-btn flat label="Import" v-close-popup />
        <q-btn flat label="Cancel" v-close-popup />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style scoped lang="scss">
</style>