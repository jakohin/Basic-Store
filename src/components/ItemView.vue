<template>
  <div class="item">
    <img class="item-img" :src="item['images']">
    <div class="item-info">
      <h2 class="item-name">{{ item['name'] }}</h2>
      <div class="item-price">{{ item['price'] }}</div>
      <div class="item-desc">
        {{ item['desc'] }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ItemView",
  data () {
    return {
    }
  },
  props: {
    item: Object,
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
  padding: 16px 8px;
  text-align: left;
  min-width: 250px;
  min-height: 340px;
}

.item-img {
  height: 60%;
  width: 80%;
  padding-left: 10%;
}

.item-info {
  margin-top: 16px;
  border-top: 1px solid black;
}

.item-info *{
  margin-left: 8px;
}

.item-name {
  margin: 8px 0 0 0;
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