<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
    <router-view/>
	<van-tabbar v-show="$route.meta.tabbar" active-color="#ff6700" route v-model="active">
	  <van-tabbar-item icon="home-o" to="/">首页</van-tabbar-item>
	  <van-tabbar-item icon="search" to="/usershow">秀场</van-tabbar-item>
	  <van-tabbar-item icon="apps-o" to="/category" >分类</van-tabbar-item>
	  <van-tabbar-item icon="friends-o" to="/mine" >我的</van-tabbar-item>
	</van-tabbar>
	
	
  </div>
</template>
<script>
	export default {
	  data() {
	    return {
	      active: 0
	    }
	  },
	}
</script>


<style lang="less">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
