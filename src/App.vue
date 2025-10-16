<script setup lang="ts">
import { type ComputedRef, ref, type Ref, watch, computed } from 'vue'
import InputNumber from 'primevue/inputnumber'
import DatePicker from 'primevue/datepicker'
import Dropdown from 'primevue/dropdown'
import { Button } from 'primevue'
import Loading from '@/components/Loading.vue'
import { pyodideModule } from './modules/pyodide'
import {
  dystrybunataFt,
  funkcjaNiezawdnosciRt,
  funkcjaGestaft,
  funkcjaIntensywnoscilambdat,
  rozkladTrwalosciEta
} from './modules/RelCalculator'
import { Chart, Grid, Line } from 'vue3-charts'
import type { ChartAxis } from 'vue3-charts/dist/types'

// Refs
const numberOfElements: Ref<number> = ref(10)
const numberOfTimeSteps: Ref<number> = ref(10)
const Values: Ref<any> = ref({})


const timeAddtion:ComputedRef<number>=computed(()=>{
  return durationStep.value * (selectedPeriosd.value as any) .value
})

  const datetimeStart = ref(new Date());
    const durationStep=ref( 1);

const F: Ref<any> = ref()
const R: Ref<any> = ref()
const f: Ref<any> = ref()
const lam: Ref<any> = ref()
const E: Ref<any> = ref()


const updateNumbers=()=>{

let newValues:any={}
for (let i = 1; i <= numberOfTimeSteps.value; i++) {
  newValues[i] = 0
}
  console.log('updating numbers to', newValues)
Values.value = newValues
}

const roundUpValue=(val:number, step:number=3)=>{
  return Math.round(val * Math.pow(10, step)) / Math.pow(10, step);
}

watch([numberOfTimeSteps], () => {
updateNumbers()
})
updateNumbers(  )

// Watchers
// watch([numberOfElements, numberOfTimeSteps], () => {
//   generateRandomValues()
// })

// watch(pyodideModule.isInitialized, (val) => {
//   if (val === true) {
//     textBookExample()
// caluclateValues()
//   }
// })


const onRandomizeButton=() => {
  generateRandomValues()
}
const periods = ref([
    { name: 's', code: 's', value: 1, limit: 60 },
    { name: 'm', code: 'm', value: 60, limit: 60 },
    { name: 'h', code: 'h', value: 60*60, limit: 24 },
    { name: 'd', code: 'd', value: 60*60*24, limit: 999999999999999 }
]);


const selectedPeriosd = ref( periods.value[0]);

// Functions
const generateRandomValues = () => {
  const dict: any = {}
  for (let i = 1; i <= numberOfTimeSteps.value; i++) {
    dict[i] = (Math.random() * numberOfElements.value).toFixed(0)
  }
  Values.value = dict
}

const caluclateValues = async () => {
  console.log('calculating values')
  F.value = dystrybunataFt(Values.value, numberOfElements.value)
  R.value = funkcjaNiezawdnosciRt(Values.value, numberOfElements.value)
  f.value = funkcjaGestaft(Values.value, numberOfElements.value)
  lam.value = funkcjaIntensywnoscilambdat(Values.value, numberOfElements.value)
  E.value = rozkladTrwalosciEta(Values.value, numberOfElements.value)
}

const timeToString = (time: number) => {

  const totalSeconds = Math.floor(time )
  const hours = Math.floor(totalSeconds / 3600)
  const minutes = Math.floor((totalSeconds % 3600) / 60)
  const seconds = totalSeconds % 60
  return `${hours}h ${minutes}m ${seconds}s`
}
  const updateModelType = (val: Date | null) => {

  }
const textBookExample = () => {
  numberOfElements.value = 35
  numberOfTimeSteps.value = 10
  Values.value = {
    1: 0,
    2: 3,
    3: 3,
    4: 5,
    5: 8,
    6: 7,
    7: 6,
    8: 2,
    9: 1,
    10: 0
  }
}

const keyToDate=(key: number):String => {
  return new Date(datetimeStart.value.getTime()  + (key*timeAddtion.value*1000)).toUTCString()
}






import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { color } from 'chart.js/helpers'
import {  registerables } from 'chart.js'
import { Colors } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale,...registerables,Colors)



const FtGraphData=computed(()=>{
  return {
        labels: Object.keys(F.value || {}).map((key)=> timeToString(timeAddtion.value*Number(key))),
        datasets: [
          {
            label: 'F*(t)',
            data: Object.values(F.value || {}),
            borderColor: '#f87979',
            backgroundColor: 'rgba(248, 121, 121, 0.5)',
          },
        ],
      }
})



const RtGraphData=computed(()=>{
  return {
        labels: Object.keys(R.value || {}).map((key)=> timeToString(timeAddtion.value*Number(key))),
        datasets: [
          {
            label: 'R*(t)',
            data: Object.values(R.value || {}),
            borderColor: '#f87979',
            backgroundColor: 'rgba(248, 121, 121, 0.5)',
          },
        ],
      }
})

const ftGraphData=computed(()=>{
  return {
        labels: Object.keys(f.value || {}).map((key)=> timeToString(timeAddtion.value*Number(key))),
        datasets: [
          {
            label: 'f*(t)',
            data: Object.values(f.value || {}),
            borderColor: '#f87979',
            backgroundColor: 'rgba(248, 121, 121, 0.5)',
          },
        ],
      }
})

const lamGraphData=computed(()=>{
  return {
        labels: Object.keys(lam.value || {}).map((key)=> timeToString(timeAddtion.value*Number(key))),
        datasets: [
          {
            label: 'λ*(t)',
            data: Object.values(lam.value || {}),
            borderColor: '#f87979',
            backgroundColor: 'rgba(248, 121, 121, 0.5)',
          },
        ],
      }
})


const chartOptions= {
        responsive: true
      }

</script>

<template>
  <div
    class="app centerEverything hiddenDuringPrint"
    v-if="pyodideModule.isInitialized.value == false"
  >
    <Loading label="Loading.." />
  </div>

  <div class="app" v-else>


    <div class="main">
      <!-- Inputs -->
<!-- {{ JSON.stringify(timeAddtion) }} -->


        <!-- {{ JSON.stringify(Values) }}
{{ JSON.stringify(numberOfElements) }} -->
      <div class="inputsWrapper hiddenDuringPrint">


  <div class="inputContainer">
          <label>Start pomiarów</label>
          <DatePicker v-model="datetimeStart" class="inputNumber" fluid  showTime hourFormat="24" :updateModelType="undefined" />
        </div>

          <div class="inputContainer">
          <label>Okresowść pomiarów</label>
          <div style="flex-direction: row; display: flex; gap: 10px; align-items: center; width: 100%;">
            <InputNumber  :min="1" v-model="durationStep" class="inputNumber" style="width: 40%;" fluid  />
  <div class="card flex justify-content-center">
        <Dropdown v-model="selectedPeriosd" :options="periods" optionLabel="name" placeholder="-" class="w-full md:w-14rem" />

          </div>
            </div>
        </div>


        <div class="inputContainer">
          <label>Ilość elementów</label>
          <InputNumber v-model="numberOfElements" class="inputNumber" fluid :min="1" />
        </div>

        <div class="inputContainer">
          <label>Ilość pomiarów</label>
          <InputNumber v-model="numberOfTimeSteps" class="inputNumber" fluid :min="1" />
        </div>


            <!-- Buttons -->
    <div class="buttonsWrapper hiddenDuringPrint">
           <Button label="Randomize" @click="onRandomizeButton" />
      <Button label="Calculate" @click="caluclateValues" />
      <Button label="Textbook Example" @click="textBookExample" />
    </div>
      </div>

      <!-- Results -->
      <div class="resultsWrapper">

    <div class ="result_element">
            <h3>Zarejestrowane uszkodzone elementy</h3>
        <table class="resultsTable">
          <thead>
            <tr>
              <th>Moment</th>
              <th>Uszkodzone elementy</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(val, key) in Values" :key="key">
              <td>{{ keyToDate(key) }}</td>

              <td class="tdInput"><InputNumber @value-change="(newval)=>{Values[key]=newval}" :modelValue="Values[key]" class="inputNumber" fluid :min="1" :max="numberOfElements"/>
</td>
            </tr>
          </tbody>
        </table>
    </div>


    <div class ="result_element">


           <h3>Empiryczna dystrybuanta trwałości czasu pracy do uszkodzenia F*(t)</h3>
        <table class="resultsTable">
         <thead>
           <tr>
              <th>t</th>
              <th>F</th>
            </tr>
          </thead>
         <tbody>
           <tr v-for="(val, key) in F" :key="key">
              <td>{{ timeToString(timeAddtion*key) }}</td>
              <td>{{ roundUpValue(val) }}</td>
            </tr>
          </tbody>
        </table>
<div
 :style="FtGraphData.labels.length>0?'':'display: none;'"
  class="graphContainer"
 >
  <Bar

    id="my-chart-id-Ft"
    :options="chartOptions"
    :data="FtGraphData as any"

  />
</div>

    </div>

    <div class ="result_element">
            <h3>Funkcja niezawodnośći R*(t)</h3>
        <table class="resultsTable">
         <thead>
           <tr>
              <th>t</th>
              <th>R</th>
            </tr>
          </thead>
         <tbody>
           <tr v-for="(val, key) in R" :key="key">
              <td>{{ timeToString(timeAddtion*key) }}</td>
              <td>{{ roundUpValue(val) }}</td>
            </tr>
          </tbody>
        </table>
<div
 :style="FtGraphData.labels.length>0?'':'display: none;'"
  class="graphContainer"
 >
  <Bar

    id="my-chart-id-Rt"
    :options="chartOptions"
    :data="RtGraphData as any"

  />
</div>

    </div>


          <div class ="result_element">

                  <h3>Funkcja gęstości prawdobieństwa  f*(t)</h3>
        <table class="resultsTable">
         <thead>
           <tr>
              <th>t</th>
              <th>f</th>
            </tr>
          </thead>
         <tbody>
           <tr v-for="(val, key) in f" :key="key">
              <td>{{ timeToString(timeAddtion*key) }}</td>
              <td>{{ roundUpValue( val) }}</td>
            </tr>
          </tbody>
        </table>

<div
 :style="FtGraphData.labels.length>0?'':'display: none;'"
 class="graphContainer"
 >
  <Bar

    id="my-chart-id-ft"
    :options="chartOptions"
    :data="ftGraphData as any"

  />
</div>

          </div>

    <div class ="result_element">
            <h3>Funkcja intensywnośći uszkodzeń λ*(t)</h3>
        <table class="resultsTable">
         <thead>
           <tr>
              <th>t</th>
              <th>λ</th>
            </tr>
          </thead>
         <tbody>
           <tr v-for="(val, key) in lam" :key="key">
              <td>{{ timeToString(timeAddtion*key) }}</td>
              <td>{{roundUpValue( val) }}</td>
            </tr>
          </tbody>
        </table>
<div
 :style="FtGraphData.labels.length>0?'':'display: none;'"
  class="graphContainer"
 >
  <Bar

    id="my-chart-id-lam"
    :options="chartOptions"
    :data="lamGraphData  as any"

  />
</div>
    </div>
  <div class ="result_element" id="final_result_elemnt">

        <h3>Średnia trwałość E[T]</h3>
<p class="resultValue">
  {{ E !== undefined && E !== null ? (E/durationStep).toFixed(3) : '–' }} {{ selectedPeriosd?.name }}
</p>
  </div>



      </div>
    </div>


  </div>
</template>


<style>
html, body {
  margin: 0;
  padding: 0;
  background-color: #121212;
  color: #f5f5f5;
  min-height: 100vh;
  width: 100%;
}
</style>

<style scoped>

.graphContainer {
  width: 100%;
  max-width: 800px;
  margin-top: 2rem;
  margin-bottom: 4rem;
}


/* Tło aplikacji*/
.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  background-color: #121212;
  min-height: 100vh;
  width: 100%;
  padding: 2rem;
  box-sizing: border-box;
  color: #f5f5f5;
}
/* Layout główny */
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

/* Inputy */
.inputsWrapper {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  margin-bottom: 2rem;
  flex-wrap: wrap; /* pozwala zawijać na małych ekranach */
  justify-content: center;
}

.inputContainer {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  width: 180px;
  align-items: flex-start;
}

.inputNumber {
  width: 180px;
}

/* Wyniki */
.resultsWrapper {
  border: 2px solid #444;
  border-radius: 8px;
  padding: 1.5rem;
  background-color: #1e1e1e;
  color: #f5f5f5;
  width: 80vw;
  max-width: 900px;
  margin-top: 1rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

.resultsTable {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  table-layout: fixed;
}

.resultsTable th,
.resultsTable td {
  border: 1px solid #555;
  padding: 0.5rem;
  text-align: center;
}

.resultsTable th {
  background-color: #333;
}

.resultsList {
  list-style: none;
  padding: 0;
  margin: 0;
}

.resultsList li {
  margin: 0.3rem 0;
  font-size: 1rem;
}
.resultValue {
  background-color: #1e1e1e;
  border: 1px solid #555;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  display: inline-block;
  min-width: 120px;
  text-align: center;
  margin-bottom: 1.5rem;
  font-weight: bold;
  font-size: 1.1rem;
  color: #f5f5f5;
}

/* Przyciski */
.buttonsWrapper {

  color: #fff;

  transition: background 0.2s;
  margin: 2rem 0 3rem; /* odstęp od dołu strony */
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* .buttonsWrapper button:hover {
  background-color: #444 !important;
} */

/* Centrowanie przy ładowaniu */
.centerEverything {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

/* Responsywność */
@media (max-width: 768px) {
  .resultsWrapper {
    width: 95vw;
    padding: 1rem;
  }

  .inputsWrapper {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .inputContainer {
    width: 100%;
    max-width: 280px;
    align-items: center;
  }

  .inputNumber {
    width: 100%;
    background: #2a2a2a;
   color: #fff;
   border: 1px solid #444;
   border-radius: 6px;
   padding: 0.3rem 0.5rem;
  }
}

.tdInput span *{
  background-color: inherit !important;
  width: 100% !important;
  text-align: center !important;
  height: 100% !important;
  border: none !important;
}
.tdInput{
  border: #555  solid 2px !important;
}
@media print {


  .hiddenDuringPrint {
    display: none !important;
  }


  .resultsWrapper{
    border: none !important;
    box-shadow: none !important;
  }
  .app {
    padding: 1cm !important;
  }
  .resultsTable th, .resultsTable td {
    border: 1px solid #000 !important;
  }
  .resultsTable th {
    background-color: #ccc !important;
    -webkit-print-color-adjust: exact;
  }
  .resultValue {
    border: 1px solid #000 !important;  }

    .resultsTable{
    }
.resultsWrapper{
  display: flex !important;
  flex-wrap: wrap !important;
  width: 100vw !important;
}
.result_element{
  width: 5cm !important;
  text-align: center !important;
  margin: 0.2cm;
}
.result_element *{
  font-size: 0.8rem;
}
tr td:last-child {
    width: 1%;
    white-space: nowrap;
}

.resultsTable{
width: 10rem !important
}
.resultsTable *{
font-size: 0.5rem !important;
}
.resultsTable tr *{
height: 0.5cm !important;
overflow: hidden;
padding: 0.1cm;
}

.result_element h3{
  height: 4rem !important;
}

.tdInput *{
  border: none !important;
}
input{
  border: none !important;
}
.resultValue{
  border: none !important;
}

.graphContainer {
  width: 50cm !important;
  overflow: hidden;
}

.graphContainer canvas {
  width: 100% !important;
  height: auto !important;
  width: 10cm !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: auto !important;

}
.graphContainer *{
  margin: auto !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 10cm !important;
}


.result_element{
  margin: 0 !important;
   width: 10cm !important;
   overflow: hidden;
}


.graphContainer{
  width: 100% !important;
  max-width: 100% !important;
  height: auto !important;
}

.graphContainer canvas{
  width: 100% !important;
  max-width: 100% !important;
  height: auto !important;
}

.result_element {
  justify-content: center !important;
  align-items: center !important;
  display: flex !important;
  flex-direction: column !important;
}

.result_element{

}

.result_element{
    aspect-ratio: 210 / 297 !important;
}

#__vue-devtools-container__ {
  display: none !important;
}

.resultsWrapper{
  border: none !important;
  box-shadow: none !important;
  background-color: none !important;
}
.main{
  background-color: none !important;
}
.app{
  background-color: #fff !important;
  color: #000 !important;
}
body html{
  background-color: #fff !important;
  color: #000 !important;
}
#app{
  background-color: #fff !important;
  color: #000 !important;
}

html, body *{
  background-color: #fff !important;
  color: #000 !important;
}
.resultsWrapper *{
  background-color: #fff !important;
  color: #000 !important;
}
.resultsWrapper{
  background-color: #fff !important;
  color: #000 !important;
}
:root *{
  background-color: #fff !important;
}

.resultsWrapper{
}

.result_element{
  page-break-inside: avoid !important;
  width: 20cm !important ;
}

#final_result_elemnt{
  width: 10cm !important ;
  height: 2cm !important ;
}

.result_element {
  display: flex;
  justify-content: center;
  align-items: flex-start;
}
.result_element *{

}
}
</style>
