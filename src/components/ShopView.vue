<template>
  <ul id="shop-view">
    <li v-for="(item, index) in getItems()" :key="index">
      <ItemView :item="item"></ItemView>
    </li>
  </ul>
</template>

<script>
import ItemView from "@/components/ItemView";
export default {
  name: "ShopView",
  components: {ItemView},
  methods: {
    getItems () {
      return [
        {
          thumbnail: "https://via.placeholder.com/240x240",
          name: "TestItem",
          price: "123",
          desc: "This is an very epic item. Most notably, it is an item."
        },
          {
          thumbnail: "https://via.placeholder.com/240x240",
          name: "TestItem2",
          price: "87",
          desc: "This is an very epic item. Most notably, it is an item."
        }
      ]
    }
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