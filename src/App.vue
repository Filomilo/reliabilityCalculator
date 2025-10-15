<script setup lang="ts">
import { ref, type Ref, watch } from 'vue'
import InputNumber from 'primevue/inputnumber'
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

// Refs
const numberOfElements: Ref<number> = ref(10)
const numberOfTimeSteps: Ref<number> = ref(10)
const radomValues: Ref<any> = ref({})

const F: Ref<any> = ref()
const R: Ref<any> = ref()
const f: Ref<any> = ref()
const lam: Ref<any> = ref()
const E: Ref<any> = ref()

// Watchers
watch([numberOfElements, numberOfTimeSteps], () => {
  generateRandomValues()
})

watch(pyodideModule.isInitialized, (val) => {
  if (val === true) {
    generateRandomValues()
  }
})

// Functions
const generateRandomValues = () => {
  const dict: any = {}
  for (let i = 1; i <= numberOfTimeSteps.value; i++) {
    dict[i] = (Math.random() * numberOfElements.value).toFixed(0)
  }
  radomValues.value = dict
}

const caluclateValues = async () => {
  console.log('calculating values')
  F.value = dystrybunataFt(radomValues.value, numberOfElements.value)
  R.value = funkcjaNiezawdnosciRt(radomValues.value, numberOfElements.value)
  f.value = funkcjaGestaft(radomValues.value, numberOfElements.value)
  lam.value = funkcjaIntensywnoscilambdat(radomValues.value, numberOfElements.value)
  E.value = rozkladTrwalosciEta(radomValues.value, numberOfElements.value)
}

const textBookExample = () => {
  numberOfElements.value = 35
  numberOfTimeSteps.value = 10
  radomValues.value = {
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
      <div class="inputsWrapper hiddenDuringPrint">
        <div class="inputContainer">
          <label>Number of elements</label>
          <InputNumber v-model="numberOfElements" class="inputNumber" fluid />
        </div>

        <div class="inputContainer">
          <label>Number of time steps</label>
          <InputNumber v-model="numberOfTimeSteps" class="inputNumber" fluid />
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
            <tr v-for="(val, key) in radomValues" :key="key">
              <td>{{ key }}</td>
              <td>{{ val }}</td>
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
              <td>{{ key }}</td>
              <td>{{ val }}</td>
            </tr>
          </tbody>
        </table>


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
              <td>{{ key }}</td>
              <td>{{ val }}</td>
            </tr>
          </tbody>
        </table>


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
              <td>{{ key }}</td>
              <td>{{ val }}</td>
            </tr>
          </tbody>
        </table>



          </div>

    <div class ="result_element">
            <h3>Funkcja intensywnośći uszkodzeń λ*(t)</h3>
        <table class="resultsTable">
         <thead>
           <tr>
              <th>t</th>
              <th>lam</th>
            </tr>
          </thead>
         <tbody>
           <tr v-for="(val, key) in lam" :key="key">
              <td>{{ key }}</td>
              <td>{{ val }}</td>
            </tr>
          </tbody>
        </table>

    </div>


        <h3>Średnia trwałość E[T]</h3>
<p class="resultValue">
  {{ E !== undefined && E !== null ? E.toFixed(3) : '–' }}
</p>


      </div>
    </div>

    <!-- Buttons -->
    <div class="buttonsWrapper hiddenDuringPrint">
      <Button label="Calculate" @click="caluclateValues" />
      <Button label="Textbook Example" @click="textBookExample" />
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
  background-color: #333;
  color: #fff;
  border-radius: 6px;
  border: 1px solid #555;
  transition: background 0.2s;
  margin: 2rem 0 3rem; /* odstęp od dołu strony */
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.buttonsWrapper button:hover {
  background-color: #444 !important;
}

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
      page-break-inside: avoid !important;
    }
.result_element{
  page-break-inside: avoid !important;
  margin-bottom: 1.5rem !important;
}
}


tr td:last-child {
    width: 1%;
    white-space: nowrap;
}




</style>
