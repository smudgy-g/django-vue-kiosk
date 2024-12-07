<template>
  <div>
    <label :for="id" class="block font-medium text-gray-900 text-sm/6"> {{ label }} </label>
    <div class="mt-2">
      <textarea
        :id="id"
        :name="id"
        rows="4"
        :value="value"
        class="px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm/6"
      />
    </div>
  </div>
</template>
<script setup lang="ts">
defineProps<{
  id: string
  label: string
  value?: string | number
}>()
</script>
