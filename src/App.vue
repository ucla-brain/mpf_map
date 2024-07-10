<script>
import ImageMenu from './components/ImageMenu.vue'
import Carousel3d from './components/Carousel3d'
import BrainHeader from './components/Header'
import imageData from './assets/data.json'

export default {
  name : 'app',
  components: {
    ImageMenu,
    Carousel3d,
    BrainHeader
  },
  methods: {
    pickedImages(picked) {
      this.images = imageData[picked];
    }
  },
  data () {
    return {
        "images": imageData['SW110614-01B-ACAd/2-phal']
    }
  }
}
</script>

<template>
  <div id="app">
      <brain-header />
      <image-menu @picked-images="pickedImages" />
      <carousel3d :slides="images" />
  </div>
</template>

<style scoped>
  #blaRadios {
    position: relative;
    top: 205px;
  }

  .funkyradio input[type="radio"]:empty ~ label, .funkyradio input[type="checkbox"]:empty ~ label {
    margin-top: 1em;
  }  
</style>
 