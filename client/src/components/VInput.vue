<template>
  <div>
    <label :for="id" class="block font-medium text-gray-900 text-sm/6"> {{ label }} </label>

    <input
      :name="id"
      :id="id"
      :type="type"
      :step="step"
      :min="setMin"
      :max="setMax"
      :disabled="disabled"
      :value="value"
      class="relative px-2 mt-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm/6"
    />
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    id: string
    label: string
    value: string | number
    type?: 'number' | 'text' | 'date'
    step?: number
    min?: number
    max?: number
    disabled?: boolean
  }>(),
  {
    type: 'text',
    step: 0.01,
    min: 0,
    disabled: false,
  },
)

const setMin = computed(() => {
  if (props.type === 'date' || props.type === 'number') {
    return props.min != null ? props.min : 0
  }

  return undefined
})

const setMax = computed(() => {
  if (props.type === 'number') {
    return props.max != null ? props.max : 9999999
  }

  if (props.type === 'date') {
    return props.max != null ? props.max : undefined
  }

  return undefined
})
</script>
