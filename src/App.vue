<template>
  <div id="main">
    <div id="header">
      <h1>JHB</h1>
      <NavbarView></NavbarView>
    </div>
    <div id="content">
      <ShopView></ShopView>
    </div>
    <div id="footer">
      <a>Impressum</a>
      <a>Contact</a>
      <div>
        (c) 2022 JHB
      </div>
    </div>
  </div>
</template>

<script>
import ShopView from "@/components/ShopView";
import NavbarView from "@/components/NavbarView";

export default {
  name: 'App',
  components: {
    NavbarView,
    ShopView
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#content {
  grid-area: 2 / 1 / span 1 / span 5;
  display: flex;
  flex-flow: wrap row;
  justify-content: space-evenly;
  align-content: space-between;
  align-items: center;
  margin-top: 30px;
}

a:hover {
  cursor: pointer;
}
</style>
