<template lang="pug">
Hotkey(:keys="['ctrl', 'e']" @hotkey="signOut")
  header.pt-5.pb-5
    .container
      .flex.justify-between.items-center
        img(class="w-1/6" src="../assets/logo.png")
        div(class="flex pr-2.5")
          div {{ store.user.name }}
          svg(@click="signOut" class="hover:cursor-pointer" xmlns="http://www.w3.org/2000/svg" fill="none" width="24" height="24" viewBox="0 0 24 24" stroke="#172c5f" className="size-6")
            path(strokeLinecap="round" strokeLinejoin="round" stroke="#172c5f" d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15")
</template>
<script setup>
import { Hotkey } from "@simolation/vue-hotkey";
import { useAuthStore, useIsLoadingStore } from '../store/auth.store'
import { useRouter } from "vue-router";

const router = useRouter()
const store = useAuthStore()
const isLoadingStore = useIsLoadingStore();

const signOut = () => {
  isLoadingStore.set(true);
  setTimeout(() => {
    isLoadingStore.set(false);
    store.clear();
    router.push({ name: "login-page" });
  }, 1000);
};
</script>
