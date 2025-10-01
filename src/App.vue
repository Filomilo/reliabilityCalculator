<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'



import InputNumber from 'primevue/inputnumber';
import { ref, type Ref } from 'vue';


const numberA: Ref<number> =ref(0)

const numberB: Ref<number> =ref(0)
</script>

<template>

  <div class="main">

<div class="inputContainer">
Number A:
<InputNumber v-model="numberA" class="inputNumber" fluid  />
</div>
<div class="inputContainer" >
Number B:
<InputNumber v-model="numberB" class="inputNumber" fluid   />
</div>
<div class="result">
A+B={{numberA + numberB}}

</div>

<div class="result">
A-B={{numberA - numberB}}
</div>

<div class="result">
A*B={{numberA * numberB}}
</div>

<div class="result">
A/B={{numberA / numberB}}
</div>

  </div>


</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}

.inputContainer{
  margin-top:20px;
  margin-bottom:20px;
  display:flex;
  flex-direction:column;
  gap:10px;
  width:150px;
  align-items:center;
}
.inputNumber{
  width:150px;
  background-color: rgb(216, 216, 216)
}

.result{
  margin-top:20px;
  font-size:20px;
  font-weight:bold;
  color: #4a4a4a;
  text-align:center;
  width:90vw;
}


.main{
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  height:90vh;
}
</style>
