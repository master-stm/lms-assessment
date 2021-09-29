<template>
  <div>
    <q-card>
      <q-card-section>
        <div class="text-overline">Book ID: {{ book.bookID }}</div>
        <div class="text-overline">Title: {{ book.title }}</div>
        <div class="text-overline">Authors: {{ book.authors }}</div>
        <div class="text-overline">Language: {{ book.language_code }}</div>
      </q-card-section>
      <q-card-section>
        <div class="text-overline">Publisher: {{ book.publisher }}</div>
        <div class="text-overline">
          Publish date: {{ book.publication_date }}
        </div>
        <div class="text-overline">
          Number of pages: {{ book["  num_pages"] }}
        </div>
      </q-card-section>
      <q-card-section>
        <div class="text-overline">Ratings count: {{ book.ratings_count }}</div>
        <div class="text-overline">
          Average rating: {{ book.average_rating }}
        </div>
        <div class="text-overline">
          Text reviews: {{ book.text_reviews_count }}
        </div>
      </q-card-section>
      <q-card-section>
        <div class="text-overline">isbn: {{ book.isbn }}</div>
        <div class="text-overline">isnb13: {{ book.isbn13 }}</div>
      </q-card-section>
      <q-card-actions align="right">
        <q-btn flat label="OK" color="primary" v-close-popup />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  props: ["book"],
  data() {
    return {};
  },
};
</script>

<style scoped lang="scss">
</style>