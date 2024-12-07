<template>
  <TransitionRoot as="template" :show="openDrawer">
    <Dialog class="relative z-10" @close="$emit('close')">
      <div class="fixed inset-0" />

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div class="fixed inset-y-0 right-0 flex max-w-full pl-10 pointer-events-none">
            <TransitionChild
              as="template"
              enter="transform transition ease-in-out duration-500 sm:duration-700"
              enter-from="translate-x-full"
              enter-to="translate-x-0"
              leave="transform transition ease-in-out duration-500 sm:duration-700"
              leave-from="translate-x-0"
              leave-to="translate-x-full"
            >
              <DialogPanel class="w-screen max-w-md pointer-events-auto">
                <div class="flex flex-col h-full overflow-y-scroll bg-white shadow-xl">
                  <div class="px-4 py-6 bg-blue-700 sm:px-6">
                    <div class="flex items-center justify-between">
                      <DialogTitle class="text-base font-semibold text-white">
                        {{ title }}
                      </DialogTitle>
                      <div class="flex items-center ml-3 h-7">
                        <button
                          type="button"
                          class="relative text-blue-200 bg-blue-700 rounded-md hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                          @click="$emit('close')"
                        >
                          <span class="absolute -inset-2.5" />
                          <span class="sr-only">Close panel</span>
                          <XMarkIcon class="size-6" aria-hidden="true" />
                        </button>
                      </div>
                    </div>
                    <div class="mt-1">
                      <p class="text-sm text-blue-300">
                        <slot name="sub-heading" />
                      </p>
                    </div>
                  </div>
                  <div class="relative flex-1 px-4 py-6 sm:px-6">
                    <!-- Your content -->
                    <slot />
                  </div>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup lang="ts">
import { Dialog, DialogPanel, DialogTitle, TransitionChild, TransitionRoot } from '@headlessui/vue'
import { XMarkIcon } from '@heroicons/vue/24/outline'

defineProps<{
  openDrawer: boolean
  title: string
}>()

defineEmits<{
  (e: 'close'): void
}>()
</script>
