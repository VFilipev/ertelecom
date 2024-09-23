<template lang="pug">
div
  Loader(v-if="isLoadingStore.isLoading")
  div(v-else)
    Header
    TreeList(:items="cityList" @onClick="treeExpanded" @addItem="addItem" @update="update")
  TransitionRoot(appear :show="isOpen" as="template")
    Dialog(as="div" @close="closeModal" class="relative z-10")
      TransitionChild(as="template" enter="duration-300 ease-out" enter-from="opacity-0"
            enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100"
            leave-to="opacity-0")
        div(class="fixed inset-0 bg-black/25")
          div(class="fixed inset-0 overflow-y-auto")
            div(class="flex min-h-full items-center justify-center p-4 text-center")
              TransitionChild(as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95"
                enter-to="opacity-100 scale-100" leave="duration-200 ease-in"
                leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95")
                div(class="w-full max-w-md")
                  ItemForm(:typ="activeTyp" :item="activeItem" :isChange="isChange" @save="save")
</template>
<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import TreeList from "../components/TreeList.vue";
import ItemForm from "../components/ItemForm.vue";
import Header from "../components/Header.vue";
import "vue3-tree/dist/style.css";
import { City, URL, District } from "../api";
import Loader from "../components/Loader.vue";
import { useAuthStore, useIsLoadingStore } from "../store/auth.store";
import { TransitionRoot, TransitionChild, Dialog } from "@headlessui/vue";

let activeItem = ref({});
let activeTyp = ref("city");
let isOpen = ref(false);
let isChange = ref(false)
const addItem = (typ, par, change) => {

  activeTyp.value = typ;
  activeItem.value = par ? par : {};
  isChange.value = change
  isOpen.value = true;
};

const depthSearch = (arr) => {
  const result = [];
  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    if (element.nodes?.length > 0) {
      element.expanded = false;
      result.push(element);
      depthSearch(element.nodes);
    } else {
      element.expanded = false;
      result.push(element);
    }
  }
  return result;
};

const treeExpanded = (e) => {
  e.expanded = !e.expanded;
};

const closeModal = () => {
  activeItem.value = {}
  isOpen.value = false;
};

const save = () => {
  getList();
  isOpen.value = false;
};

const isLoadingStore = useIsLoadingStore();
const store = useAuthStore();
const router = useRouter();

let cityList = ref([]);
const getList = async () => {
  cityList.value = await City.getList();
  cityList.value = depthSearch(cityList.value);
};

const checkAuth = () => {
  isLoadingStore.set(true);
  setTimeout(() => {
    if (store.user.status === true) {
      getList();
      isLoadingStore.set(false);
    } else {
      router.push({ name: "login-page" });
    }
  }, 1000);
};

const update = () => {
  getList();
};

onMounted(() => {
  checkAuth()
});
</script>
<style>
h2 {
  font-family: "Montserrat", sans-serif;
  color: #172c5f;
}

.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100vh;
}
</style>
