<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
  <div class="flex flex-col justify-center flex-1 min-h-full py-12 sm:px-6 lg:px-8">
    <div class="text-center sm:mx-auto sm:w-full sm:max-w-md">
      <p class="text-4xl italic font-semibold text-blue-600">Kiosk</p>
      <h2 class="mt-6 font-bold tracking-tight text-gray-900 text-2xl/9">
        Sign in to your account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
      <div class="px-6 py-12 bg-white shadow sm:rounded-lg sm:px-12">
        <form class="space-y-6" @submit.prevent="handleLogin">
          <VInput id="username" label="Username" v-model="form.username" autocomplete="username" />
          <VInput
            id="password"
            type="password"
            label="Password"
            v-model="form.password"
            autocomplete="password"
          />

          <div class="flex justify-end">
            <div class="text-sm/6">
              <a href="#" class="font-semibold text-blue-600 hover:text-blue-500">
                Forgot password?
              </a>
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="flex w-full justify-center rounded-md bg-blue-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
            >
              Sign in
            </button>
          </div>
        </form>
      </div>

      <p class="mt-10 text-center text-gray-500 text-sm/6">
        Not a member?
        {{ ' ' }}
        <a href="/register" class="font-semibold text-blue-600 hover:text-blue-500">
          Register now
        </a>
      </p>
    </div>
  </div>
</template>
<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useCustomFetch } from '@/composables/useCustomFetch'
import VInput from '@/components/VInput.vue'
import { reactive } from 'vue'

const route = useRoute()
const router = useRouter()
const { removeToken, setToken } = useAuthStore()

const form = reactive({
  username: '',
  password: '',
})

async function handleLogin() {
  removeToken()
  const { data } = await useCustomFetch('/api/v1/auth/token/login/').post(form).json()

  console.log(data.value)

  const token = data.value?.auth_token
  setToken(token)
  localStorage.setItem('token', token)

  const toPath = route.meta.to || '/portal/dashboard'
  router.push(toPath)
}
</script>
