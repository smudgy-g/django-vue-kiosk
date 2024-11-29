<template>
  <div class="flex flex-col h-full bg-white divide-y divide-gray-200">
    <div class="flex-1 h-0 overflow-y-auto">
      <div class="flex flex-col justify-between flex-1">
        <div class="divide-y divide-gray-200 sm:px-6">
          <div class="pt-6 pb-5 space-y-6">
            <VInput id="product-name" label="Product name" />
            <VInput id="product-code" label="Product code" />
            <VInput id="price" label="Price" type="number" />
            <VTextarea id="description" label="Description" />
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-end px-4 py-4 shrink-0">
      <button
        type="button"
        class="px-3 py-2 text-sm font-semibold text-gray-900 bg-white rounded-md shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"
        @click="$emit('close')"
      >
        Cancel
      </button>
      <button
        type="submit"
        class="inline-flex justify-center px-3 py-2 ml-4 text-sm font-semibold text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
      >
        Save
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import VInput from './VInput.vue'
import VTextarea from './VTextarea.vue'

defineEmits<{
  (e: 'close'): void
}>()
</script>
