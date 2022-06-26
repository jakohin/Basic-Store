<template>
  <div :class="{sticky: isSticky}" id="navbar" ref="navbar">
    <a v-for="(url, index) in linkList" :key="index">{{url}}</a>
  </div>
</template>

<script>
export default {
  name: "NavbarView",
  data () {
    return {
      linkList: ["Home", "About", "Shop"],
      isSticky: false,
    }
  },
  methods: {
    checkSticky () {
      this.isSticky = window.pageYOffset >= this.navbarOffset
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

<style scoped>
#navbar {
  max-height: 200px;
  width: 80%;
  display: flex;
  flex-flow: nowrap row;
  justify-content: space-evenly;
  margin-left: 10%;
  border-bottom: 1px solid black;
  background-color: white;
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

#navbar a:hover {
  background-color: whitesmoke;
}

.sticky {
  position: fixed;
  top: 0;
}
</style>