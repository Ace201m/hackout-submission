<template>
  <div>
  <div @click="fromBot=!fromBot" v-bind:class="{ message_body: true, l: fromBot, r: !fromBot }" >
  
    <div v-if='typeof(message.messageText)==typeof([1,2])'>
      <div v-for="(res, index) in message.messageText" :key="res"> 
        <p>{{ 1+index }}. {{ res[0] }}</p>
         <img style="max-height:100px;" :src='res[1]'>

        
      </div>
    </div>
    <div v-else>
      {{ message.messageText }}
    </div>
    
    
  </div>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: [
    'message', 'key'
  ],
  data () {
    return {

    }
  },
  methods: {
    
  },
  computed: {
    fromBot () {
      return this.message.fromBot;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.message_body {
  background-color: rgb(235, 235, 235);
  margin: 22px;
  border-radius: 25px;
  padding: 15px;
}

.l {
  text-align: left;
  margin-right: 100px;
}

.r {
text-align: right;
margin-left: 100px;
}
</style>
