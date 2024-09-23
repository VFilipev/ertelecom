<template lang="pug">
div.h-screen.flex.justify-center
  div(class="flex w-96 min-h-full flex-col justify-center px-6 py-12 lg:px-8")
    div(class="sm:mx-auto sm:w-full sm:max-w-sm")
      img(class="mx-auto h-10 w-auto" src="../assets/logo.png" alt="ERTelecom")
      h2.label Авторизуйтесь в системе
    div(class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm")
      form.form(class="space-y-6" action="#" method="POST")
        div
          label.form__label(for="login") Логин
          div.mt-2
            input.form__input(v-model="newUser.name" id="login" name="login" type="login" autocomplete="login" required )
          label.form__label(for="password") Пароль
          div.mt-2
            input.form__input(v-model="newUser.password" id="password" name="password" type="password" required )
          p(style="color: red;" v-if="error") {{ error }}
        button.form_btn(@click="createUser" type="submit") Войти
      p(class="mt-10 text-center text-sm text-gray-500") Нет аккаунта?
        router-link.form__link(to="/register" tag="a") Зарегистрироваться
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../store/auth.store'
import { useRouter } from 'vue-router';
import axios from 'axios'
import HomePage from './HomePage.vue';
const store = useAuthStore()

let newUser = ref({})
let error = ref('')
const router = useRouter()

const createUser = async (e) => {
    e.preventDefault();
    let form = new FormData()
    form.append('username', newUser.value.name)
    form.append('password', newUser.value.password)
    try {
        await axios.post('api-token-auth/', form)
        store.set({ ...newUser.value, 'status': true })
        router.push({ name: 'home-page' })
    } catch (e) {
        error.value = e.response.data
        setTimeout(()=>error.value = '', 2000)
    }
}
const signOut = () => {
    store.clear()
}
const checkAuth = ()=>{
    console.log(store.user.status);
    if(store.user.status == true){router.push({ name: 'home-page' })}
}
onMounted(() => {
    checkAuth()
})
</script>
<style>
.form_btn{
  @apply flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600
}
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
</style>

