<template>
  <q-page padding>
    <q-tabs class="row justify-around" v-model="currentTab">
      <q-tab
        v-for="tab in tabsArray"
        :key="tab.label"
        class="col-md-3"
        :name="tab.name"
        :label="tab.label"
      />
    </q-tabs>
    <q-separator />

    <q-tab-panels v-model="currentTab" animated>
      <q-tab-panel v-for="(tab, i) in tabsArray" :key="i" :name="tab.name">
        <keep-alive>
          <component :is="currentTab" ref="component" />
        </keep-alive>
      </q-tab-panel>
    </q-tab-panels>
  </q-page>
</template>

<script>
import LocalStore from "../components/LocalStore.vue";
import GeneralStore from "../components/GeneralStore.vue";
export default {
  name: "Books",
  components: {
    "general store": GeneralStore,
    "local store": LocalStore,
  },
  data() {
    return {
      currentTab: "general store",
      tabsArray: [
        {
          name: "general store",
          label: "General Store",
        },
        {
          name: "local store",
          label: "Local Store",
        },
      ],
    };
  },
};
</script>
