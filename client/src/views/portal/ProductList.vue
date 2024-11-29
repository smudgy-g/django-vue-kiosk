<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold text-gray-900">Products</h1>
        <!-- <p class="mt-2 text-sm text-gray-700">
                A list of all the products in your account including their name, product_code, email and Description.
              </p> -->
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <button
          type="button"
          class="block px-3 py-2 text-sm font-semibold text-center text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
          @click="handleAddProduct"
        >
          Add product
        </button>
      </div>
    </div>
    <div class="mt-8 -mx-4 sm:-mx-0">
      <TheLoadingSpinner v-if="isFetching" class="mt-16" />
      <template v-else>
        <VTable>
          <template #head>
            <tr>
              <VTableHeadCell class="sm:pl-0"> Name </VTableHeadCell>
              <VTableHeadCell class="hidden lg:table-cell"> Description </VTableHeadCell>
              <VTableHeadCell class="hidden sm:table-cell"> Product Code </VTableHeadCell>
              <VTableHeadCell> Price </VTableHeadCell>
              <VTableHeadCell class="relative sm:pr-0">
                <span class="sr-only">Edit</span>
              </VTableHeadCell>
            </tr>
          </template>

          <tr v-for="product in products" :key="product.id">
            <VTableCell class="w-full text-gray-900 max-w-0 sm:w-auto sm:max-w-none sm:pl-0">
              {{ product.name }}
              <dl class="font-normal lg:hidden">
                <dt class="sr-only">Product Code</dt>
                <dd class="mt-1 text-gray-700 truncate">{{ product.product_code }}</dd>
              </dl>
            </VTableCell>
            <VTableCell class="hidden lg:table-cell">
              {{ product.description }}
            </VTableCell>
            <VTableCell class="hidden sm:table-cell">
              {{ product.product_code }}
            </VTableCell>
            <VTableCell>
              {{ product.price }}
            </VTableCell>
            <VTableCell class="text-right sm:pr-0">
              <button
                class="text-blue-600 hover:text-blue-900"
                @click="() => handleEditProduct(product.id)"
              >
                Edit
                <span class="sr-only">, {{ product.name }}</span>
              </button>
            </VTableCell>
          </tr>
        </VTable>
      </template>
    </div>
    <VDrawer title="Add Product" :open-drawer="isDrawerOpen" @close="isDrawerOpen = false">
      <ProductForm
        :mode="productDrawerMode"
        @close="isDrawerOpen = false"
        :product-details="selectedProduct"
      />
    </VDrawer>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useFetch } from '@vueuse/core'
import VTable from '@/components/VTable.vue'
import VTableHeadCell from '@/components/VTableHeadCell.vue'
import VTableCell from '@/components/VTableCell.vue'
import VDrawer from '@/components/VDrawer.vue'
import TheLoadingSpinner from '@/components/TheLoadingSpinner.vue'
import ProductForm from '@/components/ProductForm.vue'
import type { Product } from '@/types'

const isDrawerOpen = ref(false)
const isLoading = ref(false)
const productDrawerMode = ref<'edit' | 'view'>('view')
const selectedProduct = ref<Product>()

const {
  data: products,
  error,
  isFetching,
} = useFetch<Product[]>(import.meta.env.VITE_SERVER_BASE_URL + '/api/v1/products/').json()

if (error.value) {
  console.error(error)
  throw error.value
}

function fetchProduct(id: string) {
  const { data, error } = useFetch(
    import.meta.env.VITE_SERVER_BASE_URL + '/api/v1/products/' + id,
  ).json()

  if (error.value) {
    console.error(error)
    throw error.value
  }
  selectedProduct.value = data as unknown as Product
}

function handleEditProduct(id: string) {
  fetchProduct(id)
  productDrawerMode.value = 'edit'
  isDrawerOpen.value = true
}

function handleAddProduct() {
  productDrawerMode.value = 'edit'
  isDrawerOpen.value = true
}

function handleViewProduct() {
  productDrawerMode.value = 'view'
  isDrawerOpen.value = true
}
</script>
