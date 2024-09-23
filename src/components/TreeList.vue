<template lang="pug">
div.tree-wrapper
    ul.tree-list
        li.tree-row(v-for="city in props.items")
          div.tree-row-item(@click="$emit('onClick', city)")
              div
                  span.tree-row-txt {{ city.label }}
                  span.ml-5px(v-if="city.nodes.length > 0") {{ city.nodes.length }}
              div.flex
                IconEdit(@click.stop="$emit('addItem', 'city', city, true)")
                IconDelete(@click.stop="deleteItem(city, 'city')")
                IconPlus(@click.stop="$emit('addItem', 'district', city, false)")
          ul.tree-list(v-if="city.nodes.length > 0 && city.expanded")
            li.tree-row.pl-6(v-for="district in city.nodes")
              div.tree-row-item(@click="$emit('onClick', district)")
                  div
                      span.tree-row-txt {{ district.label }}
                      span.ml-5px(v-if="district.nodes.length > 0") {{ district.nodes.length }}
                  div.flex
                    IconEdit(@click.stop="$emit('addItem', 'district', district, true)")
                    IconDelete(@click.stop="deleteItem(district, 'district')")
                    IconPlus(@click.stop="$emit('addItem', 'street', district, false)")
              ul.tree-list(v-if="district.nodes.length > 0 && district.expanded")
                li.tree-row.pl-6(v-for="street in district.nodes")
                  div.tree-row-item(@click="$emit('onClick', street)")
                    div
                        span.tree-row-txt {{ street.label }}
                        span.ml-5px(v-if="street.nodes?.length > 0") {{ street.nodes?.length  }}
                    div.flex
                        IconEdit
                        IconDelete(@click.stop="deleteItem(street, 'street')")
                        IconPlus(@click.stop="$emit('addItem', 'house', street, false)")
                  ul.tree-list(v-if="street.nodes?.length > 0 && street.expanded")
                    li.tree-row.pl-6(v-for="house in street.nodes")
                      div.tree-row-item(@click="$emit('onClick', house)")
                        div
                          span.tree-row-txt {{ house.label }}
                          span.ml-5px(v-if="house.nodes?.length > 0") {{ house.nodes?.length }}
                        .flex
                          IconEdit
                          IconDelete(@click.stop="deleteItem(house, 'house')")
                          IconPlus(@click.stop="$emit('addItem', 'entrance', house, false)")
                      ul.tree-list(v-if="house.nodes?.length > 0 && house.expanded")
                        li.tree-row.pl-6(v-for="entrance in house.nodes")
                          div.tree-row-item(@click="isOpenModal = true")
                              span.tree-row-txt {{ entrance.label }}
    TransitionRoot(appear :show="isOpenModal" as="template")
        Dialog.relative.z-10(as="div" @close="closeModal")
            TransitionChild(as="template" enter="duration-300 ease-out" enter-from="opacity-0"
                enter-to="opacity-100" leave="duration-200 ease-in" leave-from="opacity-100" leave-to="opacity-0")
              div(class="fixed inset-0 bg-black/25")
            div.fixed.inset-0.overflow-y-auto
                div.flex.min-h-full.items-center.justify-center.p-4.text-center
                    TransitionChild(as="template" enter="duration-300 ease-out" enter-from="opacity-0 scale-95"
                        enter-to="opacity-100 scale-100" leave="duration-200 ease-in"
                        leave-from="opacity-100 scale-100" leave-to="opacity-0 scale-95")
                        div.w-full.max-w-md
                            ModalDelete(v-if="activeItem.id" @update="update" :item="activeItem" :typ="activeTyp")
                            ModalTable(v-else)
    Hotkey(:keys="['ctrl', 'n']" @hotkey="$emit('addItem', 'city')")
        button.tree_btn_add(@click="$emit('addItem', 'city')") Добавить город
</template>
<script setup>
import { Dialog, TransitionChild, TransitionRoot } from "@headlessui/vue";
import { Hotkey } from "@simolation/vue-hotkey";
import { ref } from "vue";
import IconDelete from "./icon/IconDelete.vue";
import IconPlus from "./icon/IconPlus.vue";
import IconEdit from './icon/IconEdit.vue'
import ModalDelete from "./ModalDelete.vue";
import ModalTable from "./ModalTable.vue";
const emit = defineEmits(["update"]);
const activeItem = ref({});
const activeTyp = ref({});
const isOpenModal = ref(false);
const update = () => {
  closeModal();
  emit("update");
};
const closeModal = () => {
  isOpenModal.value = false;
};
const props = defineProps(["items"]);
const deleteItem = async (city, typ) => {
  activeItem.value = city;
  activeTyp.value = typ;
  isOpenModal.value = true;
};
</script>
<style>
.tree_btn_add {
  @apply bg-transparent py-2 px-2.5 border bc-main rounded;
}
.ml-5px {
  margin-left: 5px;
}
ul.tree-list {
  gap: 10px;
}
li.tree-row {
  gap: 10px;
}
.bc-main {
  border-color: #172c5f;
}
ul.tree-list li.tree-row{
  padding-left: 24px;
}
.tree-wrapper {
  font-family: "Montserrat", sans-serif;
  color: #172c5f;
}

.tree-row-item:hover {
  background-color: #172b5f0f;
}

.tree-row-item:hover {
  cursor: pointer;
}

.tree-row-item {
  display: flex;
  justify-content: space-between;
}
</style>
