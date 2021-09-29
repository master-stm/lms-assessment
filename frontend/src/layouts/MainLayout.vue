<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-toolbar-title> Library Management System </q-toolbar-title>
      </q-toolbar>
      <q-btn-group unelevated style="margin-left: 35%">
        <q-btn label="Books" icon="auto_stories" to="/" />
        <q-separator size="20em" spaced vertical style="opacity: 0" />
        <q-btn label="Members" icon="people_alt" to="members" />
      </q-btn-group>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "MainLayout",

  data() {
    return {};
  },
};
</script>
