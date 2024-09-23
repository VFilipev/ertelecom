<template lang="pug">
DialogPanel.dialog-panel
  DialogTitle(as="h3" class="text-lg font-medium leading-6 text-gray-900")
    span Удалить {{ getTitle[props.typ] }}
  div(class="mt-4 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6")
    div(class="sm:col-span-4")
      div Вы уверены что хотите удалить <b>{{ props.item.label }}</b> и все его содержимое?
  div.mt-4
    button.modal_btn(@click="deleteItem" type="button") Удалить {{ getTitle[props.typ] }}
</template>
<script setup>
import {
DialogPanel,
DialogTitle
} from '@headlessui/vue';
import axios from 'axios';
import { URL } from '../api';
import { getTitle } from './const';
const props = defineProps(['item', 'typ'])
const emit = defineEmits(['update'])
const deleteItem = async() => {
    let url = URL[props.typ]
    await axios.delete(url+props.item.id+'/',props.item)
    emit('update')
}
</script>
<style>
.modal_btn{
    @apply inline-flex justify-center rounded-md border border-transparent bg-red-100 px-4 py-2 text-sm font-medium text-black hover:bg-red-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-red-500 focus-visible:ring-offset-2
}
.dialog-panel{
    @apply w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all
}
</style>
