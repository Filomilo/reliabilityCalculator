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
    class="app centerEverything"
    v-if="pyodideModule.isInitialized.value == false"
  >
    <Loading label="Loading.." />
  </div>

  <div class="app" v-else>
    <div class="main">
      <!-- Inputs -->
      <div class="inputsWrapper">
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
        <h3>Generated Values</h3>
        <table class="resultsTable">
          <thead>
            <tr>
              <th>Time Step</th>
              <th>Value</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(val, key) in radomValues" :key="key">
              <td>{{ key }}</td>
              <td>{{ val }}</td>
            </tr>
          </tbody>
        </table>

        <h3>Calculated Functions</h3>
        <ul class="resultsList">
          <li><strong>F:</strong> {{ F }}</li>
          <li><strong>R:</strong> {{ R }}</li>
          <li><strong>f:</strong> {{ f }}</li>
          <li><strong>λ:</strong> {{ lam }}</li>
          <li><strong>E:</strong> {{ E }}</li>
        </ul>
      </div>
    </div>

    <!-- Buttons -->
    <div class="buttonsWrapper">
      <Button label="Calculate" @click="caluclateValues" />
      <Button label="Textbook Example" @click="textBookExample" />
    </div>
  </div>
</template>

<style scoped>
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
}

.resultsTable {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
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

/* Przyciski */
.buttonsWrapper {
  margin: 2rem 0 3rem; /* odstęp od dołu strony */
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
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
  }
}
</style>
