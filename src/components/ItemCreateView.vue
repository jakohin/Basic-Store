<template>
  <div class="item">
    <UploadImages class="item-img" :max="5" v-model="itemImages" @change="handleImages"/>
    <div class="item-info">
      <label for="itemNameField"></label>
      <input ref="itemNameField"  class="item-name" v-model="itemName" placeholder="Item Name"/>
      <input ref="itemPriceField" type="number" min="0" step="any" class="item-price" v-model="itemPrice"/>
      <input ref="itemStockField" type="number" min="0" class="item-stock" v-model="itemStock"/>
      <textarea ref="itemDescField" class="item-desc" v-model="itemDesc"></textarea>
      <button @click.prevent="createItem">Save</button>
    </div>
  </div>
</template>

<script>
import UploadImages from "vue-upload-drop-images"
import { notify } from "@kyvg/vue3-notification";
export default {
  name: "ItemView",
  data () {
    return {
      itemImages: [],
      itemName: "",
      itemPrice: 0.0,
      itemDesc: "",
      itemStock: 0,
    }
  },
  components: {
    UploadImages
  },
  methods: {
    handleImages (files) {
      console.log(files)
    },
    createItem () {
      if (this.verifyFields()) {
        fetch("http://localhost:8001/items/create?" + new URLSearchParams({
          name: this.itemName,
          desc: this.itemDesc,
          price: this.itemPrice,
          images: this.itemImages,
          stock: this.itemStock
        }), {
          method: "PUT",
          headers: {"Access-Control-Allow-Headers": "*"}
        })
      }
    },
    verifyFields () {
      if (! this.itemName.length > 0) {
        notify({type: "error", text: "The item must have a name!"})
        this.$refs.itemNameField.classList.add("error")
        return false
      } else {
        this.$refs.itemNameField.classList.remove("error")
      }
      if (! this.itemDesc.length > 0) {
        notify({type: "error", text: "The item must have a description!"})
        this.$refs.itemDescField.classList.add("error")
        return false
      }  else {
        this.$refs.itemDescField.classList.remove("error")
      }
      if(! this.itemStock > 0) {
        notify({type: "error", text: "Must have at least one item in stock!"})
        this.$refs.itemStockField.classList.remove("error")
        return false
      } else {
        this.$refs.itemStockField.classList.remove("error")
      }
      if (! this.itemPrice === 0) {
        notify({type: "warn", text: "Do you really want the item to be free?"})
      }
      return true
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
}

.item-img {
  max-height: 240px;
  max-width: 240px;
  height: 60%;
  width: 80%;
  padding-left: 10%;
}

.item-img:before {
  content: "Item Image"
}

.item-info {
  display: flex;
  flex-flow: column nowrap;
  margin-top: 16px;
  border-top: 1px solid black;
}

.item-info *{
  margin-left: 8px;
  font-family: 'Nunito Sans', sans-serif;
}

.item-name {
  display: block;
  font-size: 1.5em;
  margin-block-start: 0.83em;
  margin-block-end: 0.83em;
  margin-inline-start: 0;
  margin-inline-end: 0;
  font-weight: bold;
  margin: 8px 0;
}

.item-name:before {
  content: "Item Name"
}

.item-desc {
  margin-top: 8px;
  padding-bottom: 8px;
  border-bottom: 1px solid black;
}

.item-desc:before {
  content: "Item Description"
}

.item-price {
  color: #3f3f3f;
}

.item-price:before {
  content: "Price"
}

.item-price::after{
  content: "$ "
}

.error {
  background-color: whitesmoke;
  border-color: #E41D12;
}

</style>