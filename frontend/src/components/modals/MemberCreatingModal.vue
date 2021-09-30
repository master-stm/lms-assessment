<template>
  <q-card style="min-width: 350px">
    <q-card-section>
      <div class="text-h6">Create a Membership</div>
    </q-card-section>

    <q-card-section class="q-pt-none">
      <q-input v-model="name" label="name" dense autofocus />
    </q-card-section>

    <q-card-actions align="right" class="text-primary">
      <q-btn flat label="Cancel" v-close-popup />
      <q-btn
        flat
        label="Create Membership"
        @click="$emit('confirm', name)"
        v-close-popup
      />
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  data() {
    return {
      name: "",
    };
  },
};
</script>

<style scoped lang="scss">
</style>