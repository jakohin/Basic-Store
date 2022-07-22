<template>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Nunito+Sans&family=Nunito:wght@200&display=swap" rel="stylesheet">
  <div id="main">
    <div id="header">
      <h1>JHB</h1><router-link id="login-button" to="/login">Login</router-link>
      <nav :class="{sticky: isSticky}" id="navbar" ref="navbar">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/shop">Shop</router-link>
      </nav>
      <AdminNavbar v-if="this.authenticated()"/>
    </div>
    <router-view id="content" :style="{'margin-top': contentMarginTop}"/>
    <div id="footer">
      <nav id="footer-nav">
        <router-link to="/impress">Impress</router-link>
        <router-link to="/contact">Contact</router-link>
      </nav>
      <div>© 2022 JHB</div>
    </div>
  </div>
</template>

<script>
import jQuery from 'jquery'
import AdminNavbar from "./components/AdminNavbar";

global.$ = jQuery

export default {
  components: {AdminNavbar},
  data () {
    return {
      isSticky: false
    }
  },
  computed: {
    authenticated () { return this.$store.state.authenticated },
    contentMarginTop () {
      return global.$('#navbar').outerHeight() + 30
    },
  },
  methods: {
    checkSticky () {
      this.isSticky = scrollY >= this.navbarOffset
    }
  },
  mounted() {
    window.onscroll = () => {
      this.checkSticky()
    }
    this.navbarOffset = this.$refs.navbar.getBoundingClientRect().top
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

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#header {}

#footer {}

body {
  padding: 0;
  margin: 0;
}

#navbar, #footer-nav {
  max-height: 200px;
  width: 80%;
  display: flex;
  flex-flow: nowrap row;
  justify-content: space-evenly;
  margin-left: 10%;
  background-color: white;
}

#navbar {
  border-bottom: 1px solid black;
}
#navbar a{
  color: black
}

#footer-nav {
  border-top: 1px solid black;
}
#footer-nav a{
  color: #3f3f3f;
}

#navbar a, #footer-nav a {
  text-align: center;
  text-decoration: none;
  width: 30%;
  height: auto;
  padding: 8px;
  margin: 8px;
  background-color: white;
}

#navbar a:hover, #footer-nav a:hover {
  background-color: whitesmoke;
}

a:hover {
  cursor: pointer;
}

.sticky {
  position: fixed;
  top: 0;
}

nav a.router-link-exact-active {
  color: #42b983;
}

#content {
  display: flex;
  justify-content: space-evenly;
  align-content: space-between;
  align-items: center;
  margin: 30px 0;
  /*background: url("assets/blob-scene-haikei.svg") no-repeat top center;*/
  overflow: hidden;
  flex-flow: row wrap;
}

#login-button {
  border: 1px solid black;
  padding: 8px;
  width: 10%;
  position: fixed;
  right: 10%;
  top: 10%;
}

#login-button{
  color: black;
  text-decoration: none;
}

#login-button:hover {
  background-color: whitesmoke;
}


@media only screen and (orientation: portrait) {
  #content {
    align-content: center;
  }
}
</style>
