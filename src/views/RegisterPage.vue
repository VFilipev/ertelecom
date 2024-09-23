<template lang="pug">
div.h-screen.flex.justify-center
  div(class="flex min-h-full flex-col justify-center w-96 px-6 py-12 lg:px-8")
    div(class="sm:mx-auto sm:w-full sm:max-w-sm")
      img(class="mx-auto h-10 w-auto" src="../assets/logo.png" alt="ERTelecom")
      h2.label Регистрация
    div(class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm")
      form(class="space-y-6 form" action="#" method="POST")
        div
          label.form__label(for="login") Логин
          div.mt-2
            input.form__input(v-model="newUser.name" id="login" name="login" type="login" autocomplete="login" required)
          label.form__label(for="mail") Почта
          div.mt-2
            input.form__input(v-model="newUser.mail" id="mail" name="mail" type="mail" autocomplete="mail" required)
          label.form__label(for="password") Пароль
          div.mt-2
            input.form__input(v-model="newUser.password" id="password" name="password" type="password" required)
          p(class="text-red-500" v-if="error") {{ error }}
        button.form__btn(@click="createUser" type="submit") Зарегистрироваться
      p(class="mt-10 text-center text-sm text-gray-500") Есть аккаунт?
        router-link.form__link(to="/login" tag="a") Авторизоваться
</template>
<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../store/auth.store'
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useAuthStore()
let newUser = ref({})
const createUser = () =>{
    console.log('Будет чуть позже');
}
</script>
<style scoped>
h2.label{
  @apply mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900
}
.form__input{
  @apply block w-full rounded-md border-0 py-1.5 pl-1 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6
}
.form__label{
  @apply block text-sm font-medium leading-6 text-gray-900
}
.form__link{
  @apply font-semibold leading-6 text-indigo-600 hover:text-indigo-500
}
.form__btn{
  @apply flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600
}

</style>
