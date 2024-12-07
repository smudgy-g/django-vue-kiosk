<template>
  <div class="py-12 sm:px-6 lg:px-8">
    <VCard class="mx-auto sm:max-w-2xl">
      <form @submit.prevent="handleFormSubmit">
        <div class="space-y-12">
          <div class="pb-12 border-b border-gray-900/10">
            <h2 class="font-semibold text-gray-900 text-base/7">Profile</h2>
            <p class="mt-1 text-gray-600 text-sm/6">
              This information will be used when sending orders to suppliers.
            </p>
            <div class="grid grid-cols-1 mt-10 gap-x-6 gap-y-8 sm:grid-cols-6">
              <VInput
                class="sm:col-span-3"
                id="firstName"
                label="First name"
                autocomplete="first-name"
                v-model="form.firstName"
              />
              <VInput
                class="sm:col-span-3"
                id="lastName"
                label="Last name"
                autocomplete="last-name"
                v-model="form.lastName"
              />
              <VInput
                class="sm:col-span-3"
                id="username"
                label="Username"
                autocomplete="username"
                v-model="form.username"
              />
              <VInput
                class="sm:col-span-3"
                id="email"
                label="Email address"
                type="email"
                autocomplete="email"
                v-model="form.email"
              />
              <VInput
                class="sm:col-span-3"
                id="password"
                label="Password"
                type="password"
                v-model="form.password"
              />
              <VInput
                class="sm:col-span-3"
                id="confirmPassword"
                label="Confirm password"
                type="password"
                v-model="form.confirmPassword"
              />
            </div>
          </div>
          <div class="pb-12 border-b border-gray-900/10">
            <h2 class="font-semibold text-gray-900 text-base/7">Company Information</h2>
            <p class="mt-1 text-gray-600 text-sm/6">
              Use a permanent address where you can receive mail.
            </p>
            <div class="grid grid-cols-1 mt-10 gap-x-6 gap-y-8 sm:grid-cols-6">
              <VInput
                class="sm:col-span-full"
                id="company"
                label="Company name"
                autocomplete="organization"
                v-model="form.company"
              />
              <VInput
                class="sm:col-span-full"
                id="street"
                label="Street address"
                autocomplete="street-address"
                v-model="form.street"
              />
              <VInput
                class="sm:col-span-2 sm:col-start-1"
                id="city"
                label="City"
                autocomplete="address-level2"
                v-model="form.city"
              />
              <VInput
                class="sm:col-span-2"
                id="region"
                label="State / Province"
                autocomplete="address-level1"
                v-model="form.region"
              />

              <VInput
                class="sm:col-span-2"
                id="zip"
                label="ZIP / Postal code"
                autocomplete="postal-code"
                v-model="form.zip"
              />
            </div>
          </div>
        </div>
        <div class="flex items-center justify-end mt-6 gap-x-6">
          <VButton :variant="Variant.Link" to="/">Cancel</VButton>
          <VButton type="submit">Save</VButton>
          <!-- :disabled="!isFormValid" -->
        </div>
      </form>
    </VCard>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import * as yup from 'yup'
import VCard from '@/components/VCard.vue'
import VInput from '@/components/VInput.vue'
import VButton from '@/components/VButton.vue'
import { Variant } from '@/enums'
import { useCustomFetch } from '@/composables/useCustomFetch'

const schema = yup.object().shape({
  firstName: yup.string().required(),
  lastName: yup.string().required(),
  username: yup.string().required(),
  email: yup.string().email().required(),
  password: yup.string().required(),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref('password')], 'Passwords must match')
    .required(),
  company: yup.string().required(),
  street: yup.string().required(),
  city: yup.string().required(),
  region: yup.string().required(),
  zip: yup.string().required(),
})

const form = reactive<yup.InferType<typeof schema>>({
  firstName: '',
  lastName: '',
  email: '',
  username: '',
  password: '',
  confirmPassword: '',
  company: '',
  street: '',
  city: '',
  region: '',
  zip: '',
})

// const isFormValid = computed(() => {
//   return Object.values(form).every((value) => value !== null && value !== undefined && value !== '')
// })

async function handleFormSubmit() {
  try {
    await schema.validate(form, { abortEarly: false }) // Validate all fields
    console.log('Form is valid:', form)
    const { data } = await useCustomFetch('/api/v1/auth/users/').post(form).json()
  } catch (error) {
    if (error instanceof yup.ValidationError) {
      console.dir(error.inner) // Logs detailed error information for all fields
    }
  }
}
</script>
