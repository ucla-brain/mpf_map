<script>
import jsonData from '@/assets/imageMenu.json';

export default {
  data () {
    return {
      picked: 'SW110614-01B-ACAd/2-phal',
      "projections": []
    }
  },
  methods: {
    computeId(i, j) {
      let count = 0;
      for (let k = 0; k < i; k++) {
        count += this.projections[k].regions.length;
      }
      return count + j + 1;
    },    
    change() {
      this.$emit('picked-images', this.picked);
    }
  },
  mounted() {
    this.projections = jsonData.projections;
  }
};
</script>

<template>
  <div id="blaRadios" class="funkyradio col-xs-2">
    <div :class="projection.class" v-for="(projection, i) in projections" :key="i">
      <span>{{projection.label}}</span>
      <div class="funkyradio-default" v-for="(reg, j) in projection.regions" :key="j">
        <input type="radio" :id="computeId(i, j)" :value="reg.class" v-model="picked" v-on:change="change()">
        <label :for="computeId(i, j)" style="margin-top: 1.4em;">
          <span :class="reg.class">{{reg.label}}</span>
        </label>
      </div>
    </div>
  </div>
</template>

<style scoped>
.blaam {
  color:rgb(82,63,195);
}

.blaal {
  color: rgb(187,63,195);
}

.blaac {
  color: rgb(3,144,102);
}

.blap {
  color: rgb(63,128,193);
}

.blav {
  color: rgb(43,31,115);
}

.bmap {
  color: rgb(108,31,115);
}

.la {
  color: rgb(31,82,115);
}

.anterograde, .retrograde {
  margin-top: 0.2em;
  padding-bottom: 30px;  
}

.funkyradio div {
  clear: both;
  overflow: hidden;
}

.funkyradio label {
  width: 100%;
  border-radius: 3px;
  border: 1px solid #D1D3D4;
  font-weight: normal;
}

.funkyradio input[type="radio"]:empty,
.funkyradio input[type="checkbox"]:empty {
  display: none;
}

.funkyradio input[type="radio"]:empty ~ label,
.funkyradio input[type="checkbox"]:empty ~ label {
  position: relative;
  line-height: 2.5em;
  text-indent: 3.25em;
  margin-top: 2em;
  cursor: pointer;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

.funkyradio input[type="radio"]:empty ~ label:before,
.funkyradio input[type="checkbox"]:empty ~ label:before {
  position: absolute;
  display: block;
  top: 0;
  bottom: 0;
  left: 0;
  content: '';
  width: 2.5em;
  background: #D1D3D4;
  border-radius: 3px 0 0 3px;
}

.funkyradio input[type="radio"]:hover:not(:checked) ~ label,
.funkyradio input[type="checkbox"]:hover:not(:checked) ~ label {
  color: #888;
}

.funkyradio input[type="radio"]:hover:not(:checked) ~ label:before,
.funkyradio input[type="checkbox"]:hover:not(:checked) ~ label:before {
  content: '\2714';
  text-indent: .9em;
  color: #C2C2C2;
}

.funkyradio input[type="radio"]:checked ~ label,
.funkyradio input[type="checkbox"]:checked ~ label {
  color: #777;
}

.funkyradio input[type="radio"]:checked ~ label:before,
.funkyradio input[type="checkbox"]:checked ~ label:before {
  content: '\2714';
  text-indent: .9em;
  color: #333;
  background-color: #ccc;
}

.funkyradio input[type="radio"]:focus ~ label:before,
.funkyradio input[type="checkbox"]:focus ~ label:before {
  box-shadow: 0 0 0 3px #999;
}

.funkyradio-default input[type="radio"]:checked ~ label:before,
.funkyradio-default input[type="checkbox"]:checked ~ label:before {
  color: #333;
  background-color: #ccc;
}

.funkyradio-primary input[type="radio"]:checked ~ label:before,
.funkyradio-primary input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #337ab7;
}

.funkyradio-success input[type="radio"]:checked ~ label:before,
.funkyradio-success input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #5cb85c;
}

.funkyradio-danger input[type="radio"]:checked ~ label:before,
.funkyradio-danger input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #d9534f;
}

.funkyradio-warning input[type="radio"]:checked ~ label:before,
.funkyradio-warning input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #f0ad4e;
}

.funkyradio-info input[type="radio"]:checked ~ label:before,
.funkyradio-info input[type="checkbox"]:checked ~ label:before {
  color: #fff;
  background-color: #5bc0de;
}

span {
  font-weight: bold;  
}
</style>
