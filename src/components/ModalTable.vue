<template lang="pug">
DialogPanel.dialog-panel
  DialogTitle(as="h3" class="text-lg font-medium leading-6 text-gray-900")
    span Оборудование
  div(class="mt-4")
    table.w-full.border-collapse.border.border-slate-500
      thead
        th.border-collapse.border.border-slate-500 id
        th.border-collapse.border.border-slate-500 name
        th.border-collapse.border.border-slate-500 q
      tbody
        td.border-collapse.border.border-slate-500 1
        td.border-collapse.border.border-slate-500 Свитч
        td.border-collapse.border.border-slate-500 13
</template>
<script setup>
import {
DialogPanel,
DialogTitle
} from '@headlessui/vue';
</script>
