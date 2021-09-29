<template>
  <q-page padding>
    <!-- content -->
    <div class="q-pa-md" style="padding-bottom: 220px">
      <div class="q-mt-md">
        <q-fab
          v-model="fab"
          label="Actions"
          vertical-actions-align="left"
          color="purple"
          icon="keyboard_arrow_down"
          direction="down"
        >
          <q-fab-action
            color="primary"
            @click="searchModal = true"
            icon="search"
            label="Search for a member"
          />
          <q-fab-action
            color="secondary"
            @click="createMemberModal = true"
            icon="person_add"
            label="Create Membership"
          />
        </q-fab>
        <q-btn color="primary" icon="check" label="OK" @click="logger" />
      </div>
    </div>
    <q-dialog v-model="createMemberModal" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Create a Membership</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input
            v-model="name"
            label="name"
            dense
            autofocus
            @keypress.enter="confirmMembership"
          />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn
            flat
            label="Create Membership"
            @click="confirmMembership"
            v-close-popup
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="confirmationModal">
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
            @click="createMembership"
            label="OK"
            color="primary"
            v-close-popup
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="searchModal" persistent>
      <q-card style="min-width: 350px">
        <q-card-section>
          <div class="text-h6">Member ID</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
          <q-input dense v-model="queryID" autofocus />
        </q-card-section>

        <q-card-actions align="right" class="text-primary">
          <q-btn flat label="Cancel" v-close-popup />
          <q-btn @click="handleSearch" flat label="Search" v-close-popup />
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-card
      v-if="member"
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
            <q-btn label="Add Balance" @click="handleAddBalance" />
            <q-separator spaced size="2px" vertical color="grey-4" />
            <q-btn label="Rent" @click="handleRent" />
            <q-separator spaced size="2px" vertical color="grey-4" />
            <q-btn label="Return" @click="handleReturn" />
          </q-btn-group>
        </q-card-actions>
      </div>
    </q-card>
  </q-page>
</template>

<script>
export default {
  name: "Members",

  data() {
    return {
      book: {},
      name: "",
      member: {},
      fab: true,
      createMemberModal: false,
      confirmationModal: false,
      searchModal: false,
      queryID: "",
      member: null,
      serverURL: "http://localhost:5000/",
      editedBook: {},
    };
  },
  methods: {
    logger,
    handleSearch() {
      fetch(this.serverURL + "get_member/" + this.queryID)
        .then((res) => res.json())
        .then((data) => {
          this.member = data;
        });
    },
    confirmMembership() {
      this.member = {
        id: Date.now(),
        name: this.name,
        points: 0,
        rentedBooks: "",
      };
      this.confirmationModal = true;
    },
    createMembership() {
      fetch(this.serverURL + "add_member", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.member),
      })
        .then(() => {
          this.$q.notify({
            message: "Member Created",
            position: "top",
            color: "secondary",
          });
          this.member = {};
        })
        .catch((err) => console.error(err));
    },
    onSubmit() {
      this.book.publication_date.toString();
      fetch(this.serverURL + "add_book", {
        method: "POST",
        headers: {
          "content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        body: JSON.stringify(this.book),
      })
        .then((res) => res.json())
        .then(() =>
          this.$q.notify({
            message: `added Book: ${this.book.title} - ID: ${this.book.bookID}`,
            position: "center",
            color: "info",
          })
        )
        .catch((err) => console.error(err));
    },
    handleRent() {
      this.$q
        .dialog({
          title: "Issue book rent",
          message: "Enter Book ID",
          prompt: {
            model: "",
            type: "number",
          },
          cancel: true,
          persistent: true,
        })
        .onOk((bookID) => {
          let id = bookID.toString();
          if (this.member.rentedBooks.length === 0 && this.member.points > 0) {
            this.member.rentedBooks = [id].join();
            --this.member.points;
          } else if (this.member.points > 0) {
            let arr = this.member.rentedBooks.split(",");
            arr.push(id);
            --this.member.points;
            this.member.rentedBooks = arr.join();
          } else {
            this.$q.notify({
              message: "something went wrong",
              color: "red",
            });
          }
          fetch(this.serverURL + "edit_member/" + this.member.id, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(this.member),
          }).catch((err) => console.error(err));

          fetch(this.serverURL + "get_book/" + bookID)
            .then((res) => res.json())
            .then((requestedBook) => {
              this.editedBook = requestedBook;
              --this.editedBook.quantity;

              fetch(this.serverURL + "update_book/" + bookID, {
                method: "PUT",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(this.editedBook),
              }).catch((err) => console.error(err));
            })
            .catch((err) => console.error(err));
        });
    },
    handleAddBalance() {
      this.$q
        .dialog({
          title: "Add balance",
          message: "How many points?",
          prompt: {
            model: "",
            type: "number", // optional
          },
          cancel: true,
          persistent: true,
        })
        .onOk((data) => {
          this.member.points = data;
          fetch(this.serverURL + "edit_member/" + this.member.id, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(this.member),
          }).catch((err) => console.error(err));
        });
    },
    handleReturn() {
      this.$q
        .dialog({
          title: "Issue book return",
          message: "Book ID",
          prompt: {
            model: "",
            type: "number", // optional
          },
          cancel: true,
          persistent: true,
        })
        .onOk((bookID) => {
          let arr = this.member.rentedBooks.split(",");
          if (arr.includes(bookID)) {
            for (var i = 0; i < arr.length; i++) {
              if (arr[i] === bookID) {
                arr.splice(i, 1);
              }
            }
            this.member.rentedBooks = arr.join();
            fetch(this.serverURL + "edit_member/" + this.member.id, {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify(this.member),
            }).catch((err) => console.error(err));
            fetch(this.serverURL + "get_book/" + bookID)
              .then((res) => res.json())
              .then((requestedBook) => {
                this.editedBook = requestedBook;
                ++this.editedBook.quantity;

                fetch(this.serverURL + "update_book/" + bookID, {
                  method: "PUT",
                  headers: {
                    "Content-Type": "application/json",
                  },
                  body: JSON.stringify(this.editedBook),
                }).catch((err) => console.error(err));
              })
              .catch((err) => console.error(err));
          } else {
            this.$q.notify({
              message: "enter a valid book id",
              color: "red",
            });
          }
        });
    },
  },
};
</script>
