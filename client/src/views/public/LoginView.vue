<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
  <div class="flex flex-col justify-center flex-1 min-h-full py-12 sm:px-6 lg:px-8">
    <div class="text-center sm:mx-auto sm:w-full sm:max-w-md">
      <p class="text-4xl italic font-semibold text-blue-600">Kiosk</p>
      <h2 class="mt-6 font-bold tracking-tight text-gray-900 text-2xl/9">
        Sign in to your account
      </h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-[480px]">
      <div class="px-6 py-12 bg-white shadow sm:rounded-lg sm:px-12">
        <form class="space-y-6" action="#" method="POST">
          <div>
            <label for="email" class="block font-medium text-gray-900 text-sm/6">
              Email address
            </label>
            <div class="mt-2">
              <input
                id="email"
                name="email"
                type="email"
                autocomplete="email"
                required
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm/6"
              />
            </div>
          </div>

          <div>
            <label for="password" class="block font-medium text-gray-900 text-sm/6">Password</label>
            <div class="mt-2">
              <input
                id="password"
                name="password"
                type="password"
                autocomplete="current-password"
                required
                class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm/6"
              />
            </div>
          </div>

          <div class="flex justify-end">
            <div class="text-sm/6">
              <a href="#" class="font-semibold text-blue-600 hover:text-blue-500">
                Forgot password?
              </a>
            </div>
          </div>

          <div>
            <button
              type="submit"
              class="flex w-full justify-center rounded-md bg-blue-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-sm hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
            >
              Sign in
            </button>
          </div>
        </form>
      </div>

      <p class="mt-10 text-center text-gray-500 text-sm/6">
        Not a member?
        {{ ' ' }}
        <a href="/register" class="font-semibold text-blue-600 hover:text-blue-500">
          Register now
        </a>
      </p>
    </div>
  </div>
</template>
