<template>
  <div>
    <q-banner class="bg-white text-secondary" style="height: 75vh">
      <q-item v-ripple class="text-dark">
        <q-item-section>Book ID</q-item-section>
        <q-item-section>Title</q-item-section>
        <q-item-section>Actions</q-item-section>
      </q-item>
      <q-separator spaced inset vertical dark />
      <q-list bordered separator>
        <q-item
          v-for="book in booksArray.slice(startIndex, endIndex)"
          class="row"
          :key="book.bookID"
        >
          <q-item-section class="col-md-3">
            {{ book.bookID }}
          </q-item-section>
          <q-item-section class="col-md-3">{{ book.title }}</q-item-section>
          <q-item-section class="col-md-3" side>
            <div class="row justify-end">
              <q-btn
                class="col-md-5"
                color="primary"
                flat
                label="more..."
                @click="moreClick(book)"
              />
              <q-btn
                class="col-md-5"
                color="primary"
                flat
                label="Import Book"
                @click="importClick(book)"
              />
            </div>
          </q-item-section>
        </q-item>
      </q-list>
      <div class="q-pa-lg flex flex-center">
        <q-btn-group unelevated>
          <q-btn
            :disable="startIndex === 0"
            label="prev"
            @click="navigatePrev"
          />
          <q-separator space size="5em" vertical dark />
          <q-btn
            :disable="endIndex === booksArray.length"
            label="next"
            @click="navigateNext"
          />
        </q-btn-group>
      </div>
    </q-banner>
    <q-dialog v-model="showMoreDialog"
      ><BookInfoModal :book="bookToImport"
    /></q-dialog>
    <q-dialog v-model="showImportDialog" persistent>
      <q-card class="my-card">
        <q-card-section>
          <q-input v-model="quantity" type="number" label="Quantity" min="0" />
        </q-card-section>
        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Import" v-close-popup @click="handelImport" />
          <q-btn flat label="Cancel" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import BookInfoModal from "../components/BookInfoModal.vue";
import { getAllData } from "../functions/fetchers";
export default {
  name: "General Store",
  components: { BookInfoModal },
  data() {
    return {
      booksArray: [],
      bookToImport: {},
      showMoreDialog: false,
      showImportDialog: false,
      quantity: 1,
      startIndex: 0,
      endIndex: 5,
    };
  },
  methods: {
    getAllData,
    moreClick(book) {
      this.showMoreDialog = true;
      this.bookToImport = book;
    },
    importClick(book) {
      this.showImportDialog = true;
      this.bookToImport = book;
    },
    handelImport() {
      this.bookToImport.quantity = this.quantity;
      this.bookToImport.rented = "no";

      fetch("http://localhost:5000/add_book", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.bookToImport),
      })
        .then(() => {
          this.$q.notify({
            message: `Book ID: ${this.bookToImport.bookID} imported`,
            position: "center",
            color: "primary",
          });
          this.bookToImport = {};
        })
        .catch((err) => console.error(err));
    },
    navigatePrev() {
      this.startIndex = this.startIndex - 5;
      this.endIndex = this.endIndex - 5;
    },
    navigateNext() {
      this.startIndex = this.startIndex + 5;
      this.endIndex = this.endIndex + 5;
    },
  },

  async created() {
    this.booksArray = await getAllData("http://localhost:3000/message");
  },
};
</script>
