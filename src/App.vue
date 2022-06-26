<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans&family=Nunito:wght@200&display=swap" rel="stylesheet">
  <div id="main">
    <div id="header">
      <h1>JHB</h1>
      <NavbarView></NavbarView>
    </div>
    <div id="content" :style="{'margin-top': contentMarginTop}">
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
import jQuery from 'jquery'

global.$ = jQuery

export default {
  name: 'App',
  components: {
    NavbarView,
    ShopView
  },
  computed: {
    contentMarginTop () {
      return global.$('#navbar').outerHeight() + 30
    }
  },
  data () {
    return {

    }
  }
}
</script>

<style>
:root {
  font-family: 'Nunito Sans', sans-serif;
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100vw;
  background-color: white;
}

body {
  padding: 0;
  margin: 0;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  display: grid;
}

#content {
  display: flex;
  justify-content: space-evenly;
  align-content: space-between;
  align-items: center;
  margin: 30px 0;
  /*background: url("assets/blob-scene-haikei.svg") no-repeat top center;*/
  overflow: hidden;
}

a:hover {
  cursor: pointer;
}
</style>
