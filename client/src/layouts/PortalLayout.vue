<template>
  <div class="min-h-full">
    <ThePortalNavigation />
    <header class="bg-white shadow-sm">
      <!-- <div class="px-4 py-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
        <h1 class="font-semibold text-gray-900 text-lg/6">Dashboard</h1>
      </div> -->
    </header>
    <main>
      <div class="px-4 py-6 mx-auto max-w-7xl sm:px-6 lg:px-8">
        <!-- Your content -->
        <router-view />
      </div>
    </main>
  </div>
</template>

<script setup>
import ThePortalNavigation from '@/components/ThePortalNavigation.vue'
</script>
