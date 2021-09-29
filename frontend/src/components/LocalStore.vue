<template>
  <q-banner class="bg-white text-secondary">
    <q-item v-ripple class="text-dark">
      <q-item-section>Book ID</q-item-section>
      <q-item-section>Title</q-item-section>
      <q-item-section>Quantity</q-item-section>
      <q-item-section>Actions</q-item-section>
    </q-item>
    <q-separator spaced inset vertical dark />
    <q-list bordered separator>
      <q-item v-for="book in booksArray" class="row" :key="book.bookID">
        <q-item-section class="col-md-3">
          {{ book.bookID }}
        </q-item-section>
        <q-item-section class="col-md-3">{{ book.title }}</q-item-section>
        <q-item-section class="col-md-2">{{ book.quantity }}</q-item-section>
        <q-item-section class="col-md-2" side>
          <div class="row justify-end">
            <q-btn
              class="col-md-5"
              color="primary"
              flat
              label="more..."
              @click="moreClick(book)"
            />
          </div>
        </q-item-section>
      </q-item>
    </q-list>
    <q-dialog v-model="showBookInfo" persistent>
      <BookInfoModal :book="book" />
    </q-dialog>
  </q-banner>
</template>

<script>
import BookInfoModal from "../components/BookInfoModal.vue";
import { getAllData } from "../functions/fetchers";
export default {
  name: "Local Store",
  components: { BookInfoModal },
  data() {
    return {
      booksArray: [],
      book: "",
      showBookInfo: false,
      serverURL: "http://localhost:5000/",
    };
  },
  methods: {
    getAllData,
    async getBook() {
      this.booksArray = await this.getAllData(this.serverURL + "get_books");
    },
    moreClick(book) {
      this.book = book;
      this.showBookInfo = true;
    },
  },
  created() {
    this.getBook();
  },
};
</script>
