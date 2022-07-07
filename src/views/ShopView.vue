<template>
  <ul id="shop-view">
    <li v-for="(item, index) in items" :key="index">
      <ItemCard :item="item"></ItemCard>
    </li>
    <ItemCreateCard/>
  </ul>
</template>

<script>
import ItemCard from "@/components/ItemCard";
import ItemCreateCard from "@/components/ItemCreateCard";
export default {
  name: "ShopView",
  components: {ItemCard, ItemCreateCard},
  data () {
    return {
      items: []
    }
  },
  created () {
      fetch("http://localhost:8001/items/all", {
        method: "GET",
        headers: {"Access-Control-Allow-Headers": "*"}
      })
        .then(response => response.json())
        .then(data => this.items = data['items']).then(data => console.log(data))
  }
}
</script>

<style scoped>
li {
  list-style: none;
}

li:not(:last-child) {
  margin-bottom: 32px;
}

ul {
  padding: 0;
}

#shop-view {
  width: 80%;
  display: flex;
  flex-flow: wrap row;
  justify-content: space-evenly;
  align-content: space-between;
  align-items: center;
  margin: 30px 0;
}

</style>