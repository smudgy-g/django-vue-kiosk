<template>
  <form
    class="flex flex-col h-full bg-white divide-y divide-gray-200"
    @submit.prevent="handleSubmit"
  >
    <div class="flex-1 h-0 overflow-y-auto">
      <div class="flex flex-col justify-between flex-1">
        <div class="divide-y divide-gray-200 sm:px-6">
          <div class="pt-6 pb-5 space-y-6">
            <VSelect
              id="supplier"
              label="Supplier"
              :value="form.supplier"
              :disabled="mode === 'view'"
              :options="supplierList"
            />
            <VInput
              id="product-name"
              label="Product name"
              :value="form.productName"
              :disabled="mode === 'view'"
            />
            <VInput
              id="product-code"
              label="Product code"
              :value="form.productCode"
              :disabled="mode === 'view'"
            />
            <VInput
              id="price"
              label="Price"
              type="number"
              :value="form.price"
              :disabled="mode === 'view'"
            />
            <VTextarea
              id="description"
              label="Description"
              :value="form.description"
              :disabled="mode === 'view'"
            />
          </div>
        </div>
      </div>
    </div>
    <div v-if="mode === 'edit'" class="flex justify-end px-4 py-4 shrink-0">
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
  </form>
</template>

<script setup lang="ts">
import type { Option, Product } from '@/types'
import VSelect from './VSelect.vue'
import VInput from './VInput.vue'
import VTextarea from './VTextarea.vue'
import { computed, reactive, watch } from 'vue'

// MARK: Props & emits

const props = defineProps<{
  mode: 'view' | 'edit'
  productDetails?: Product
  supplierList: Option<string>[]
}>()

const emit = defineEmits<{
  (e: 'close'): void
  (e: 'submit', updatedProduct: Partial<Product>): void
}>()

const form = reactive({
  supplier: {
    value: props.productDetails?.supplier.id || '',
    label: props.productDetails?.supplier.name || '',
  },
  productName: props.productDetails?.name || '',
  productCode: props.productDetails?.product_code || '',
  price: props.productDetails?.price || 0,
  description: props.productDetails?.description || '',
})

// MARK: Helpers

function handleSubmit() {
  const updatedProduct = {
    name: form.productName,
    code: form.productCode,
    price: form.price,
    description: form.description,
  }

  emit('submit', updatedProduct)
}
</script>
