import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const isAuthenticated = ref<boolean>(false)
  const token = ref<string | null>(null)

  function initialiseStore() {
    if (localStorage.getItem('token')) {
      token.value = localStorage.getItem('token')
      isAuthenticated.value = true
    } else {
      token.value = null
      isAuthenticated.value = false
    }
  }

  function setToken(value: string) {
    token.value = value
    isAuthenticated.value = true
  }
  function removeToken() {
    token.value = null
    isAuthenticated.value = false
  }

  return { isAuthenticated, token, setToken, removeToken, initialiseStore }
})
