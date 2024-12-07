<template>
  <component
    :is="variant === Variant.Link ? 'router-link' : 'button'"
    :type="setType"
    class="px-3 py-2 font-semibold cursor-pointer text-sm/6"
    :class="styles"
    :disabled="disabled"
  >
    <slot />
  </component>
</template>
<script setup lang="ts">
import { computed } from 'vue'
import { Variant } from '@/enums'

const props = withDefaults(
  defineProps<{
    variant?: Variant
    type?: 'button' | 'submit'
    disabled?: boolean
  }>(),
  {
    variant: Variant.Primary,
    type: 'button',
    disabled: false,
  },
)

const setType = computed(() => {
  return props.variant === Variant.Link ? undefined : props.type
})

const styles = computed(() => {
  switch (props.variant) {
    case Variant.Primary:
      return 'rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600'

    case Variant.Link:
      return 'hover:underline'
    case Variant.Secondary:
    default:
      return 'text-gray-900 '
  }
})
</script>
