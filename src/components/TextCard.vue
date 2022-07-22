<template>
  <div id="text-container">
    {{ data }}
  </div>
</template>

<script>
export default {
  name: "TextCard",
  props: {
    data: String,
  }
}
</script>

<style scoped>
#text-container {
  display: flex;
  flex-flow: row wrap;
  width: 80%;
  border: black solid 1px;
}
</style>