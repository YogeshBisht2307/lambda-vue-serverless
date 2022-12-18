<template>
  <router-view />
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
*,
::after,
::before {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: left;
}

a {
  text-decoration: none;
}

.text-center {
  text-align: center !important;
}

.is-invalid {
  border-color: red !important;
}
</style>