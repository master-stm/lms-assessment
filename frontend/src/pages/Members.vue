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
      </div>
    </div>

    <q-dialog v-model="createMemberModal" persistent>
      <MemberCreatingModal @confirm="confirmMembership" />
    </q-dialog>

    <q-dialog v-model="confirmationModal">
      <MemberConfirmModal :member="newMember" @create="createMembership" />
    </q-dialog>

    <q-dialog v-model="searchModal" persistent>
      <SearchMemberModal @search="handleSearch" />
    </q-dialog>

    <MemberInfoCard
      v-if="member"
      :member="member"
      @addBalance="handleAddBalance"
      @rent="handleRent"
      @return="handleReturn"
    />
  </q-page>
</template>

<script>
import MemberCreatingModal from "../components/modals/MemberCreatingModal.vue";
import MemberConfirmModal from "../components/modals/MemberConfirmModal.vue";
import SearchMemberModal from "../components/modals/SearchMemberModal.vue";
import MemberInfoCard from "../components/MemberInfoCard.vue";
import { getData, addData, editData } from "../functions/fetchers";
export default {
  name: "Members",
  components: {
    MemberCreatingModal,
    MemberConfirmModal,
    SearchMemberModal,
    MemberInfoCard,
  },
  data() {
    return {
      book: {},
      member: {},
      newMember: {},
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
    getData,
    addData,
    editData,
    async handleSearch(queryID) {
      try {
        this.member = await this.getData(
          this.serverURL + "get_member/" + queryID
        );
      } catch (error) {
        console.error(error);
      }
    },
    confirmMembership(name) {
      this.newMember = {
        id: Date.now(),
        name,
        points: 0,
        rentedBooks: "",
      };
      this.confirmationModal = true;
    },
    async createMembership() {
      try {
        await this.addData(this.serverURL + "add_member", this.newMember);

        this.$q.notify({
          message: "Member Created with ID " + this.newMember.id,
          position: "top",
          color: "secondary",
        });
        this.newMember = {};
      } catch (error) {
        console.error(error);
      }
    },

    async handleRent() {
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
        .onOk(async (bookID) => {
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
          await this.editData(
            this.serverURL + "edit_member/" + this.member.id,
            this.member
          );

          let requestedBook = await this.getData(
            this.serverURL + "get_book/" + bookID
          );

          requestedBook.quantity--;
          await this.editData(
            this.serverURL + "update_book/" + bookID,
            requestedBook
          );
        });
    },
    handleAddBalance() {
      this.$q
        .dialog({
          title: "Add balance",
          message: "How many points?",
          prompt: {
            model: "",
            type: "number",
          },
          cancel: true,
          persistent: true,
        })
        .onOk((data) => {
          this.member.points += parseInt(data);
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
            type: "number",
          },
          cancel: true,
          persistent: true,
        })
        .onOk(async (bookID) => {
          let arr = this.member.rentedBooks.split(",");
          if (arr.includes(bookID)) {
            for (var i = 0; i < arr.length; i++) {
              if (arr[i] === bookID) {
                arr.splice(i, 1);
              }
            }
            this.member.rentedBooks = arr.join();
            await this.editData(
              this.serverURL + "edit_member/" + this.member.id,
              this.member
            );

            let requestedBook = await this.getData(
              this.serverURL + "get_book/" + bookID
            );
            requestedBook.quantity++;
            await this.editData(
              this.serverURL + "update_book/" + bookID,
              requestedBook
            );
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
