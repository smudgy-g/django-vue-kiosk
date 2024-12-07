import { useAuthStore } from '@/stores/auth'
import { createFetch } from '@vueuse/core'

export const useCustomFetch = createFetch({
  baseUrl: import.meta.env.VITE_SERVER_BASE_URL,
  options: {
    async beforeFetch({ options }) {
      const { token } = useAuthStore()
      options.headers.Authorization = `Bearer ${token}`

      return { options }
    },
  },
  fetchOptions: {
    mode: 'cors',
  },
})
