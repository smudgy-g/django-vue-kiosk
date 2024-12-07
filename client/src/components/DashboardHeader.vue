<template>
  <div class="sm:flex sm:items-center">
    <div class="sm:flex-auto">
      <h1 class="text-base font-semibold text-gray-900">
        <slot />
      </h1>
      <p class="mt-2 text-sm text-gray-700">
        <slot name="subheader" />
      </p>
    </div>
    <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
      <slot name="button" />
    </div>
  </div>
</template>
