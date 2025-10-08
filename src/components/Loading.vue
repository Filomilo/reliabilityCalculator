<template>
  <div class="loadingComponent">
   <div class="loader">
</div> {{ props.label }}
  </div>

</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
  label: {
    type: String,
    required: false,
    default: 'Loading'
  }
});

</script>

<style lang="css">
/* HTML: <div class="loader"></div> */
.loader {
  width: 50px;
  aspect-ratio: 1;
  color: #000;
  border: 2px solid;
  display: grid;
  box-sizing: border-box;
  animation: l1 4s infinite linear;
}
.loader::before,
.loader::after {
  content: "";
  grid-area: 1/1;
  margin: auto;
  width: 70.7%;
  aspect-ratio: 1;
  border: 2px solid;
  box-sizing: content-box;
  animation: inherit;
}
.loader::after {
  width: 50%;
  aspect-ratio: 1;
  border: 2px solid;
  animation-duration: 2s;
}
@keyframes l1{
  100% {transform:rotate(1turn)}
}

.loadingComponent{
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:10px;
  font-size:1.5rem;
  color:#444;
}
</style>
