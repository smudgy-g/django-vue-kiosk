<template>
  <div>
    <label :for="id" class="block font-medium text-gray-900 text-sm/6"> {{ label }} </label>

    <select
      :name="id"
      :id="id"
      :disabled="disabled"
      :value="value"
      class="relative px-2 mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm/6"
    >
      <option v-for="option in options" :key="option.value" :value="option.value">
        {{ option.label }}
      </option>
    </select>
  </div>
</template>

<script setup lang="ts">
import type { Option } from '@/types'

withDefaults(
  defineProps<{
    id: string
    label: string
    value: Option<any>
    options: Array<Option<string>>
    disabled?: boolean
  }>(),
  {
    disabled: false,
  },
)
</script>
