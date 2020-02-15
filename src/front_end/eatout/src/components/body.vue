<template>
  <div class="app_body container">
    <template v-for='(message, index) in getMessages'>
      <messageDisplay v-bind:message='message' :fromBot='message.fromBot' :key="index"></messageDisplay>
    </template>
    
    <br>
    <hr v-if="!initial && isVeg!=''">
    <h3>{{ question }}</h3>
    <br>
    
    
    <button class="btn" v-if='initial' @click="initialize()" >Start!</button>
    
    <template v-if="!initial && isVeg==''" >
      <template v-for='category in categories'>
    <button class="btn"   :key='category' @click="setIsVeg(category)" >{{ category }}</button>
    </template>
    </template>

    <template v-if="!initial && isVeg!=''">
      <template v-for='category in categories'>
    <button class="btn" :key='category' @click="getSomething(category)" >{{ category }}</button>
    </template>
    </template>

  </div>
</template>

<script>
import messageDisplay from './messageDisplay.vue';

export default {
  name: 'Body',
  components: {
    'messageDisplay': messageDisplay
  },
  data: ()=>{
    return {
      messages: [],
      q: [],
      isVeg: '',
      categories: ['Start!'],
      initial: true,
      question: "Can't think what to eat, I can help?",
    }
  },
  methods: {
    getSomething (index) {
      console.log(index);
      this.$http.get('https://reqres.in/api/products/3').then(
        (data) => {
          this.messages.push(data);
          console.log("This runs");
        }
      );
      this.question=""
    },
    initialize () {
      this.question = "What would you prefer?";
      this.categories = ['Veg', 'Both', 'Non veg'];
      this.initial = false;
    },
    setIsVeg (inp) {
      this.isVeg = inp;
      this.isVeg = this.isVeg.replace(/\s/g,'').toLowerCase();
      var newMessage = {
        fromBot: false,
        messageText: "You selected "+inp
      }
      this.messages.push(newMessage);

      // send request

      this.$http.get('http://localhost:5000/recommender?isveg='+this.isVeg+'&query=').then(
        (response) => {
          console.log("Success");
          console.log(response);
        }
      ).catch( response => {
        console.log(response);
      });
      
    }
  },
  computed: {
    getMessages () {
      return this.messages;
    }
  }
}
</script>





























<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.app_body {
    margin-top:10px;
    min-height: 400px;
    margin-bottom:70px;
}
div.app_body {
  border: 20px #f43461 solid;
}
.btn {
  background-color: #f43461;
  color: white;
  padding: 7px;
  border-radius: 10px;
  margin: 15px;
  margin-top:7px;
}
.btn:focus, .btn:active:focus, .btn.active:focus{
    outline:none;
    box-shadow:none;
}
h3{
  margin-bottom: 0px;
  padding-bottom: 0;
}

</style>
