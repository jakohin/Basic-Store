<template>
  <div id="navbar">
    <a v-for="(url, index) in linkList" :key="index">{{url}}</a>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data () {
    return {
      linkList: ["Home", "About", "Shop"]
    }
  }
}
</script>

<style scoped>
#navbar {
  max-height: 200px;
  width: 80%;
  display: flex;
  flex-flow: nowrap row;
  justify-content: space-evenly;
}

#navbar a {
  text-align: center;
  text-decoration: none;
  width: 30%;
  height: auto;
  padding: 8px;
  margin: 8px;
  background-color: white;
}
</style>