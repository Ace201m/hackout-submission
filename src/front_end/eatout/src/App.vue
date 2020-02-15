<template>
  <div id="app">
    <appHeader></appHeader>
    <appBody></appBody>
    <appFooter></appFooter>
  </div>
</template>

<script>
import appHeader from './components/header.vue'
import appFooter from './components/footer.vue'
import appBody from './components/body.vue'
import VueResource from 'vue-resource'
import Vue from 'vue'
import axios from 'axios'

Vue.use(VueResource)
Vue.use(axios)

export default {
  name: 'App',
  components: {
    'appHeader': appHeader,
    'appFooter': appFooter,
    'appBody': appBody
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
  margin-top: 22px;
}
</style>
