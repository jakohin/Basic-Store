<template>
  <ItemView v-for="(item, index) in getItems()" :key="index"></ItemView>
</template>

<script>
import ItemView from "@/components/ItemView";
export default {
  name: "ShopView",
  components: {ItemView},
  methods: {
    getItems () {
      return []
    }
  }
}
</script>

<style scoped>

</style>