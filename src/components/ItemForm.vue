<template lang="pug">
DialogPanel.dialog_panel
  DialogTitle.dialog_panel__title(as="h3")
    span Добавить {{ getTitle[props.typ] }}
    span.ml-1(v-if="props.item.id") в {{ props.item.label }}
  div(class="mt-6 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6")
    div(class="sm:col-span-4")
      label.dialog_panel__label(for="username") Название
      div.mt-2
        div.dialog_panel__wraper_input
          input.dialog_panel__input(v-model="obj.label" type="text" name="username" id="username" autocomplete="username" :placeholder="getPlaceholder[props.typ]")
  div.mt-4
    button.dialog_panel__btn(type="button" @click="save") Сохранить
</template>
<script setup>
import axios from 'axios'
import {
DialogPanel,
DialogTitle
} from '@headlessui/vue';
import { defineEmits, ref, onMounted } from 'vue';
import { URL } from '../api';
import { getTitle, getParent, getPlaceholder } from './const'
const props = defineProps(['typ', 'item', 'isChange'])
const emit = defineEmits(['save'])
let obj = ref({})
const save = async () => {
  let url = URL[props.typ]
  if(props.item.id && props.isChange == false ){ obj.value[getParent[props.typ]] =  props.item.id}
  if(props.isChange == true){
      await axios.patch(url+obj.value.id+'/',obj.value)
    }else{
      await axios.post(url,obj.value)
    }

  emit('save')
}
onMounted(() => {
  if(props.isChange == true){ obj.value = {...props.item} }
})
</script>
<style>
.dialog_panel{
  @apply w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all
}
.dialog_panel__title{
  @apply text-lg font-medium leading-6 text-gray-900
}
.dialog_panel__btn{
  @apply inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2
}
.dialog_panel__input{
  @apply block flex-1 border-0 bg-transparent py-1.5 pl-1 text-gray-900 placeholder:text-gray-400 focus:ring-0 sm:text-sm sm:leading-6
}
.dialog_panel__label{
  @apply block text-sm font-medium leading-6 text-gray-900
}
.dialog_panel__wraper_input{
  @apply flex rounded-md shadow-sm ring-1 ring-inset ring-gray-300 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-600 sm:max-w-md
}
</style>
