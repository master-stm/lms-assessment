<template>
  <q-card
    flat
    bordered
    class="my-card bg-grey-1 absolute-center"
    style="width: auto"
  >
    <div class="center">
      <q-card-section>
        <div class="row items-center no-wrap">
          <div class="col">
            <div class="text-h4">{{ member.name }}</div>
            <div class="text-subtitle1">ID: {{ member.id }}</div>
          </div>
        </div>
      </q-card-section>
      <q-card-section horizontal>
        <div style="margin-left: 2em" class="row items-center no-wrap">
          <div class="col">
            <p><strong>Points: </strong>{{ member.points }}</p>
            <p><strong>Rented Books: </strong>{{ member.rentedBooks }}</p>
          </div>
        </div>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-btn-group flat>
          <q-btn label="Add Balance" @click="$emit('addBalance')" />
          <q-separator spaced size="2px" vertical color="grey-4" />
          <q-btn label="Rent" @click="$emit('rent')" />
          <q-separator spaced size="2px" vertical color="grey-4" />
          <q-btn label="Return" @click="$emit('return')" />
        </q-btn-group>
      </q-card-actions>
    </div>
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