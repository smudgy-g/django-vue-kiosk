<template>
  <div class="px-4 sm:px-6 lg:px-8">
    <DashboardHeader>
      Suppliers
      <template #button>
        <button
          type="button"
          class="block px-3 py-2 text-sm font-semibold text-center text-white bg-blue-600 rounded-md shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
        >
          <!-- @click="handleAddSupplier" -->
          Add Supplier
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
              <VTableHeadCell class="hidden lg:table-cell"> Contact </VTableHeadCell>
              <VTableHeadCell class="hidden sm:table-cell"> Phone </VTableHeadCell>
              <VTableHeadCell> Email </VTableHeadCell>
              <VTableHeadCell class="relative sm:pr-0">
                <span class="sr-only">Edit</span>
              </VTableHeadCell>
            </tr>
          </template>

          <tr v-for="supplier in suppliers" :key="supplier.id">
            <VTableCell class="w-full text-gray-900 max-w-0 sm:w-auto sm:max-w-none sm:pl-0">
              {{ supplier.name }}
              <dl class="font-normal lg:hidden">
                <dt class="sr-only">supplier Code</dt>
                <dd class="mt-1 text-gray-700 truncate">{{ supplier.phone }}</dd>
              </dl>
            </VTableCell>
            <VTableCell class="hidden lg:table-cell">
              {{ supplier.contact_person }}
            </VTableCell>
            <VTableCell class="hidden sm:table-cell">
              {{ supplier.phone }}
            </VTableCell>
            <VTableCell>
              {{ supplier.email }}
            </VTableCell>
            <VTableCell class="text-right sm:pr-0">
              <button class="text-blue-600 hover:text-blue-900" @click="">
                Edit
                <span class="sr-only">, {{ supplier.name }}</span>
              </button>
            </VTableCell>
          </tr>
        </VTable>
      </template>
    </div>
    <!-- <VDrawer title="Add Supplier" :open-drawer="isDrawerOpen" @close="isDrawerOpen = false">
      <SupplierForm
        :mode="supplierDrawerMode"
        @close="isDrawerOpen = false"
        :supplier-details="selectedSupplier"
      />
    </VDrawer> -->
  </div>
</template>
<script setup lang="ts">
import { useFetch } from '@vueuse/core'
import DashboardHeader from '@/components/DashboardHeader.vue'
import TheLoadingSpinner from '@/components/TheLoadingSpinner.vue'
import VTable from '@/components/VTable.vue'
import VTableHeadCell from '@/components/VTableHeadCell.vue'
import VTableCell from '@/components/VTableCell.vue'
import type { Supplier } from '@/types'

const { data: suppliers, isFetching } = useFetch<Supplier[]>(
  import.meta.env.VITE_SERVER_BASE_URL + '/api/v1/suppliers',
).json()
</script>
