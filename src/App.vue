<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { pyodideModule } from './modules/pyodide';


import InputNumber from 'primevue/inputnumber';
import { Button } from 'primevue';
import { computed, ref, type Ref, type ComputedRef, watch } from 'vue';
import { dystrybunataFt, funkcjaNiezawdnosciRt,funkcjaGestaft,funkcjaIntensywnoscilambdat,rozkladTrwalosciEta } from './modules/RelCalculator';
import Loading from '@/components/Loading.vue';
const numberOfElements: Ref<number> =ref(10)

const numberOfTimeSteps: Ref<number> =ref(10)

const radomValues: Ref<any> =ref({})


const F: Ref<any>= ref()
  const R: Ref<any>= ref()
    const f: Ref<any>= ref()
      const lam: Ref<any>= ref()
         const E: Ref<any>= ref()
watch([numberOfElements, numberOfTimeSteps], () => {
generateRandomValues()
})

const generateRandomValues=()=>{
  const dict: any={}
  for(let i=1;i<numberOfTimeSteps.value+1;i++){
   dict[i]=(Math.random()*numberOfElements.value).toFixed(0)
  }

  radomValues.value= dict
}

const caluclateValues=async()=>{

  console.log("calculating values")

  F.value=dystrybunataFt(radomValues.value,numberOfElements.value)
  R.value=funkcjaNiezawdnosciRt(radomValues.value,numberOfElements.value)
  f.value=funkcjaGestaft(radomValues.value,numberOfElements.value)
lam.value=funkcjaIntensywnoscilambdat(radomValues.value,numberOfElements.value)
E.value=rozkladTrwalosciEta(radomValues.value,numberOfElements.value)
}

watch(pyodideModule.isInitialized,(val)=>{
if(val===true){
  generateRandomValues()
}
})



const textBookExample=()=>{
  numberOfElements.value=35
  numberOfTimeSteps.value=10
  radomValues.value={
    1:0,
    2:3,
    3:3,
    4:5,
    5:8,
    6:7,
    7:6,
    8:2,
    9:1,
    10:0
  }
}

</script>

<template>

<div class="app centerEverything" v-if="pyodideModule.isInitialized.value==false">
  <Loading  label="Loading.."/>

</div>
<div class="app" v-else>
 <div class="main">

<div class="inputContainer">
Number of elements
<InputNumber v-model="numberOfElements" class="inputNumber" fluid  />
</div>
<div class="inputContainer" >
Number of time steps
<InputNumber v-model="numberOfTimeSteps" class="inputNumber" fluid   />
</div>
<div class="resultsContainer">

values:
{{ JSON.stringify(radomValues) }}
<br>
F:
{{ JSON.stringify(F) }}
<br>
R:
{{ JSON.stringify(R) }}
<br>

f:
{{ JSON.stringify(f) }}
<br>
lam:

{{ JSON.stringify(lam) }}


<br>
E:
{{ JSON.stringify(E) }}
  </div>

</div>

<Button label="caluculate"  @click="caluclateValues"/>
<Button label="textbook example"  @click="textBookExample"/>
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

.centerEverything{
  display:flex;
  align-items:center;
  justify-content:center;
  height:100vh;
  overflow: hidden;
  ;
}



.resultsContainer{
  border: black solid 2px;
  width: 80vw;
  overflow: scroll;
}

button{
  margin: 1rem;
}
</style>
