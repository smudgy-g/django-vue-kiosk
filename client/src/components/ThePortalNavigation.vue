<template>
  <Disclosure as="nav" class="bg-blue-600" v-slot="{ open }">
    <div class="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <div class="shrink-0">
            <p class="text-3xl italic font-semibold text-white">Kiosk</p>
          </div>
          <div class="hidden md:block">
            <div class="flex items-baseline ml-10 space-x-4">
              <a
                v-for="item in navigation"
                :key="item.name"
                :href="item.href"
                :class="[
                  item.current ? 'bg-blue-700 text-white' : 'text-white hover:bg-blue-500/75',
                  'rounded-md px-3 py-2 text-sm font-medium',
                ]"
                :aria-current="item.current ? 'page' : undefined"
                >{{ item.name }}</a
              >
            </div>
          </div>
        </div>
        <div class="hidden md:block">
          <div class="flex items-center ml-4 md:ml-6">
            <!-- Profile dropdown -->
            <Menu as="div" class="relative ml-3">
              <div>
                <MenuButton
                  class="relative flex items-center max-w-xs px-2 py-1 text-sm bg-blue-600 rounded-md focus:outline-none focus:ring-1 focus:ring-white focus:ring-offset-2 focus:ring-offset-blue-600"
                >
                  <span class="font-semibold text-white">Account</span>
                </MenuButton>
              </div>
              <transition
                enter-active-class="transition duration-100 ease-out"
                enter-from-class="transform scale-95 opacity-0"
                enter-to-class="transform scale-100 opacity-100"
                leave-active-class="transition duration-75 ease-in"
                leave-from-class="transform scale-100 opacity-100"
                leave-to-class="transform scale-95 opacity-0"
              >
                <MenuItems
                  class="absolute right-0 z-10 w-48 py-1 mt-2 origin-top-right bg-white rounded-md shadow-lg ring-1 ring-black/5 focus:outline-none"
                >
                  <MenuItem v-for="item in userNavigation" :key="item.name" v-slot="{ active }">
                    <a
                      :href="item.href"
                      :class="[
                        active ? 'bg-gray-100 outline-none' : '',
                        'block px-4 py-2 text-sm text-gray-700',
                      ]"
                      >{{ item.name }}</a
                    >
                  </MenuItem>
                </MenuItems>
              </transition>
            </Menu>
          </div>
        </div>
        <div class="flex -mr-2 md:hidden">
          <!-- Mobile menu button -->
          <DisclosureButton
            class="relative inline-flex items-center justify-center p-2 text-blue-200 bg-blue-600 rounded-md hover:bg-blue-500/75 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-blue-600"
          >
            <span class="absolute -inset-0.5" />
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block size-6" aria-hidden="true" />
            <XMarkIcon v-else class="block size-6" aria-hidden="true" />
          </DisclosureButton>
        </div>
      </div>
    </div>

    <DisclosurePanel class="md:hidden">
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <DisclosureButton
          v-for="item in navigation"
          :key="item.name"
          as="a"
          :href="item.href"
          :class="[
            item.current ? 'bg-blue-700 text-white' : 'text-white hover:bg-blue-500/75',
            'block rounded-md px-3 py-2 text-base font-medium',
          ]"
          :aria-current="item.current ? 'page' : undefined"
          >{{ item.name }}</DisclosureButton
        >
      </div>
      <div class="pb-3 border-t border-blue-700">
        <div class="flex items-center px-5">
          <!-- <div class="ml-3">
            <div class="text-base font-medium text-white">{{ user.name }}</div>
            <div class="text-sm font-medium text-blue-300">{{ user.email }}</div>
          </div> -->
        </div>
        <div class="px-2 mt-3 space-y-1">
          <DisclosureButton
            v-for="item in userNavigation"
            :key="item.name"
            as="a"
            :href="item.href"
            class="block px-3 py-2 text-base font-medium text-white rounded-md hover:bg-blue-500/75"
          >
            {{ item.name }}
          </DisclosureButton>
        </div>
      </div>
    </DisclosurePanel>
  </Disclosure>
</template>
<script setup lang="ts">
import { watch } from 'vue'
import { useRoute } from 'vue-router'
import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from '@headlessui/vue'
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline'

const route = useRoute()

const user = {
  name: 'Tom Cook',
  email: 'tom@example.com',
}

const navigation = [
  { name: 'Dashboard', href: '/portal/dashboard', current: true },
  { name: 'Products', href: '/portal/products', current: false },
  { name: 'Suppliers', href: '/portal/suppliers', current: false },
  { name: 'Orders', href: '/portal/orders', current: false },
  { name: 'Reports', href: '/portal/reports', current: false },
]
const userNavigation = [
  { name: 'Your Profile', href: '#' },
  { name: 'Settings', href: '#' },
  { name: 'Sign out', href: '#' },
]

watch(
  () => route.name,
  (newName, oldName) => {
    console.log(newName)
    navigation.forEach((item) => {
      if (item.name.toLowerCase() === newName) {
        item.current = true
      } else {
        item.current = false
      }
    })
  },
  {
    deep: true,
  },
)
</script>
