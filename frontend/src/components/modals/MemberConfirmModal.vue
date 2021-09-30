<template>
  <q-card style="min-width: 350px">
    <q-card-section>
      <div class="text-h6">Confirm</div>
    </q-card-section>
    <q-separator spaced inset vertical dark />
    <q-card-section class="q-pt-none">
      <p>ID: {{ member.id }}</p>
      <p>Name: {{ member.name }}</p>
      <p>Points: {{ member.points }}</p>
      <p>Rented books: none</p>
    </q-card-section>

    <q-card-actions align="right">
      <q-btn
        flat
        @click="$emit('create')"
        label="OK"
        color="primary"
        v-close-popup
      />
    </q-card-actions>
  </q-card>
</template>

<script>
export default {
  props: ["member"],
  data() {
    return {};
  },
};
</script>

<style scoped lang="scss">
</style>