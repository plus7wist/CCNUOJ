<template>
  <div class="maincontainer" id="app">
    <el-header>
      <p class="header-p">Online Judge And Analysis System</p>
    </el-header>
    <el-main>
      <div class="content">
        <homeheader/>
      </div>
    </el-main>
    <el-footer>
      <p class="foot-p"> ccnu-acm 测试版</p>
    </el-footer>
  </div>
</template>

<script>
import homeheader from '../components/homeheader'
import photowalls from '../components/photowalls'
import queslist from '../components/queslist'
//  Vue.components('home-header',{
//  })
//  new Vue({el:'#app'})    全局创建components
// webpack注册  2018.9.26 pyl
export default {
  name: 'home',
  data () {
    return {}
  },
  components: {
    homeheader,
    photowalls,
    queslist
  }
}
</script>

<style lang="css" scoped>

  .header-p {
    text-indent: 0em;
    padding-left: 5em;
    font-size: 40%;
  }

  .foot-p {
    text-indent: -5em;
    padding-left: 35em;
    font-size: 40%;
  }

  .maincontainer {
    height: 100%;
    margin: 0;
    padding: 0;

  }

  .el-header {
    height: 100px;
    line-height: 100px;
    background: rgb(197, 207, 221);
    width: 100%;
    position: absolute;
    z-index: 5;
    top: 0;
    text-align: center;
    color: #333;
  }

  .el-footer {
    height: 100px;
    line-height: 100px;
    background: rgb(197, 207, 221);
    width: 100%;
    position: absolute;
    z-index: 200;
    bottom: 0;
    text-align: center;
    color: #333;
  }

  .el-main {
    width: 100%;
    overflow: auto;
    top: 30px;
    position: absolute;
    z-index: 10;
    bottom: 100px;
  }

  .content {
    padding: 10px;
  }

</style>
