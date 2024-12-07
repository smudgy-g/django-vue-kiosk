<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <DashboardHeader>
      Products
      <template #button>
        <button
          type="button"
          class="block px-3 py-2 text-sm font-semibold text-center text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
          @click="handleAddProduct"
        >
          Add product
        </button>
      </template>
    </DashboardHeader>

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
            <VTableCell class="flex gap-2 text-right sm:pr-0">
              <button
                class="text-blue-600 hover:text-blue-900"
                @click="handleEditProduct(product.id)"
              >
                Edit
                <span class="sr-only">, {{ product.name }}</span>
              </button>
              <!-- <button class="text-blue-600 hover:text-blue-900" @click="handleViewProduct">
                View
                <span class="sr-only">, {{ product.name }}</span>
              </button> -->
            </VTableCell>
          </tr>
        </VTable>
      </template>
    </div>
    <VDrawer title="Manage Product" :open-drawer="isDrawerOpen" @close="isDrawerOpen = false">
      <ProductForm
        :mode="productDrawerMode"
        @close="isDrawerOpen = false"
        :product-details="selectedProduct"
        :supplier-list="supplierList"
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
import type { Option, Product, Supplier } from '@/types'
import DashboardHeader from '@/components/DashboardHeader.vue'

const isDrawerOpen = ref(false)
const productDrawerMode = ref<'edit' | 'view'>('view')
const selectedProduct = ref<Product>()
const supplierList = ref<Option<string>[]>([])

const {
  data: products,
  error,
  isFetching,
} = useFetch<Product[]>(import.meta.env.VITE_SERVER_BASE_URL + '/api/v1/products/').json()

if (error.value) {
  console.error(error)
  throw error.value
}

async function fetchSupplierList(): Promise<Option<string>[]> {
  const { data, error } = await useFetch<Supplier[]>(
    import.meta.env.VITE_SERVER_BASE_URL + '/api/v1/suppliers/',
  ).json()

  if (error.value) console.error(error.value)
  console.log(data.value)
  if (!data.value) return []

  return (data.value as Supplier[]).map((supplier) => ({
    value: supplier.id,
    label: supplier.name,
  }))
}

async function handleEditProduct(id: string) {
  productDrawerMode.value = 'edit'
  selectedProduct.value = (products.value as Product[]).find((p) => p.id === id)
  supplierList.value = [
    {
      value: selectedProduct.value?.supplier.id as string,
      label: selectedProduct.value?.supplier.name as string,
    },
  ]
  // supplierList.value = (await fetchSupplierList()) ?? []
  isDrawerOpen.value = true
}

function handleAddProduct() {
  productDrawerMode.value = 'edit'
  isDrawerOpen.value = true
}
</script>
