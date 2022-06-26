<template>
  <div id="main">
    <div id="header">
      <h1>JHB</h1>
      <Navbar></Navbar>
    </div>
    <Content>
      <ShopView></ShopView>
    </Content>
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
import HelloWorld from './components/HelloWorld.vue'
import Content from "@/components/Content";
import Navbar from "@/components/Navbar";

export default {
  name: 'App',
  components: {
    Navbar,
    Content,
    HelloWorld
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
</style>
