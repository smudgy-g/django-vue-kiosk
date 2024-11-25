<template>
  <table class="min-w-full divide-y divide-gray-300">
    <thead>
      <!-- <tr>
        <th
          scope="col"
          class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-0"
        >
          Name
        </th>
        <th
          scope="col"
          class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 lg:table-cell"
        >
          Description
        </th>
        <th
          scope="col"
          class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 sm:table-cell"
        >
          Product Code
        </th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Price</th>
        <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0">
          <span class="sr-only">Edit</span>
        </th>
      </tr> -->
      <slot name="head" />
    </thead>
    <tbody class="bg-white divide-y divide-gray-200">
      <!-- <tr v-for="product in products" :key="product.id">
        <td
          class="w-full py-4 pl-4 pr-3 text-sm font-medium text-gray-900 max-w-0 sm:w-auto sm:max-w-none sm:pl-0"
        >
          {{ product.name }}
          <dl class="font-normal lg:hidden">
            <dt class="sr-only">Product Code</dt>
            <dd class="mt-1 text-gray-700 truncate">{{ product.product_code }}</dd>
          </dl>
        </td>
        <td class="hidden px-3 py-4 text-sm text-gray-500 lg:table-cell">
          {{ product.description }}
        </td>
        <td class="hidden px-3 py-4 text-sm text-gray-500 sm:table-cell">
          {{ product.product_code }}
        </td>
        <td class="px-3 py-4 text-sm text-gray-500">{{ product.price }}</td>
        <td class="py-4 pl-3 pr-4 text-sm font-medium text-right sm:pr-0">
          <a href="#" class="text-blue-600 hover:text-blue-900">
            Edit
            <span class="sr-only">, {{ product.name }}</span>
          </a>
        </td>
      </tr> -->
      <slot />
    </tbody>
  </table>
</template>
