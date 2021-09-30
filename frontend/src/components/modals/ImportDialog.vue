<template>
  <q-card class="my-card">
    <q-card-section>
      <q-input v-model="quantity" type="number" label="Quantity" min="1" />
    </q-card-section>
    <q-card-actions align="right" class="text-primary">
      <q-btn
        flat
        label="Import"
        v-close-popup
        @click="$emit('importBook', quantity)"
      />
      <q-btn flat label="Cancel" v-close-popup />
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  data() {
    return {
      quantity: 1,
    };
  },
};
</script>

<style scoped lang="scss">
</style>