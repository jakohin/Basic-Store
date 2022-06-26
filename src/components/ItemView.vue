<template>
  <div class="item">
    <img class="item-img" src="{{itemThumb}}">
    <h2 class="item-name">{{itemName}}</h2>
    <div class="item-price">{{itemPrice}}</div>
    <div class="item-desc">
      {{itemDesc}}
    </div>
  </div>
</template>

<script>
export default {
  name: "ItemView",
  data () {
    return {
      itemThumb: "https://via.placeholder.com/240x240",
      itemName: "TestItem",
      itemPrice: "123",
      itemDesc: "This is an very epic item. Most notably, it is an item."
    }
  }
}
</script>

<style scoped>

.item {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-content: space-between;
  border: 1px solid black;
  padding: 8px;
}

.item-img {
  height: 60%;
  width: 80%;
  padding-left: 10%;
}

.item-name {
  border-top: 1px solid black;
  margin-bottom: 5px;
}

.item-desc {
  margin-top: 8px;
  padding-bottom: 8px;
  border-bottom: 1px solid black;
}

.item-price {
  color: #3f3f3f;
}

.item-price::before{
  content: "$ "
}
</style>