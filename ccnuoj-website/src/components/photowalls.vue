<template>
  <div>
    <el-carousel height="400px" indicator-position="outside">
      <el-carousel-item :key="index" v-for="(img,index) in photoList">
        <img v-bind:src="img.url">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  name: 'photowalls',
  data () {
    return {
      photoList: [
        {url: require('../assets/photocarousel/ccnuacm02.jpg')},
        {url: require('../assets/photocarousel/ccnuacm03.jpg')},
        {url: require('../assets/photocarousel/ccnuacm01.png')},
        {url: require('../assets/photocarousel/ccnuacm04.jpg')}
      ]
    }
  },
  components: {}
}
</script>

<style>

  img {
    width: auto;
    height: auto;
    max-width: 100%;
    max-height: 100%;
  }

  .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
