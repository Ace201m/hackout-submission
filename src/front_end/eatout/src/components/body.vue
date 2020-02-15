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
      baseURL: 'http://localhost:5000/recommender?isveg=',
      q: [],
      isVeg: '',
      categories: ['Start!'],
      initial: true,
      question: "Can't think what to eat, I can help?",
    }
  },
  methods: {
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
        messageText: "You selected "+inp+'.'
      }
      this.messages.push(newMessage);

      // send request

      this.$http.get(this.baseURL+this.isVeg+'&query=').then(
        (response) => {
          var nnewMessage = {
            messageText: "What would you like to have?",
            fromBot: true,
          }

          this.question = "Select from given options -";          
          var temp = [];
          for(var i in response.body.options){
            temp.push(response.body.options[i]);
          }
          this.categories = temp;
          this.messages.push(nnewMessage);


        }
      ).catch( response => {
        console.log(response);
      });
    },

    getSomething (category) {
      this.q.push(category);
      
      this.messages.push({
        fromBot: false,
        messageText: "You selected "+category+'.'
      });

      var queryAddOn = '';

      for(var a in this.q){
        queryAddOn += this.q[a].replace(' ','_');
        if(a!=this.q.length-1){
          queryAddOn += '*';
        }
          
      }
      this.$http.get(this.baseURL+this.isVeg+'&query='+queryAddOn).then(
        (response) => {
          
          if('result' in response.body){

            this.question = "complete";
            console.log(response);
            console.log(response.body.result);
            var nnnewMessage = {
              messageText: response.body.result,
              fromBot: true,
            };
            this.messages.push(nnnewMessage);
            this.categories = [];
          }
          else{
            var nnewMessage = {
            messageText: "What would you like to have?",
            fromBot: true,
          }

          this.question = "Select from given options -";          
          var temp = [];
          for(var i in response.body.options){
            temp.push(response.body.options[i]);
          }
          this.categories = temp;
          this.messages.push(nnewMessage);
          }
          


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
  },
  
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
