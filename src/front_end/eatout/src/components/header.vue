<template>
  <header class="header">
      <h3>{{ header_text }}</h3>
      <img class="img-fluid" src="../assets/1.png">
  </header>
</template>

<script>
export default {
  name: 'Header',
  props: {
    msg: String
  },
  data: () => {
      return {
          header_text: "Welcome to"
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
header {
    border-bottom: 2px #f43461 solid;
    padding-bottom: 22px;
}
.img-fluid {
  max-height: 50px;
}
</style>
